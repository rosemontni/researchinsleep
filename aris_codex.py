#!/usr/bin/env python3
"""
Minimal Codex-native ARIS wrapper.

This script keeps the local workspace small and fetches upstream ARIS skills
on demand instead of cloning the upstream repository into the project.
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import textwrap
import urllib.request
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
CONFIG_PATH = ROOT / "config" / "upstream_skills.json"
CACHE_ROOT = ROOT / ".aris-cache"
RUNS_ROOT = ROOT / ".aris" / "runs"


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def load_config() -> dict[str, Any]:
    return json.loads(CONFIG_PATH.read_text(encoding="utf-8"))


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def slugify(value: str) -> str:
    cleaned = []
    for ch in value.lower():
        if ch.isalnum():
            cleaned.append(ch)
        elif ch in {" ", "-", "_"}:
            cleaned.append("-")
    text = "".join(cleaned).strip("-")
    while "--" in text:
        text = text.replace("--", "-")
    return text or "run"


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    ensure_dir(path.parent)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def run_subprocess(cmd: list[str], timeout: int = 30) -> tuple[int, str]:
    try:
        result = subprocess.run(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            timeout=timeout,
            check=False,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        return 1, str(exc)
    return result.returncode, result.stdout.strip()


def fetch_text(url: str) -> str:
    with urllib.request.urlopen(url) as response:
        return response.read().decode("utf-8")


def cache_skill(skill_name: str, force: bool = False) -> Path:
    config = load_config()
    skill = config["skills"][skill_name]
    cache_dir = CACHE_ROOT / "skills" / skill_name
    cache_path = cache_dir / "SKILL.md"
    meta_path = cache_dir / "metadata.json"
    if cache_path.exists() and not force:
        return cache_path

    ensure_dir(cache_dir)
    content = fetch_text(skill["raw_url"])
    cache_path.write_text(content, encoding="utf-8")
    write_json(
        meta_path,
        {
            "skill": skill_name,
            "source_url": skill["raw_url"],
            "fetched_at": utc_now(),
        },
    )
    return cache_path


@dataclass
class RunState:
    run_id: str
    pipeline: str
    goal: str
    current_stage_index: int
    stages: list[str]
    created_at: str
    updated_at: str
    status: str
    overrides: dict[str, Any]

    @property
    def current_stage(self) -> str | None:
        if self.current_stage_index >= len(self.stages):
            return None
        return self.stages[self.current_stage_index]

    @property
    def run_dir(self) -> Path:
        return RUNS_ROOT / self.run_id

    @property
    def state_path(self) -> Path:
        return self.run_dir / "state.json"

    def to_dict(self) -> dict[str, Any]:
        return {
            "run_id": self.run_id,
            "pipeline": self.pipeline,
            "goal": self.goal,
            "current_stage_index": self.current_stage_index,
            "stages": self.stages,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "status": self.status,
            "overrides": self.overrides,
        }


def load_run(run_id: str) -> RunState:
    state_path = RUNS_ROOT / run_id / "state.json"
    payload = read_json(state_path)
    return RunState(**payload)


def save_run(run: RunState) -> None:
    run.updated_at = utc_now()
    write_json(run.state_path, run.to_dict())


def create_run(pipeline: str, goal: str, run_id: str | None, overrides: dict[str, Any]) -> RunState:
    config = load_config()
    stages = config["pipelines"][pipeline]
    if not run_id:
        run_id = f"{utc_now().split('T')[0]}-{slugify(goal)[:32]}"
    run = RunState(
        run_id=run_id,
        pipeline=pipeline,
        goal=goal,
        current_stage_index=0,
        stages=stages,
        created_at=utc_now(),
        updated_at=utc_now(),
        status="in_progress",
        overrides=overrides,
    )
    ensure_dir(run.run_dir / "prompts")
    ensure_dir(run.run_dir / "notes")
    save_run(run)
    return run


def render_stage_prompt(run: RunState, skill_name: str, skill_body: str) -> str:
    prompt = f"""\
# ARIS Upstream Skill Wrapper

You are running an upstream ARIS skill inside a local Codex workflow wrapper.

## Local Wrapper Goals

- Use the upstream skill below as the authoritative workflow specification.
- Adapt any Claude Code specific wording, slash-command assumptions, or MCP references into direct Codex execution inside this workspace.
- Prefer writing durable artifacts to disk so the run can resume cleanly.
- Keep all local workflow state under `.aris/runs/{run.run_id}/`.

## Run Context

- Run ID: `{run.run_id}`
- Pipeline: `{run.pipeline}`
- Goal: `{run.goal}`
- Stage: `{skill_name}`
- Remaining stages: `{", ".join(run.stages[run.current_stage_index:])}`

## Local Execution Rules

- Treat this workspace as the project root.
- If the upstream skill expects external review tools that are unavailable, continue with the strongest direct Codex equivalent and note the substitution explicitly.
- Before finishing this stage, write a concise stage report to `.aris/runs/{run.run_id}/notes/{skill_name}.md`.
- If the stage is substantially complete, write `.aris/runs/{run.run_id}/notes/{skill_name}.complete.json` with:
  - `stage`
  - `completed_at`
  - `summary`
  - `next_stage`
- If blocked, write `.aris/runs/{run.run_id}/notes/{skill_name}.blocked.md` describing the blocker and the minimum input needed.

## Upstream Skill

Source of truth follows below.

```md
{skill_body}
```
"""
    return textwrap.dedent(prompt)


def prompt_path_for(run: RunState, skill_name: str) -> Path:
    index = run.current_stage_index + 1
    return run.run_dir / "prompts" / f"{index:02d}-{skill_name}.md"


def stage_complete_path(run: RunState, stage_name: str) -> Path:
    return run.run_dir / "notes" / f"{stage_name}.complete.json"


def stage_blocked_path(run: RunState, stage_name: str) -> Path:
    return run.run_dir / "notes" / f"{stage_name}.blocked.md"


def parse_stage_complete(path: Path) -> dict[str, Any]:
    payload = read_json(path)
    required = {"stage", "completed_at", "summary", "next_stage"}
    missing = sorted(required - set(payload))
    if missing:
        raise ValueError(f"missing keys: {', '.join(missing)}")
    return payload


def validate_stage_markers(run: RunState, stage_name: str) -> tuple[bool, str]:
    complete_path = stage_complete_path(run, stage_name)
    blocked_path = stage_blocked_path(run, stage_name)
    if complete_path.exists():
        try:
            payload = parse_stage_complete(complete_path)
        except (json.JSONDecodeError, ValueError) as exc:
            return False, f"invalid completion marker {complete_path}: {exc}"
        if payload["stage"] != stage_name:
            return False, f"completion marker stage mismatch: expected {stage_name}, got {payload['stage']}"
        return True, f"complete: {complete_path}"
    if blocked_path.exists():
        return True, f"blocked: {blocked_path}"
    return False, "no completion or blocker marker found"


def detect_local_codebase() -> tuple[bool, str]:
    signals = [ROOT / "pyproject.toml", ROOT / "adrd", ROOT / "paper", ROOT / "tests"]
    existing = [path.name for path in signals if path.exists()]
    if existing:
        return True, f"local project signals found: {', '.join(existing)}"
    return False, "no local codebase signals found"


def detect_paper_toolchain() -> tuple[bool, str]:
    local_tectonic = ROOT / "tectonic.exe"
    if local_tectonic.exists():
        return True, f"local tectonic found at {local_tectonic}"
    for candidate in ("tectonic", "latexmk", "pdflatex"):
        code, output = run_subprocess([candidate, "--version"], timeout=15)
        if code == 0:
            first_line = output.splitlines()[0] if output else candidate
            return True, f"{candidate} available: {first_line}"
    return False, "no LaTeX toolchain detected (tectonic/latexmk/pdflatex)"


def run_doctor(codex_bin: str, pipeline: str | None = None) -> dict[str, Any]:
    config = load_config()
    pipeline_name = pipeline or "research-pipeline"
    pipeline_stages = config["pipelines"].get(pipeline_name, [])
    codex_code, codex_output = run_subprocess([os.path.expandvars(codex_bin), "--version"])
    codebase_ok, codebase_msg = detect_local_codebase()
    paper_ok, paper_msg = detect_paper_toolchain()
    upstream_ok = bool(config.get("skills")) and bool(config.get("pipelines"))
    return {
        "workspace": str(ROOT),
        "pipeline": pipeline_name,
        "stages": pipeline_stages,
        "checks": {
            "upstream_config": {
                "ok": upstream_ok,
                "details": "upstream skills and pipelines loaded" if upstream_ok else "missing upstream skill config",
            },
            "codex_cli": {
                "ok": codex_code == 0,
                "details": codex_output.splitlines()[0] if codex_output else "codex CLI check failed",
            },
            "local_codebase": {
                "ok": codebase_ok,
                "details": codebase_msg,
            },
            "paper_toolchain": {
                "ok": paper_ok,
                "details": paper_msg,
            },
        },
    }


def cmd_doctor(args: argparse.Namespace) -> int:
    report = run_doctor(args.codex_bin, args.pipeline)
    print(json.dumps(report, ensure_ascii=False, indent=2))

    fatal_checks = ("upstream_config", "codex_cli")
    failed = [name for name in fatal_checks if not report["checks"][name]["ok"]]
    return 0 if not failed else 2


def cmd_pipelines(_: argparse.Namespace) -> int:
    config = load_config()
    for name, stages in config["pipelines"].items():
        print(f"{name}: {' -> '.join(stages)}")
    return 0


def cmd_skills(_: argparse.Namespace) -> int:
    config = load_config()
    for name, meta in config["skills"].items():
        print(f"{name}: {meta['purpose']}")
    return 0


def cmd_init(args: argparse.Namespace) -> int:
    overrides = {}
    if args.ref_paper:
        overrides["ref_paper"] = args.ref_paper
    if args.base_repo:
        overrides["base_repo"] = args.base_repo
    run = create_run(args.pipeline, args.goal, args.run_id, overrides)
    print(f"Initialized run: {run.run_id}")
    print(f"Current stage: {run.current_stage}")
    print(f"State file: {run.state_path}")
    return 0


def cmd_status(args: argparse.Namespace) -> int:
    run = load_run(args.run_id)
    print(json.dumps(run.to_dict(), ensure_ascii=False, indent=2))
    return 0


def cmd_fetch(args: argparse.Namespace) -> int:
    path = cache_skill(args.skill, force=args.force)
    print(path)
    return 0


def cmd_next(args: argparse.Namespace) -> int:
    run = load_run(args.run_id)
    if run.status == "completed":
        print(f"Run {run.run_id} is already completed.")
        return 0
    if run.current_stage is None:
        print(f"Run {run.run_id} has no remaining stages.")
        return 0

    skill_name = run.current_stage
    skill_path = cache_skill(skill_name, force=args.refresh)
    skill_body = skill_path.read_text(encoding="utf-8")
    prompt = render_stage_prompt(run, skill_name, skill_body)
    output_path = prompt_path_for(run, skill_name)
    ensure_dir(output_path.parent)
    output_path.write_text(prompt, encoding="utf-8")

    print(f"Stage: {skill_name}")
    print(f"Prompt written to: {output_path}")
    return 0


def cmd_advance(args: argparse.Namespace) -> int:
    run = load_run(args.run_id)
    if run.status == "completed":
        print(f"Run {run.run_id} is already completed.")
        return 0

    run.current_stage_index += 1
    if run.current_stage_index >= len(run.stages):
        run.status = "completed"
        save_run(run)
        print(f"Run {run.run_id} completed.")
        return 0

    save_run(run)
    print(f"Advanced run {run.run_id} to stage: {run.current_stage}")
    return 0


def cmd_run(args: argparse.Namespace) -> int:
    run = load_run(args.run_id)
    if run.current_stage is None or run.status == "completed":
        print(f"Run {run.run_id} has no runnable current stage.")
        return 0

    skill_name = run.current_stage
    prompt_file = prompt_path_for(run, skill_name)
    if not prompt_file.exists():
        cmd_next(argparse.Namespace(run_id=args.run_id, refresh=False))

    prompt_text = prompt_file.read_text(encoding="utf-8")
    codex_bin = os.path.expandvars(args.codex_bin)
    output_file = run.run_dir / "notes" / f"{skill_name}.codex-last-message.txt"
    log_file = run.run_dir / "notes" / f"{skill_name}.codex-exec.log"
    cmd = [
        codex_bin,
        "exec",
        "--cd",
        str(ROOT),
        "--skip-git-repo-check",
        "--output-last-message",
        str(output_file),
    ]
    if args.dangerous_bypass:
        cmd.append("--dangerously-bypass-approvals-and-sandbox")
    else:
        cmd.extend(["--sandbox", "workspace-write"])
    cmd.append("-")

    try:
        with log_file.open("wb") as log_handle:
            result = subprocess.run(
                cmd,
                input=prompt_text.encode("utf-8"),
                stdout=log_handle,
                stderr=subprocess.STDOUT,
                check=False,
            )
    except OSError as exc:
        print(f"Unable to start Codex CLI: {exc}")
        print(f"Prompt file is ready at: {prompt_file}")
        return 1

    print(f"Codex exited with code {result.returncode}")
    print(f"Prompt file: {prompt_file}")
    print(f"Last message file: {output_file}")
    print(f"Exec log file: {log_file}")
    return result.returncode


def cmd_e2e(args: argparse.Namespace) -> int:
    if not args.skip_doctor:
        report = run_doctor(args.codex_bin, args.pipeline)
        print(json.dumps(report, ensure_ascii=False, indent=2))
        fatal_checks = ("upstream_config", "codex_cli")
        failed = [name for name in fatal_checks if not report["checks"][name]["ok"]]
        if failed:
            print(f"Doctor failed required checks: {', '.join(failed)}")
            return 2

    if args.run_id:
        run = load_run(args.run_id)
    else:
        if not args.goal:
            print("`--goal` is required when starting a new end-to-end run.")
            return 2
        overrides = {}
        if args.ref_paper:
            overrides["ref_paper"] = args.ref_paper
        if args.base_repo:
            overrides["base_repo"] = args.base_repo
        run = create_run(args.pipeline, args.goal, args.new_run_id, overrides)
        print(f"Initialized run: {run.run_id}")

    completed_stages = 0
    while True:
        run = load_run(run.run_id)
        if run.status == "completed" or run.current_stage is None:
            print(f"Run {run.run_id} completed.")
            return 0

        stage_name = run.current_stage
        complete_path = stage_complete_path(run, stage_name)
        blocked_path = stage_blocked_path(run, stage_name)

        if complete_path.exists():
            ok, details = validate_stage_markers(run, stage_name)
            if not ok:
                print(details)
                return 5
            print(f"Stage already complete, advancing: {stage_name}")
            cmd_advance(argparse.Namespace(run_id=run.run_id))
            completed_stages += 1
            if args.max_stages is not None and completed_stages >= args.max_stages:
                print(f"Stopped after advancing {completed_stages} stage(s).")
                return 0
            continue

        cmd_next(argparse.Namespace(run_id=run.run_id, refresh=args.refresh))
        run_code = cmd_run(
            argparse.Namespace(
                run_id=run.run_id,
                codex_bin=args.codex_bin,
                dangerous_bypass=args.dangerous_bypass,
            )
        )
        if run_code != 0:
            print(f"Stage execution exited non-zero for: {stage_name}")
            return run_code

        run = load_run(run.run_id)
        complete_path = stage_complete_path(run, stage_name)
        blocked_path = stage_blocked_path(run, stage_name)

        if complete_path.exists():
            ok, details = validate_stage_markers(run, stage_name)
            if not ok:
                print(details)
                return 5
            print(f"Stage completed: {stage_name}")
            cmd_advance(argparse.Namespace(run_id=run.run_id))
            completed_stages += 1
            if args.max_stages is not None and completed_stages >= args.max_stages:
                print(f"Stopped after completing {completed_stages} stage(s).")
                return 0
            continue

        if blocked_path.exists():
            print(f"Stage blocked: {stage_name}")
            print(f"Blocker note: {blocked_path}")
            return 3

        print(f"Stage ended without a completion or blocker marker: {stage_name}")
        return 4


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Minimal Codex-native wrapper for upstream ARIS skills.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("pipelines", help="List built-in pipeline shapes.").set_defaults(func=cmd_pipelines)
    subparsers.add_parser("skills", help="List known upstream skills.").set_defaults(func=cmd_skills)

    fetch = subparsers.add_parser("fetch", help="Fetch one upstream skill into the local cache.")
    fetch.add_argument("skill")
    fetch.add_argument("--force", action="store_true")
    fetch.set_defaults(func=cmd_fetch)

    init = subparsers.add_parser("init", help="Create a new local ARIS run.")
    init.add_argument("pipeline")
    init.add_argument("--goal", required=True)
    init.add_argument("--run-id")
    init.add_argument("--ref-paper")
    init.add_argument("--base-repo")
    init.set_defaults(func=cmd_init)

    status = subparsers.add_parser("status", help="Show local run state.")
    status.add_argument("run_id")
    status.set_defaults(func=cmd_status)

    doctor = subparsers.add_parser("doctor", help="Run local preflight checks for the Codex ARIS workflow.")
    doctor.add_argument("pipeline", nargs="?", default="research-pipeline")
    doctor.add_argument("--codex-bin", default=r"C:\Users\xliup\bin\codex.exe")
    doctor.set_defaults(func=cmd_doctor)

    nxt = subparsers.add_parser("next", help="Fetch the current stage skill and render a prompt file.")
    nxt.add_argument("run_id")
    nxt.add_argument("--refresh", action="store_true")
    nxt.set_defaults(func=cmd_next)

    advance = subparsers.add_parser("advance", help="Move the run to the next stage.")
    advance.add_argument("run_id")
    advance.set_defaults(func=cmd_advance)

    run_cmd = subparsers.add_parser("run", help="Attempt to execute the current stage with Codex CLI.")
    run_cmd.add_argument("run_id")
    run_cmd.add_argument("--codex-bin", default=r"C:\Users\xliup\bin\codex.exe")
    run_cmd.add_argument("--dangerous-bypass", action="store_true")
    run_cmd.set_defaults(func=cmd_run)

    e2e = subparsers.add_parser(
        "e2e",
        help="Initialize or resume a run and execute stages automatically until completion or block.",
    )
    e2e.add_argument("pipeline", nargs="?", default="research-pipeline")
    e2e.add_argument("--goal")
    e2e.add_argument("--run-id")
    e2e.add_argument("--new-run-id")
    e2e.add_argument("--ref-paper")
    e2e.add_argument("--base-repo")
    e2e.add_argument("--refresh", action="store_true")
    e2e.add_argument("--max-stages", type=int)
    e2e.add_argument("--codex-bin", default=r"C:\Users\xliup\bin\codex.exe")
    e2e.add_argument("--dangerous-bypass", action="store_true")
    e2e.add_argument("--skip-doctor", action="store_true")
    e2e.set_defaults(func=cmd_e2e)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
