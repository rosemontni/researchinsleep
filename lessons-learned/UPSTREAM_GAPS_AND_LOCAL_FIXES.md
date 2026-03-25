# Upstream Gaps And Local Fixes

## 2026-03-25 - End-to-end needed a real local runner

### Upstream Gap

Upstream ARIS exposes a top-level pipeline concept, but local Codex execution still needed an explicit runner.

### Local Fix

Add `e2e` to `aris_codex.py` so the workflow can initialize, run, validate, and advance stages automatically.

### Durable Insight

For agent workflows, “end-to-end” works best as one command on top of a staged artifact system, not as one giant reasoning pass.

## 2026-03-25 - Stage completion needed a stronger contract

### Upstream Gap

Completion was convention-based, which made automation brittle.

### Local Fix

Validate completion markers before `e2e` auto-advances.

### Durable Insight

Artifact-driven workflows should promote completion formats to first-class contracts, not just habits.

## 2026-03-25 - Environment assumptions needed a doctor step

### Upstream Gap

Important local assumptions were discovered only after the run had already started.

### Local Fix

Add `doctor` checks for upstream config, Codex CLI, local codebase signals, and paper toolchain readiness.

### Durable Insight

Preflight checks are part of the workflow, not a convenience feature.

## 2026-03-25 - Local repo skills should be able to extend the upstream pipeline

### Upstream Gap

Useful follow-on stages like journal targeting did not belong upstream, but the end-to-end runner originally only handled upstream-cached skills.

### Local Fix

Teach `aris_codex.py` to resolve both upstream skills and local repo skills, then add `journal-shopping` after `paper-writing` in the default pipeline.

### Durable Insight

The wrapper is strongest when upstream remains the methodological core while local repo skills add project-specific final-mile stages.
