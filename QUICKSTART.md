# Quickstart

This repo is a lightweight Codex wrapper around upstream ARIS skills.

The core idea is:

- keep the workflow logic upstream in ARIS `SKILL.md` files
- keep local state and outputs here
- let Codex execute each stage against this workspace

You do **not** clone the upstream ARIS repo into this workspace. Instead, this project fetches the current upstream skills on demand and turns them into local stage prompts.

## Mental Model

Think of the system as three layers:

1. **Upstream ARIS skills**
   - Stored on GitHub.
   - Define the methodology for each stage.
   - Fetched and cached under `.aris-cache/`.

2. **Local run state**
   - Stored under `.aris/runs/<run-id>/`.
   - Tracks which stage you are in.
   - Stores prompts, notes, reports, experiment artifacts, and paper outputs.

3. **Local project code**
   - The codebase that ARIS operates on.
   - In this repo, that includes the synthetic ADRD scaffold under `adrd/`.

## What The Workflow Does

ARIS is a staged research loop:

1. **Idea discovery**
   - Find and refine a research direction.
   - Write durable proposal artifacts.

2. **Experiment bridge**
   - Turn the proposal into code and first experiments.
   - In this repo, that means the synthetic ADRD scaffold.

3. **Auto review loop**
   - Critique the evidence.
   - Add ablations, tighten claims, rerun checks.

4. **Paper writing**
   - Turn the reviewed artifacts into a paper package with LaTeX and PDFs.

The important workflow rule is: each stage writes artifacts to disk, so progress survives interruptions.

## One-Minute Start

List available pipelines:

```powershell
python .\aris_codex.py pipelines
python .\aris_codex.py skills
```

Create a run:

```powershell
python .\aris_codex.py init research-pipeline --goal "factorized gap in discrete diffusion LMs"
```

Render the current stage prompt:

```powershell
python .\aris_codex.py next <run-id>
```

Run the stage through the standalone Codex CLI:

```powershell
python .\aris_codex.py run <run-id> --dangerous-bypass
```

Advance after the stage completes:

```powershell
python .\aris_codex.py advance <run-id>
```

Inspect run state any time:

```powershell
python .\aris_codex.py status <run-id>
```

## Why `--dangerous-bypass` Exists

On this Windows setup, Codex CLI sometimes fails to persist files when using its normal sandbox. The bypass option was added as a practical workaround so long ARIS stages can actually write their artifacts.

Use it only in a workspace you trust.

## Typical Folder Layout

After a run starts, the important folders are:

- `.aris-cache/skills/`
  - cached upstream skill text
- `.aris/runs/<run-id>/prompts/`
  - rendered stage prompts sent to Codex
- `.aris/runs/<run-id>/notes/`
  - per-stage reports, completion markers, and exec logs
- `.aris/runs/<run-id>/refine-logs/`
  - durable research artifacts like proposals and experiment plans
- `.aris/runs/<run-id>/artifacts/`
  - raw experiment outputs and review outputs
- `paper/`
  - generated paper source and PDFs

## What This Repo’s Local Code Does

The local `adrd/` package is a synthetic research scaffold for ADRD.

It is useful because `experiment-bridge` needs a codebase to operate on. Without one, ARIS can only plan. With `adrd/`, the workflow can actually:

- implement the method
- run experiments
- compare against baselines
- revise claims
- write a paper from real local artifacts

## Useful Commands

Run the synthetic experiment harness:

```powershell
python -m adrd.experiment --strategy adrd
python -m adrd.experiment --preset review_suite
```

Run tests:

```powershell
python -m unittest discover -s .\tests -p "test_*.py"
```

Open the generated paper:

- PDF: [paper/main.pdf](C:\Users\xliup\OneDrive\Documents\codex\researchinsleep\paper\main.pdf)
- LaTeX: [paper/main.tex](C:\Users\xliup\OneDrive\Documents\codex\researchinsleep\paper\main.tex)

## Basic Workflow Ideas

These are the main ideas behind how this repo works:

- **Upstream-first workflow**
  - ARIS methodology stays upstream and current.

- **Thin local wrapper**
  - Local code handles orchestration, caching, and durable state.

- **Artifact-driven execution**
  - Each stage writes files, not just chat output.

- **Review before paper**
  - Claims are supposed to be narrowed by evidence before writing.

- **Prototype honesty**
  - This repo currently supports a synthetic ADRD prototype, not a real dLLM benchmark claim.

## Recommended First Read

If you want to understand the whole setup quickly, read these in order:

1. [README.md](C:\Users\xliup\OneDrive\Documents\codex\researchinsleep\README.md)
2. [QUICKSTART.md](C:\Users\xliup\OneDrive\Documents\codex\researchinsleep\QUICKSTART.md)
3. [ITERATION_REPORT.md](C:\Users\xliup\OneDrive\Documents\codex\researchinsleep\ITERATION_REPORT.md)
4. [AUTO_REVIEW.md](C:\Users\xliup\OneDrive\Documents\codex\researchinsleep\AUTO_REVIEW.md)

