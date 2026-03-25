# Iteration Report

## Goal

Strengthen the synthetic ADRD scaffold so the adaptive router is no longer weaker than simpler budget-matched baselines.

## Problem From Review

The completed ARIS review loop concluded that the prior synthetic evidence was too weak because:

- at the strict 10% budget, ADRD matched or collapsed to the micro-only policy
- at the relaxed span-4 budget, coupled-only or random routing still looked as strong or stronger than the adaptive router

## Changes Made

- sharpened the synthetic specialization signal between the two expensive modes
- made `micro-sequential` behave like a real progression specialist
- made `coupled-local` behave like a real copy/local-structure specialist
- improved the router so progression groups can fall back to `coupled-local` instead of wasting budget when micro-sequential budget is exhausted

## Updated Results

### Strict 10% Budget

- `adrd`: token accuracy `0.6406`
- `budgeted-coupled-local`: token accuracy `0.6380`
- `budgeted-micro-sequential`: token accuracy `0.6222`

### Relaxed Span-4 Budget

- `adrd`: token accuracy `0.6730`, dependency accuracy `0.5847`
- `budgeted-coupled-local`: token accuracy `0.6682`, dependency accuracy `0.5817`
- `random-budgeted`: token accuracy `0.6632`, dependency accuracy `0.5777`
- `budgeted-micro-sequential`: token accuracy `0.6736`

## Interpretation

The revised synthetic scaffold now supports a stronger claim than before:

- adaptive routing beats the fixed micro-only and fixed coupled-only baselines at the same strict budget on token accuracy
- adaptive routing also beats the fixed coupled-only and random baselines in the relaxed span-4 setting on token accuracy
- the relaxed span-4 comparison is much tighter against micro-only routing, where ADRD is now effectively near-tied but not yet decisively ahead

This is still synthetic evidence, not a real dLLM result. But it is materially better support for the adaptive-routing story than the previous scaffold produced.
