# 2026-03-25: Endgame intersection lemma

## Context

The remaining high-risk point in the Gleason proof reconstruction was a phrase
like "too many zero constraints force a contradiction."

## What worked

Turning that phrase into its own standalone lemma made the proof better:

1. list the exact great circles,
2. state their shared antipodal pairs,
3. prove when intersection pairs must be distinct,
4. then count zeros.

## General lesson

When a proof relies on "too many intersections" or "too many zeros," the right
next move is often:

- stop,
- create an explicit intersection lemma,
- and force every possible coincidence to be handled by a case split.
