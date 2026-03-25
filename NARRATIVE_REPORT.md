# Narrative Report

**Project:** factorized gap in discrete diffusion LMs  
**Date:** 2026-03-24  
**Target venue:** ICLR 2026  
**Current evidence scope:** synthetic feasibility study

## Executive Position

The original claim, "break the factorization barrier in discrete diffusion language models," is no longer a clean framing because CoDD already makes the strongest recent global-coupling argument. The defensible paper in this workspace is narrower:

**Budgeted selective dependency handling can outperform fully factorized decoding on a controlled synthetic diffusion scaffold, but the present evidence does not yet show that full adaptive three-mode routing beats the best simpler budget-matched surrogate.**

That framing is strong enough for a workshop-style or pilot paper and honest enough for a main-conference draft section that motivates a larger empirical follow-up.

## Problem

Diffusion language models promise parallel decoding, but quality degrades when simultaneously predicted tokens interact strongly. Existing recent work mostly chooses one dependency treatment globally:

- keep outputs factorized and accept incoherence,
- use a stronger coupled output family everywhere,
- or move toward sequential or semi-autoregressive decoding.

The open question explored here is whether the factorization gap is sparse enough that richer dependency handling only needs to be activated for a minority of regions.

## Proposed Method

Adaptive Dependency Routing Diffusion (ADRD) allocates each currently masked region to one of three decoding modes:

1. `factorized` for cheap independent prediction,
2. `coupled-local` for short strongly linked spans,
3. `micro-sequential` for small high-risk knots that benefit from local ordering.

The local scaffold implements:

- a synthetic dependency estimator that scores unresolved copy/progression groups,
- a budget controller that caps non-factorized usage,
- a heuristic mode router,
- and three decoding operators with different accuracy/compute tradeoffs.

This implementation is a prototype controller on a synthetic task, not a trained diffusion LM on real text.

## Experimental Scaffold

The repo contains a synthetic benchmark in `adrd.synthetic` and `adrd.core`.

- Each sequence contains random tokens plus optional dependency groups.
- Dependency groups are either `copy` spans or arithmetic-like `progression` spans.
- The evaluator reports token accuracy, dependency accuracy, dependency-group accuracy, non-dependency accuracy, and expensive-token fraction.
- The main evaluation uses 192 sequences of length 24 with four diffusion steps.
- A stress test uses length 40 sequences with denser dependencies.

## Main Evidence

### Supported Claims

1. **Selective non-factorized routing improves over the factorized baseline.**
   - `factorized_logging`: token accuracy `0.6222`, dependency accuracy `0.3446`, dependency-group accuracy `0.0418`.
   - `three_mode_budget10`: token accuracy `0.6413`, dependency accuracy `0.4363`, dependency-group accuracy `0.2154`.

2. **The compute-quality frontier is visible under explicit budgets.**
   - At a 5% budget, routing collapses to factorized behavior.
   - At about `10.89%` actual expensive-token usage (`three_mode_span4`), metrics improve sharply.

3. **Selective routing helps on longer, denser synthetic dependency spans.**
   - `long_context_factorized`: token accuracy `0.6268`, dependency accuracy `0.3720`.
   - `long_context_span4`: token accuracy `0.6526`, dependency accuracy `0.5015`.

4. **The current scaffold demonstrates mixed mode usage at relaxed budget.**
   - `three_mode_span4` uses `407` coupled-local tokens and `95` micro-sequential tokens.

### Negative Or Ambiguous Findings

1. **Full ADRD is not yet strictly superior to all matched-budget surrogates.**
   - Under the relaxed span-4 budget, `budgeted_coupled_span4` slightly exceeds `three_mode_span4` on token accuracy (`0.6871` vs `0.6825`).

2. **The strongest current synthetic gains are driven mostly by coupled-local routing.**
   - Long-context ADRD uses only coupled-local expensive routing.

3. **The current router is heuristic, not learned.**
   - This makes the result a feasibility study about budgeted dependency allocation, not a final architecture claim about learned routing in real dLLMs.

## Paper-Safe Thesis

The paper should argue:

- the factorization gap is heterogeneous rather than uniform,
- budgeted selective dependency handling is viable,
- and a three-mode controller is a reasonable design direction,

while explicitly stating:

- current evidence is synthetic,
- same-budget coupled-local-only routing remains a strong surrogate,
- and a real dLLM validation is future work.

## Figure Inventory

### Figure 1: ADRD Overview

- Purpose: show the per-step routing pipeline from dependency scoring to mode allocation.
- Source: locally generated schematic.

### Figure 2: Budget Frontier

- Purpose: show token/dependency metrics as expensive-token usage increases.
- Source: `artifacts/auto-review-loop/review_suite.csv`.

### Figure 3: Same-Budget Span-4 Comparison

- Purpose: compare factorized, micro-only, coupled-only, random, and ADRD routing under the same relaxed budget.
- Source: `artifacts/auto-review-loop/review_suite.csv`.

### Figure 4: Long-Context Stress Test

- Purpose: show ADRD gains on length-40 synthetic sequences.
- Source: `artifacts/auto-review-loop/review_suite.csv`.

### Table 1: Main Synthetic Results

- Purpose: summarize the factorized baseline, strict-budget ADRD, and relaxed-budget ADRD.
- Source: `artifacts/experiment-bridge/suite_summary.csv`.

### Table 2: Mode Usage Under Relaxed Budget

- Purpose: show that the relaxed-budget ADRD run uses both coupled-local and micro-sequential routing.
- Source: `artifacts/auto-review-loop/three_mode_span4.json`.

## Citation Scaffold

The draft should cite:

- discrete diffusion foundations,
- recent work on the factorization barrier and global coupling,
- semi-autoregressive or KV-cache-compatible diffusion decoding,
- remasking/self-correction lines,
- and hybrid AR/diffusion work.

Priority references:

- Austin et al., *Structured Denoising Diffusion Models in Discrete State-Spaces*
- Strudel et al., *Self-conditioned Embedding Diffusion for Text Generation*
- Li et al., *Breaking the Factorization Barrier in Diffusion Language Models*
- Liu et al., *Sequential Diffusion Language Models*
- Wu et al., *Fast-dLLM v2: Efficient Block-Diffusion LLM*
- Wang et al., *Remasking Discrete Diffusion Models with Inference-Time Scaling*
- Zhang et al., *Denoising is not the End: Discrete Diffusion Language Models with Self-Correction*
- Fathi et al., *Unifying Autoregressive And Diffusion-Based Sequence Generation*
- Sahoo et al., *Esoteric Language Models: Bridging Autoregressive and Masked Diffusion LLMs*

## Writing Guidance

- Do not claim a real-model breakthrough.
- Do not write as if ADRD already beats CoDD or production dLLMs.
- Treat this as a synthetic pilot that isolates the controller hypothesis.
- Emphasize budget matching, failure cases, and the distinction between feasibility and final validation.
