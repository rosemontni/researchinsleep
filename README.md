# ARIS Codex Skeleton

This workspace is a lightweight Codex-native wrapper around the upstream ARIS repository:

- Upstream repo: [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep)
- Goal: use ARIS workflows from Codex without cloning the full upstream repo into this workspace

## What This Skeleton Does

- Fetches selected upstream `SKILL.md` files directly from GitHub at runtime
- Caches them locally under `.aris-cache/`
- Creates persistent local run state under `.aris/runs/<run-id>/`
- Renders a Codex-friendly stage prompt that inlines the upstream skill text
- Tracks which stage of the ARIS pipeline you are in

## What It Does Not Do

- It does not vendor or fork the ARIS skill pack into this repo
- It does not try to preserve Claude-specific slash-command semantics
- It does not depend on Codex custom skills being installed globally

Instead, it treats upstream ARIS skills as the source of truth and wraps them in a local orchestration layer.

## Why This Shape

ARIS is actively changing upstream. If we copied the skills into this workspace, they would drift quickly. This wrapper keeps a very small local surface area and refreshes the authoritative skill content from upstream when needed.

Start with [QUICKSTART.md](C:\Users\xliup\OneDrive\Documents\codex\researchinsleep\QUICKSTART.md) if you want the shortest explanation of how the workflow fits together.

## Quick Start

Create a run:

```powershell
python .\aris_codex.py init research-pipeline --goal "factorized gap in discrete diffusion LMs"
```

See available workflows:

```powershell
python .\aris_codex.py pipelines
python .\aris_codex.py skills
```

Render the current stage prompt for a run:

```powershell
python .\aris_codex.py next <run-id>
```

This writes a prompt file under:

```text
.aris/runs/<run-id>/prompts/
```

Run the current stage through a standalone Codex CLI binary:

```powershell
python .\aris_codex.py run <run-id> --codex-bin "C:\Users\xliup\bin\codex.exe"
```

The wrapper passes `--cd` with this workspace root, `--skip-git-repo-check`, and `--sandbox workspace-write`, so it can run in a plain folder and still create stage artifacts without requiring you to initialize a Git repo first.

If Codex on Windows hits its internal sandbox bug while trying to write files, you can opt into a less restricted workaround:

```powershell
python .\aris_codex.py run <run-id> --dangerous-bypass
```

Use that only when you trust the prompt and workspace, because it tells Codex CLI to bypass its own approvals and sandbox.

Advance to the next stage after a stage is complete:

```powershell
python .\aris_codex.py advance <run-id>
```

Inspect run state:

```powershell
python .\aris_codex.py status <run-id>
```

## Recommended Usage Pattern In Codex

1. Initialize a run with `init`.
2. Use `next` to fetch the current upstream skill and render a local prompt file.
3. Open that prompt file in Codex and execute the stage.
4. When the stage is done, use `advance` to move the run forward.
5. Repeat until the pipeline finishes.

## Notes

- The wrapper keeps upstream skill URLs in `config/upstream_skills.json`.
- Pipelines are defined locally so you can keep your preferred loop shape even if upstream adds more skills.
- The `run` subcommand can target an explicit standalone CLI path, which is recommended on Windows to avoid the packaged app alias under `WindowsApps`.

## Scratch ADRD Scaffold

This workspace now also contains a minimal from-scratch ADRD research scaffold under `adrd/`.

It is intentionally small and synthetic:

- It does not claim to be a production discrete diffusion LM implementation.
- It gives `experiment-bridge` a real codebase to operate on.
- It includes the ADRD components from the proposal: dependency estimator, router, decoding modes, and budget controller.

Run the synthetic experiment harness:

```powershell
python -m adrd.experiment --strategy adrd
python -m adrd.experiment --strategy factorized
python -m adrd.experiment --preset review_suite
```

Run the tests:

```powershell
python -m unittest discover -s .\tests -p "test_*.py"
```

See [ITERATION_REPORT.md](C:\Users\xliup\OneDrive\Documents\codex\researchinsleep\ITERATION_REPORT.md) for the current post-review router redesign results.
