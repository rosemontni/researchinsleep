# 2026-03-25: Tightening imported proof pieces

## Context

In the Gleason example, the remaining "imports" were no longer the whole proof.
They were narrow proof modules:

1. warmup theorems,
2. Section 7 comparison claim.

## What worked

1. Pulling the exact source pages before rewriting kept the reconstruction
   honest.
2. Replacing "imported theorem name" with a standalone local note is a strong
   way to shrink uncertainty without pretending the entire proof is new.
3. After shrinking an import, update the project status files immediately so
   the repo's claim level stays aligned with reality.

## General insight

For difficult math exposition projects, progress often comes from changing the
unit of work:

- not "prove the theorem",
- but "eliminate one imported black box at a time."
