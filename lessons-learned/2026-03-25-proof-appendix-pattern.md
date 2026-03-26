# 2026-03-25: Proof appendix pattern

## Context

Two remaining proof gaps in the Gleason project had different shapes:

1. endgame geometry,
2. Section 6 topology bookkeeping.

## What worked

They should not be treated the same way.

1. For a geometric contradiction, integrate the case split directly into the
   main proof note.
2. For compactness / closure bookkeeping, create a short appendix so the main
   proof stays readable while the logic still becomes explicit.

## General lesson

In math-exposition projects, a good rule is:

- if the gap changes the conceptual flow, fix it inside the main proof,
- if the gap is standard but necessary bookkeeping, isolate it in an appendix.
