# 2026-03-25: Third-party proof review skill

## Context

The Gleason project reached the point where internal review was no longer
enough. The next credibility step was an external-model-style review workflow.

## What worked

It helped to separate:

1. internal audit artifacts like `PROOF_AUDIT.md`
2. external-style review artifacts like `THIRD_PARTY_REVIEW.md`

That keeps the project honest about the difference between self-critique and
independent review.

## Repo improvement

A local skill was added:

- `skills/third-party-proof-review`

This gives the repo a reusable external-review pattern for future theorem or
proof projects, not just the Gleason example.
