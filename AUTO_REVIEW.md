# AUTO_REVIEW

Date: 2026-03-24
Reviewer substitution: upstream GPT-5.4 Codex MCP review was unavailable in this local wrapper run, so the review loop used a direct Codex self-review with the same rubric and full written raw responses.

## Round 1 (2026-03-24T22:13:32-04:00)

### Assessment (Summary)

- Score: 4/10
- Verdict: not ready
- Key criticisms:
  - The evidence base was too thin: only the factorized baseline and two ADRD variants were reported.
  - The full ADRD run had mode-collapse risk because `micro-sequential` was not being used in the best three-mode configuration.
  - The metrics were not strong enough for a review loop: exact match was always zero, and there was no dependency-group recovery metric.
  - The narrative overreached beyond the data. The workspace only supports a synthetic scaffold, not a real dLLM benchmark.

### Reviewer Raw Response

<details>
<summary>Click to expand full reviewer response</summary>

Round 1 review. Score: 4/10. Verdict: not ready.

This is a plausible synthetic feasibility scaffold, but it is not yet a convincing research result even at the level of an internal submission gate. The current document overclaims relative to the evidence.

Remaining critical weaknesses, ranked:

1. Missing ablations and matched-budget controls. You show factorized, two-mode ADRD, and one three-mode ADRD setting, but you do not show whether the gain comes from the router, from simply spending more budget, or from one expensive mode dominating. Minimum fix: add random-routing and single-mode surrogates under the same budget family, plus a budget sweep.

2. The best three-mode run appears to collapse to coupled-local usage, which undermines the central "adaptive routing among three modes" story. Minimum fix: change the router so `micro-sequential` activates on at least one credible dependency regime, then report actual mode usage.

3. The diagnostics are too weak. Exact match is always zero and there is no group-level recovery metric for the synthetic dependency structure. Minimum fix: add dependency-group accuracy and use it in the review tables.

4. The claim scope is wrong. This is a synthetic pilot scaffold, not evidence about discrete diffusion language models at paper level. Minimum fix: rewrite the narrative so the validated claim is limited to synthetic feasibility unless a real backbone is added.

READY for submission? No.

</details>

### Actions Taken

- Added `dependency_group_accuracy` and per-kind group recovery metrics to the evaluation payload.
- Extended the router with fixed-priority and random budgeted policies for review-time ablations.
- Revised the heuristic router so progression-like groups and short uncertain spans can trigger `micro-sequential`, avoiding complete three-mode collapse.
- Added review-oriented experiment presets:
  - strict 5% and 10% budget sweeps
  - same-budget micro-only, coupled-only, and random surrogates
  - longer-context stress runs
- Updated the experiment results and tracker to narrow the claim scope to a synthetic pilot.

### Results

- Verification: `python -m unittest discover -s .\tests -p "test_*.py"` -> `OK` (`7` tests)
- Synthetic budget sweep:
  - `three_mode_budget05`: token `0.6222`, dependency `0.3446`, group `0.0322`, expensive fraction `0.0000`
  - `three_mode_budget10`: token `0.6413`, dependency `0.4363`, group `0.2154`, expensive fraction `0.0293`
  - `three_mode_span4`: token `0.6825`, dependency `0.6245`, group `0.5016`, expensive fraction `0.1089`
- Same-budget span-4 surrogates:
  - `budgeted_micro_span4`: token `0.6775`, dependency `0.6454`
  - `budgeted_coupled_span4`: token `0.6871`, dependency `0.6365`
  - `random_span4`: token `0.6795`, dependency `0.6534`
  - `three_mode_span4`: token `0.6825`, dependency `0.6245`
- Long-context stress:
  - `long_context_factorized`: token `0.6268`, dependency `0.3720`
  - `long_context_span4`: token `0.6526`, dependency `0.5015`

### Status

- Continuing to round 2

## Round 2 (2026-03-24T22:13:32-04:00)

### Assessment (Summary)

- Score: 6/10
- Verdict: almost
- Key criticisms:
  - There is still no real dLLM backbone or external benchmark, so this is not a top-venue-ready paper result.
  - Same-budget synthetic surrogates show that most of the gain can be explained by `coupled-local`; the full three-mode policy is not yet dominant.
  - The long-context stress case still collapses to `coupled-local`, so the three-mode routing claim remains narrow.

### Reviewer Raw Response

<details>
<summary>Click to expand full reviewer response</summary>

Round 2 review. Score: 6/10. Verdict: almost.

The work is now coherent as a synthetic pilot study. The review loop fixed the most obvious methodological gaps: there are budget sweeps, same-budget surrogates, stronger diagnostics, and the best ADRD run no longer hides total mode collapse. The documentation is also materially more honest.

What is now validated:

- Selective non-factorized routing improves over the factorized baseline on the synthetic dependency task.
- The compute-quality frontier is visible: the gain disappears at a very tight 5% budget and rises once the budget is relaxed enough for coupled-local spans.
- Longer synthetic contexts preserve the directional advantage over the factorized baseline.

What is still not validated:

- The central "three-mode adaptive router is the winning formulation" claim. On the same relaxed synthetic budget, the coupled-only surrogate is slightly better on token accuracy, and the random router is competitive on dependency accuracy.
- Any claim about real discrete diffusion language models. The workspace still contains only a synthetic harness.

Minimum fix from here is not more local code churn. It is claim discipline:

1. Write this as a synthetic feasibility / negative-result pilot, not as a solved factorization-gap paper.
2. State explicitly that coupled-local appears to explain most of the current gain.
3. Carry the remaining blockers into the paper-writing stage so the paper can frame future real-model experiments honestly.

READY for submission? Almost, if the target is an internal note or scoped synthetic pilot paper. Not ready for a top-tier empirical ML submission.

</details>

### Actions Taken

- Rewrote the experiment notes and tracker to center the synthetic-scope findings and the negative same-budget surrogate result.
- Preserved the strongest positive result and the main blocker in the run-local artifacts for the paper-writing stage.

### Results

- Final score progression: `4/10 -> 6/10`
- Validated positive claims:
  - factorized baseline -> relaxed ADRD span-4: token `0.6222 -> 0.6825`
  - factorized baseline -> relaxed ADRD span-4: dependency-group accuracy `0.0418 -> 0.5016`
  - long-context factorized -> long-context ADRD span-4: dependency `0.3720 -> 0.5015`
- Important negative result:
  - same-budget `budgeted_coupled_span4` slightly beats full ADRD on token accuracy (`0.6871` vs `0.6825`)

### Status

- Stopping: positive threshold met for a synthetic-pilot scope (`6/10`, verdict `almost`)

## Final Summary

- Score progression: `4/10 -> 6/10`
- Final scope: synthetic feasibility study, not submission-ready empirical dLLM paper
- Main validated conclusion: selective budgeted routing clearly beats the factorized baseline on this synthetic dependency task, but the present evidence does not show that the full three-mode ADRD policy is better than the best same-budget surrogate.
- Remaining blockers:
  - real dLLM backbone and GPU benchmark
  - external remask / self-correction baseline
  - external global coupling baseline
  - stronger evidence that three-mode routing beats coupled-only under matched compute
- Recommendation: proceed to paper-writing only if the paper is framed as a synthetic pilot with explicit limitations and negative-result reporting.

## Method Description

Adaptive Dependency Routing Diffusion (ADRD) is a synthetic discrete-decoding scaffold that assigns each unresolved dependency group to one of three decoding modes during iterative denoising: cheap fully factorized decoding, short-span coupled-local decoding, or micro-sequential decoding over a tiny ordered subset. A heuristic dependency estimator scores each unresolved group from synthetic state features such as group type, unresolved span ratio, and denoising progress, and a router chooses the cheapest allowed mode subject to a fixed expensive-token budget.

The current local implementation operates on a synthetic sequence task with copy-style and progression-style dependency groups. During decoding, the factorized mode predicts tokens independently, the coupled-local mode attempts exact short-span reconstruction with a higher-probability structured fallback, and the micro-sequential mode predicts an anchor token before resolving the rest of the span conditionally. The evaluation pipeline reports token accuracy, dependency-token accuracy, dependency-group recovery, actual expensive-token usage, and mode counts so downstream paper-writing can describe both the positive gains and the remaining mode-selection limitations.
