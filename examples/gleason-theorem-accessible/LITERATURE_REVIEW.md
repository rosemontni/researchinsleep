# Literature Review: Proofs and Proof Families Around Gleason's Theorem

This note reviews the main proof traditions around Gleason's theorem, with one
specific project question in mind:

Can we find, or build, a proof route that is more accessible than the standard
presentations, ideally without advanced physics language?

The review is not a general history of quantum foundations. It is a focused map
of the proof literature that matters for this project.

## 1. The baseline: Gleason's original theorem

The starting point is:

- A. M. Gleason, *Measures on the Closed Subspaces of a Hilbert Space* (1957)

This is the original theorem proving that, in Hilbert spaces of dimension
greater than `2`, finitely additive probability assignments on closed
subspaces come from density operators / quadratic forms.

For our purposes, the important point is not just historical priority. Gleason's
paper sets the standard target that later proof families try to improve on in
different ways:

1. make the proof shorter,
2. make it more elementary,
3. make it constructive,
4. generalize it to effects / POVMs,
5. weaken assumptions in low dimensions.

Project takeaway:

- essential mathematically,
- not the best starting point for accessibility.

Source:
- [Celebratio entry for Gleason 1957](https://celebratio.org/Gleason_AM/article/312/)

## 2. The elementary proof line

The most relevant paper for this project remains:

- Roger Cooke, Michael Keane, William Moran, *An elementary proof of Gleason's theorem* (1985)

This is the central source for our reconstruction work. Its stated goal is
accessibility to undergraduates with real analysis, and it replaces most of the
operator-theoretic machinery with sphere geometry, frame functions, descent
circles, and a final rigidity argument.

Strengths:

1. the proof is concrete and geometric,
2. it stays close to ordinary `3`-dimensional space,
3. it is much more teachable than the original Hilbert-space-heavy route,
4. it is the best fit we have found for an "accessible, non-physics-first"
   project.

Weaknesses:

1. it is still not actually easy,
2. the section 4 to section 7 chain is compressed,
3. the final two pages hide a lot of geometric bookkeeping,
4. "accessible to undergraduates" is still far from "high-school accessible."

Project takeaway:

- this is still the best direct source for our current goal,
- but it needs careful reconstruction to become genuinely readable.

Sources:
- [Cambridge abstract / metadata](https://www.cambridge.org/core/journals/mathematical-proceedings-of-the-cambridge-philosophical-society/article/an-elementary-proof-of-gleasons-theorem/89A7AB2F467BD015B2115B637867FB32)
- [PDF entry](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/89A7AB2F467BD015B2115B637867FB32/S0305004100063313a.pdf/an-elementary-proof-of-gleasons-theorem.pdf)

## 3. The constructive proof line

Another major direction is constructive mathematics:

- Fred Richman and Douglas Bridges, *A Constructive Proof of Gleason's Theorem* (1999)

This line asks not just whether the theorem is true, but whether it can be
proved in a constructive framework without relying on non-constructive
existence arguments.

Strengths:

1. foundationally deep,
2. sharper about effective content,
3. relevant if one cares about computability and explicit approximation.

Weaknesses for our project:

1. constructive proofs are usually less intuitive for beginners,
2. they shift the difficulty from geometry/analysis to logic/foundations,
3. they do not obviously move us closer to a high-school explanation.

Project takeaway:

- important for rigor and proof-theoretic understanding,
- not obviously the best route for pedagogical accessibility.

Source:
- [ScienceDirect abstract](https://www.sciencedirect.com/science/article/pii/S0022123698933729)

## 4. The effectiveness line

Closely related is the "effectiveness" literature:

- Ehud Hrushovski and Itamar Pitowsky, *Generalizations of Kochen and Specker's theorem and the effectiveness of Gleason's theorem* (2004)

This work connects Gleason's theorem to compactness, finite ray constructions,
and effective approximability.

Why it matters here:

1. it shows Gleason's theorem has more algorithmic/finite content than one
   might expect,
2. it helps explain why finite forcing arguments appear naturally,
3. it supports the idea that some parts of the theorem can be made more
   explicit and constructive.

But for accessibility:

1. it is philosophically and logically interesting,
2. it is not simpler than Cooke for a novice,
3. it does not hand us a clean elementary teaching proof.

Project takeaway:

- useful as a conceptual check on what can be made explicit,
- not the best main narrative for a student-facing exposition.

Sources:
- [PhilSci-Archive preprint](https://philsci-archive.pitt.edu/1263/)
- [journal metadata](https://weizmann.elsevierpure.com/en/publications/generalizations-of-kochen-and-speckers-theorem-and-the-effectiven/)

## 5. The generalized-observable / POVM line

A different proof family loosens the measurement assumptions:

- Paul Busch, *Quantum states and generalized observables: a simple proof of Gleason's theorem* (2003)
- Carlton Caves, Christopher Fuchs, Kiran Manne, Joseph Renes, *Gleason-type derivations of the quantum probability rule for generalized measurements* (2004)

These are often described as simpler than Gleason's original theorem, but there
is a crucial nuance:

- they are usually **Gleason-type** theorems on effects / POVMs,
- not just rephrasings of the original projective-measurement theorem.

Strengths:

1. conceptually elegant,
2. short,
3. important for quantum-information formulations of the Born rule,
4. they often extend to dimension `2`, where original Gleason does not.

Weaknesses for our project:

1. they rely on generalized measurements, which is more "modern QM" than our
   current geometric route,
2. the simplicity comes partly from changing the assumptions,
3. they are less helpful if our explicit target is a proof close to ordinary
   sphere geometry and understandable without advanced quantum formalism.

Project takeaway:

- very important if the goal is the Born rule under broader measurement
  assumptions,
- not a drop-in replacement for our current "accessible classical-geometry"
  project.

Sources:
- [PubMed / PRL metadata for Busch 2003](https://pubmed.ncbi.nlm.nih.gov/14525351/)
- [White Rose metadata for Busch 2003](https://eprints.whiterose.ac.uk/7250/)
- [PhilPapers entry for Caves–Fuchs–Manne–Renes 2004](https://philpapers.org/rec/CAVGDO)

## 6. The modern Gleason-type line

A more recent strand studies Gleason-type theorems via functional equations and
simulable measurements:

- Victoria Wright and Stefan Weigert, *Gleason-Type Theorems from Cauchy's Functional Equation* (2019)
- related work on qubits via mixtures of projective measurements

This line is mathematically interesting because it explains why additivity
constraints can force linearity through methods that resemble the study of
Cauchy's equation.

Strengths:

1. conceptually clean,
2. gives alternative proofs for some generalized results,
3. clarifies where continuity/regularity enters.

Weaknesses for our project:

1. the authors explicitly distinguish these theorems from Gleason's original
   theorem,
2. the approach is better for POVM/effect settings than for the original
   projective setting,
3. it does not currently solve our main problem of finding a truly simple proof
   of the original theorem.

Project takeaway:

- valuable background on why "Gleason-type" theorems can become simpler,
- not evidence that the original theorem itself already has a high-school-level
  proof.

Sources:
- [Springer article page](https://link.springer.com/article/10.1007/s10701-019-00275-x)
- [open repository version](https://eprints.whiterose.ac.uk/id/eprint/146960/)
- [PIRSA talk on qubit Gleason-type theorem](https://pirsa.org/19050023)

## 7. What the literature says about our exact project goal

Our project goal is stricter than most papers in the literature:

1. no advanced physics dependence,
2. ordinary `3`-space intuition if possible,
3. as explainable as possible to a strong high-school student.

The literature strongly suggests the following:

### 7.1 There are simpler proof families, but often for different theorems

Many "simpler" modern proofs are simpler because they prove a generalized
Born-rule theorem on effects or POVMs, not because they make the original
projective Gleason theorem elementary in the same way.

### 7.2 Cooke remains the closest fit

Among the proof families we surveyed, Cooke--Keane--Moran still looks like the
closest published proof to our target:

- concrete,
- geometric,
- low-dimensional,
- not deeply dependent on physics language.

But even Cooke stops well short of true novice accessibility.

### 7.3 A full high-school-level proof does not appear to already exist in the
literature

Based on the sources reviewed here, I do **not** see evidence of a standard,
widely recognized, fully rigorous, high-school-accessible proof of the full
original Gleason theorem.

That does not prove none exists anywhere, but it strongly suggests our project
is nontrivial and potentially original in pedagogical aim, even if not yet in
mathematical content.

## 8. Best current conclusions for this repo

The literature review suggests these concrete choices for our project:

1. keep Cooke as the main proof backbone,
2. use constructive/effective papers mainly for meta-understanding, not as the
   main student-facing route,
3. distinguish sharply between original Gleason proofs and Gleason-type POVM
   theorems,
4. avoid overclaiming "simple proof" when the theorem has only been simplified
   by changing assumptions,
5. focus our novelty on exposition and reconstruction, not on pretending the
   literature already solved the high-school-accessibility problem.

## 9. Ranked relevance for this project

Most relevant:

1. Cooke--Keane--Moran (1985)
2. Richman--Bridges (1999)
3. Hrushovski--Pitowsky (2004)

Important but secondary because they address Gleason-type generalizations:

4. Busch (2003)
5. Caves--Fuchs--Manne--Renes (2004)
6. Wright--Weigert (2019)

Historical foundation:

7. Gleason (1957)

## 10. Bottom line

The literature does **not** currently tell us:

- "here is the already-known high-school proof."

It does tell us:

- there are several proof traditions,
- Cooke is still the best direct source for an elementary reconstruction of the
  original theorem,
- constructive and generalized-measurement lines are important but solve a
  somewhat different problem,
- our current repo direction is reasonable: deepen the Cooke reconstruction and
  improve exposition rather than pretending that the literature has already made
  the full theorem genuinely easy.
