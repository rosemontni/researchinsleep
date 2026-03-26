---
name: third-party-proof-review
description: Run an external-model-style proof review for mathematical writing, proof reconstructions, and theorem projects. Use when a proof project needs an independent critical pass after internal drafting, when the user asks for third-party review, external review, adversarial review, proof audit, or a fresh model to try to break the argument, especially for projects like the Gleason example in this repo.
---

# Third-Party Proof Review

Conduct a fresh critical review of a proof project as if you were an external
reviewer, not the original author.

## Core Rule

Do not optimize for being agreeable. Optimize for identifying:

1. hidden assumptions
2. invalid inferences
3. overclaims about rigor or independence
4. notation drift
5. steps that are plausible but not fully closed

Treat the project as reviewable mathematical work, not as a chat transcript.

## Required Reviewer Posture

Maintain as much independence as possible:

1. Prefer the project's strongest summary documents first, not every scratch
   note.
2. Do not assume a step is valid because earlier notes say it is.
3. Reconstruct local reasoning from the project artifacts themselves.
4. Separate:
   - clearly proved
   - plausible but compressed
   - imported from source literature
   - unsupported

## Default Inputs

If the user does not specify a custom review set, review these in order:

1. the readable front-end document
2. the main proof document
3. the proof audit or status note
4. the narrow technical note for the highest-risk step

For the Gleason example in this repo, the default review set is:

1. `examples/gleason-theorem-accessible/EXPOSITORY_PAPER.md`
2. `examples/gleason-theorem-accessible/BEST_CURRENT_FULL_PROOF.md`
3. `examples/gleason-theorem-accessible/PROOF_AUDIT.md`
4. `examples/gleason-theorem-accessible/LATE_PROOF_DEPENDENCY_CHAIN.md`

Then load additional technical notes only when a finding depends on them.

## Review Workflow

### Phase 1: Establish claim level

Write down exactly what the project is claiming. Distinguish between claims like:

1. "best current reconstruction"
2. "fully independent proof"
3. "pedagogically accessible exposition"
4. "publication-ready note"

If the project's wording blurs these levels, flag it.

### Phase 2: Inspect proof structure

Map the proof into layers:

1. warmups / preliminaries
2. middle reduction
3. comparison construction
4. endgame contradiction

Record which layers look strongest and which look weakest.

### Phase 3: Attack the weakest layer

Pick the highest-risk proof step and try to break it.

For that step:

1. restate the inference in your own words
2. identify exact hypotheses used
3. check whether the conclusion really follows
4. look for missing case splits, hidden existence assumptions, or coordinate
   mixing

### Phase 4: Cross-check consistency

Check whether:

1. the readable paper and technical notes claim the same rigor level
2. notation is stable across documents
3. old notes contradict the newest summary
4. audit/status notes still match the current proof state

### Phase 5: Produce findings-first output

Write the review with findings first, severity ordered.

Use this structure:

```markdown
# Third-Party Proof Review

## Findings
1. [severity] [title]
   - affected files
   - why this is a real problem
   - whether it is a correctness issue, rigor gap, or presentation overclaim

## Overall Assessment
- strongest part:
- weakest part:
- current claim level that is justified:
- current claim level that is not yet justified:

## Recommended Next Step
- one highest-value revision
```

If there are no major correctness findings, say so explicitly and focus on the
remaining medium-risk compressions.

## Output Targets

When working inside a project, prefer writing:

- `THIRD_PARTY_REVIEW.md`

For the Gleason example, prefer:

- `examples/gleason-theorem-accessible/THIRD_PARTY_REVIEW.md`

If the project already has `PROOF_AUDIT.md`, do not overwrite it unless the
user explicitly asks. Treat `THIRD_PARTY_REVIEW.md` as a separate outside-pass
artifact.

## For This Repo

When reviewing a math example in this repo:

1. assume the lessons-learned system should record the main review insight
2. prefer concise, falsification-oriented findings
3. if the proof survives review, say what still prevents calling it a fully
   independent proof from scratch

## Extra Guidance

Read `references/review-checklist.md` when you want a compact checklist during
the review.
