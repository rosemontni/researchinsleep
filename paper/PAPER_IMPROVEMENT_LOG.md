# Paper Improvement Log

This file records the local Codex substitute for the upstream auto-paper-improvement loop.

## Round 0

- Initial anonymous ICLR-style draft generated from `NARRATIVE_REPORT.md`, `PAPER_PLAN.md`, `CLAIMS_FROM_RESULTS.md`, and `EXPERIMENT_RESULTS.md`.
- Scope set explicitly to a synthetic feasibility study.
- Output saved as `paper/main_round0_original.pdf`.
- Local score: `7.1/10`.
- Main issues:
  - needed a sharper explanation that the strongest claim is feasibility, not adaptive dominance;
  - needed clearer matched-budget framing;
  - needed a cleaner distinction between the positive result and the negative same-budget result.

## Round 1

- Revised introduction, setup, and results discussion after the first successful compile.
- Clarified that the partially negative result is central to the paper's contribution.
- Made the same-budget comparison explicitly about allocation policy rather than raw compute.
- Added stronger wording that a fixed coupled-only surrogate slightly outperforms full ADRD on token accuracy.
- Output saved as `paper/main_round1.pdf`.
- Local score: `7.8/10`.

## Round 2

- Final polish pass after the round-1 compile.
- Cleaned the budgeted-router notation to remove a layout issue.
- Removed a nonessential monospace reference to keep the draft more portable under the local TeX engine.
- Recompiled the final paper and saved `paper/main_round2.pdf`.
- Final local score: `8.0/10`.
- Residual issues:
  - evidence remains synthetic only;
  - bibliography metadata for several 2025--2026 papers was assembled manually from primary-source paper pages and may need final camera-ready normalization;
  - Tectonic emits a non-blocking internal rerun warning even though the PDF compiles successfully.
