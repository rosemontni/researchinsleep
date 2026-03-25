# Paper Plan

**Working title:** Budgeted Selective Dependency Routing for Discrete Diffusion Language Models  
**Subtitle:** A Synthetic Feasibility Study  
**Venue:** ICLR 2026  
**Page target:** 7-8 pages main text, references unlimited

## One-Sentence Story

The factorization gap in diffusion language models is uneven across tokens, and a budgeted controller that selectively applies richer local dependency handling can beat fully factorized decoding on a synthetic scaffold, although the current prototype does not yet outperform the best simpler budget-matched surrogate.

## Claims-Evidence Matrix

| Claim | Evidence | Strength | Paper usage |
|---|---|---|---|
| Selective expensive routing improves over fully factorized decoding. | `factorized_logging` vs `three_mode_budget10` and `three_mode_span4` | Strong in synthetic scope | Main claim |
| There is a compute-quality frontier rather than monotone free gains. | `three_mode_budget05`, `three_mode_budget10`, `three_mode_span4` | Strong | Main claim |
| ADRD helps on longer dependency-heavy contexts. | `long_context_factorized` vs `long_context_span4` | Strong in synthetic scope | Main claim |
| The router meaningfully mixes expensive modes under relaxed budget. | `three_mode_span4.json` mode token counts | Moderate | Supporting claim |
| Full three-mode ADRD beats all fixed-policy alternatives at matched budget. | Contradicted by `budgeted_coupled_span4` | Unsupported | Exclude as claim |

## Section Plan

### 1. Introduction

- Motivate the factorization gap in diffusion decoding.
- Explain why a global dependency choice is too coarse.
- State the synthetic-scope thesis and the negative result.

### 2. Background And Related Work

- Discrete diffusion language modeling.
- Coupled output modeling and factorization-barrier work.
- Semi-autoregressive, remasking, and hybrid AR/diffusion approaches.
- Position ADRD as selective budget allocation rather than a new global output family.

### 3. Adaptive Dependency Routing Diffusion

- Define the three modes.
- Describe the dependency estimator, router, and budget controller.
- Clarify that the local implementation uses heuristic routing on a synthetic task.

### 4. Synthetic Evaluation Protocol

- Describe copy/progression dependency groups.
- Report dataset sizes, sequence lengths, and budgets.
- Define metrics and the matched-budget comparison design.

### 5. Results

- Show frontier from factorized to relaxed-budget ADRD.
- Compare against same-budget micro-only, coupled-only, and random routing.
- Show long-context stress test.
- Interpret the negative result: coupled-local explains most current gains.

### 6. Limitations And Next Steps

- Synthetic scaffold only.
- No real dLLM backbone.
- Heuristic rather than learned routing.
- No direct CoDD implementation or self-correction baseline in this repo.

### 7. Conclusion

- Restate what is supported and what is not.
- Frame the paper as a controlled feasibility study for selective dependency allocation.

## Figure Plan

| Item | Type | Status | Source |
|---|---|---|---|
| Fig. 1 ADRD overview | schematic | auto-generated locally | `figures/scripts/generate_figures.py` |
| Fig. 2 Budget frontier | plot | auto-generated | `artifacts/auto-review-loop/review_suite.csv` |
| Fig. 3 Same-budget span-4 comparison | plot | auto-generated | `artifacts/auto-review-loop/review_suite.csv` |
| Fig. 4 Long-context stress test | plot | auto-generated | `artifacts/auto-review-loop/review_suite.csv` |
| Table 1 Main synthetic results | LaTeX table | auto-generated | `artifacts/experiment-bridge/suite_summary.csv` |
| Table 2 Mode usage at relaxed budget | LaTeX table | auto-generated | `artifacts/auto-review-loop/three_mode_span4.json` |

Manual architecture artwork was replaced with a direct Codex-generated schematic because no external design workflow is available in this workspace.

## Citation Plan

- Austin et al. for discrete diffusion foundations.
- Strudel et al. for text diffusion.
- Li et al. for the factorization barrier / CoDD.
- Liu et al. and Wu et al. for efficient diffusion decoding.
- Wang et al. and Zhang et al. for remasking / self-correction.
- Fathi et al. and Sahoo et al. for AR/diffusion hybridization.

## Risk Controls

- Use "synthetic feasibility study" in the title, abstract, and conclusion.
- State clearly that the best same-budget surrogate remains competitive or slightly stronger.
- Avoid language implying a trained router on a real dLLM backbone.
- Include a limitations section before conclusion.
