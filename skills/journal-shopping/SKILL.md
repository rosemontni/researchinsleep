---
name: journal-shopping
description: Journal targeting, venue-fit analysis, and submission-package preparation for completed research papers. Use when a paper is final or near-final and Codex needs to shortlist reachable high-prestige journals, study recent papers from candidate venues, adapt the manuscript to venue-specific style, and prepare journal-specific submission packages.
---

# Journal Shopping

## Overview

Use this skill only after the paper itself is complete enough to judge honestly. The goal is not to chase the most famous journal blindly. The goal is to find the highest-prestige journal that is still realistically reachable for the paper's topic, evidence quality, maturity, and presentation.

Read [references/venue-scorecard.md](references/venue-scorecard.md) before starting. Read [references/submission-package.md](references/submission-package.md) when preparing the final packages.

Because journal scopes, policies, and recent publications change over time, always browse the internet when using this skill. Prefer official journal and publisher pages, recent tables of contents, and article pages over secondary summaries.

## Workflow

### 1. Gate The Task

Confirm that the paper is actually ready for venue selection.

Require these inputs when available:

- manuscript source and latest PDF
- abstract, title, keywords, and contribution summary
- review summary or internal quality assessment
- known weaknesses, risks, and evidence limits

If the paper is still missing core experiments or has unresolved claim-evidence problems, say so explicitly and stop before venue targeting.

### 2. Build A Longlist

Search for journals that fit the paper's area and contribution type.

Build a longlist of roughly 8 to 12 venues. For each venue, capture:

- scope fit
- prestige and visibility
- reachability for the current paper
- publication model and practical constraints
- recent relevant papers
- formatting or submission constraints that could materially affect suitability

Use the scorecard in [references/venue-scorecard.md](references/venue-scorecard.md). Do not rank by prestige alone.

### 3. Select The Final 3

Choose three journals that balance:

- highest realistic prestige
- topical fit
- alignment with the paper's current evidence level
- reachable editorial bar

Produce:

- a ranked longlist
- a top-3 shortlist
- a brief explanation of why the top choice is ambitious but still reachable
- explicit reasons for rejecting more prestigious but unrealistic venues

### 4. Study 20 Recent Relevant Papers Per Finalist

For each of the final three journals:

- identify 20 recent relevant papers
- read enough of each to learn the journal's recurring expectations
- focus on abstracts, introductions, figures, results framing, discussion style, and limitations language

Extract recurring patterns:

- title style
- abstract structure and claim density
- framing of novelty
- figure style and narrative pacing
- amount of method detail in main text
- tone around limitations and significance
- common submission components beyond the manuscript

Do not pretend to have read papers you could not access. If access is limited, say exactly what you were able to inspect.

### 5. Polish The Paper For Each Finalist

Prepare three separate venue-specific packages under a dedicated output folder such as `submissions/`.

For each finalist:

- adapt the manuscript framing and presentation style
- keep the science honest and unchanged unless the user requests substantive revisions
- align title, abstract, introduction, discussion, figures, and references to venue norms
- preserve factual accuracy and do not overclaim to match venue tone

### 6. Prepare Three Submission Packages

For each of the final three journals, prepare:

- a venue-specific manuscript source package
- a rendered PDF when the toolchain allows
- a cover letter draft
- a journal-fit memo
- a checklist of submission requirements and unresolved unknowns

Use the package structure in [references/submission-package.md](references/submission-package.md).

## Required Outputs

Create these artifacts unless the user requests a different layout:

- `journal-shopping/longlist.md`
- `journal-shopping/top-3.md`
- `journal-shopping/<journal-slug>/style-notes.md`
- `journal-shopping/<journal-slug>/paper-set.md`
- `submissions/<journal-slug>/`

Each `style-notes.md` should summarize the 20-paper study for that venue. Each `paper-set.md` should list the inspected papers with links, dates, and why they were relevant.

## Judgment Rules

- Prefer honest reachability over vanity targeting.
- Reject journals whose bar clearly exceeds the current evidence quality.
- Treat official author guidelines as source of truth for submission requirements.
- Treat recent published papers as source of truth for writing and presentation style.
- When the paper is prototype-level, bias toward strong specialist journals over unrealistic top-tier general journals.
- State uncertainty clearly when journal fit is close or access to recent papers is partial.
