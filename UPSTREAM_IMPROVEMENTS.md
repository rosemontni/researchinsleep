# Local Improvements Over Upstream ARIS

This document is the quickest way to see what this repo adds on top of the upstream ARIS workflow.

Upstream source of truth:
- [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep)

This repo does not fork the upstream skills. It keeps those skills upstream and adds a thin local Codex execution layer around them.

## At A Glance

| Area | Upstream ARIS | Local Improvement In This Repo |
| --- | --- | --- |
| Top-level execution | Conceptual end-to-end pipeline | Real local `e2e` runner in [aris_codex.py](C:\Users\xliup\OneDrive\Documents\codex\researchinsleep\aris_codex.py) |
| Stage completion | Mostly convention-driven | Validated completion and blocker markers |
| Environment checks | Assumed implicitly | `doctor` preflight command |
| Codex adaptation | Not the primary target | Codex-native wrapper with standalone CLI support |
| Project separation | Workflow and examples can blur together | Clear split between wrapper, run state, and example project |
| End-to-end semantics | “One top-level command” | Explicit staged artifact-driven orchestration |

## Why This Document Exists

Upstream ARIS already has the right overall idea:

- one top-level research pipeline
- multiple staged skills underneath
- durable artifacts on disk
- review before paper writing

What it does not fully provide upstream is a concrete local execution contract for Codex. This repo fills that gap without copying the upstream skills into the workspace.

## Improvements Over Upstream

### 1. First-class local end-to-end runner

Upstream presents `/research-pipeline` as the top-level workflow, but the actual orchestration is still implicit inside staged prompts.

Locally, this repo adds a true runner in [aris_codex.py](C:\Users\xliup\OneDrive\Documents\codex\researchinsleep\aris_codex.py):

- `python .\aris_codex.py e2e ...`

That runner:

- initializes or resumes a run
- renders the current upstream skill into a local prompt
- executes it through Codex CLI
- auto-advances on valid completion markers
- stops on blocker files

This keeps the user-facing experience end-to-end while preserving the safer staged artifact model underneath.

### 2. Explicit stage completion contract

Upstream relies mostly on convention for stage completion. This repo standardizes the local contract:

- `<stage>.complete.json`
- `<stage>.blocked.md`

Completion markers are validated before the runner auto-advances. A completion marker must contain:

- `stage`
- `completed_at`
- `summary`
- `next_stage`

That makes resume, automation, and auditing much safer.

### 3. Preflight doctor checks

Upstream assumes a lot of environment context is already present. This repo adds a `doctor` command that checks the minimum local setup before an end-to-end run:

- upstream pipeline config loaded
- Codex CLI reachable
- local project signals present
- paper toolchain availability

Command:

```powershell
python .\aris_codex.py doctor
```

The `e2e` runner now calls this automatically unless you opt out with `--skip-doctor`.

### 4. Clear separation between workflow and example project

This repo separates:

- workflow infrastructure
- run state
- example research project

That split matters because ARIS is a methodology, not a single research codebase.

In this workspace:

- [aris_codex.py](C:\Users\xliup\OneDrive\Documents\codex\researchinsleep\aris_codex.py) is the workflow wrapper
- `.aris/` and `.aris-cache/` hold run state and cached upstream skills
- [adrd](C:\Users\xliup\OneDrive\Documents\codex\researchinsleep\adrd) is just one example project used to exercise the workflow

### 5. More honest end-to-end framing

The local implementation is explicit about what “end-to-end” means:

- one user command at the top
- staged execution below
- artifacts between stages
- resumable progress

It is not a claim that a single monolithic prompt produces a complete paper in one pass.

## What Is Implemented Locally Right Now

These improvements are already implemented in this repo:

- `e2e` command for one-command runs
- `doctor` command for preflight checks
- validated completion markers before auto-advance
- blocker-aware stop behavior
- upstream skill fetching without cloning the upstream repo
- Codex CLI targeting via `--codex-bin`

## What Still Has Room To Improve

These are good future candidates if we want to keep pushing:

- required-vs-warning doctor checks per stage
- richer blocker schemas, not just freeform markdown
- stage-specific environment checks
- stronger claim-safety gates before paper-writing
- optional benchmark-quality gates for prototype vs submission-ready modes
