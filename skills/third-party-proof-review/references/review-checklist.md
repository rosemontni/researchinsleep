# Review Checklist

Use this checklist when running a third-party-style proof review.

## Claim level

1. What is the project claiming?
2. Does the wording overclaim rigor, independence, or accessibility?

## Mathematical correctness

1. Is each late inference using only stated hypotheses?
2. Are there missing case splits?
3. Are there hidden existence assumptions?
4. Are coordinate systems mixed incorrectly?
5. Does any "therefore" step hide a nontrivial lemma?

## Dependency hygiene

1. Which parts are locally rebuilt?
2. Which parts are standard cited machinery?
3. Which parts are faithful reconstructions rather than independent proofs?

## Consistency

1. Do the expository and technical documents agree?
2. Does the audit still match the current proof state?
3. Do old notes contradict the newest summary?

## Output discipline

1. Findings first
2. Severity ordered
3. One best next step
