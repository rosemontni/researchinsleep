# Best Current Full Proof Reconstruction

This document is the strongest current reconstruction in this project of the
Cooke--Keane--Moran proof of Gleason's theorem in dimension `3`.

It is written to do two things at once:

1. present one coherent proof narrative from start to finish,
2. be completely honest about which parts are fully rebuilt locally and which
   parts are still imported from the source paper.

So this is **not** a claim that we have a brand-new fully independent proof
from scratch. It is a best-current full proof record: as explicit as we can
currently make it, with every remaining dependency named.

Source paper:
[Cooke--Keane--Moran, "An elementary proof of Gleason's theorem"](https://rogermcooke.net/rogermcooke_files/Elementary%20Proof%20of%20Gleasons%20Theorem.pdf)

## Notation

Throughout:

- `(p,q,r)` denotes an unprimed orthonormal frame
- `(x,y,z)` are coordinates in that frame
- `(p',q',r')` denotes a primed orthonormal frame
- `(x',y',z')` are coordinates in that frame
- `w(f)` denotes the common frame-sum weight of a frame function `f`
- `g` denotes the quadratic comparison function built from extremal values
- `h = g - f` denotes the comparison error function

## 1. The theorem

Let `S` be the unit sphere in ordinary `3`-dimensional space. A **frame
function** is a bounded function `f : S -> R` such that for every orthonormal
triple `(p,q,r)` on the sphere, the sum

`f(p) + f(q) + f(r)`

has the same value. Call that common value `w(f)`.

Gleason's theorem in this `3`-dimensional setting says:

There exists an orthonormal frame `(p,q,r)` and real numbers `M, alpha, m`
such that if `(x,y,z)` are the coordinates of `s in S` in that frame, then

`f(s) = M x^2 + alpha y^2 + m z^2`.

Equivalently, every bounded frame function is the restriction to the sphere of
a quadratic form.

## 2. Core properties used throughout

The source paper uses these basic facts:

1. `P1`: frame functions form a vector space, and weights add linearly.
2. `P2`: frame functions are even, so `f(-s)=f(s)`.
3. `P3`: if four points lie on one great circle and form two orthogonal pairs,
   then the pair sums agree.
4. `P4`: if `f(s)` is almost maximal, then some point orthogonal to `s` has
   value almost minimal.

Among these, `P4` is now locally reconstructed in:

- [P4_RECONSTRUCTION.md](C:\Users\xliup\OneDrive\Documents\codex\researchinsleep\examples\gleason-theorem-accessible\P4_RECONSTRUCTION.md)

## 3. Warmup one-variable theorems

The source paper first proves two one-variable "warmup" theorems. Their role
is to turn additive frame-style constraints into linearity on `[0,1]`.

We do not reprove them line by line in this document, but we use them exactly
as the paper does.

They are now reconstructed locally in:

- [WARMUP_THEOREMS_RECONSTRUCTION.md](C:\Users\xliup\OneDrive\Documents\codex\researchinsleep\examples\gleason-theorem-accessible\WARMUP_THEOREMS_RECONSTRUCTION.md)

The two roles are:

1. Warmup I handles the no-exceptional-set case.
2. Warmup II handles the countable-exceptional-set case.

These are the engine behind the special-case theorem in Section 5.

## 4. The Section 4 basic lemma

Fix a north pole `p`, let `N` be the northern hemisphere, and let `E` be the
equator. Suppose:

1. `f(p) = sup f`,
2. `f` is constant on `E`.

For `s in N \\ {p}`, let `D_s` be the descent great circle through `s`: the
great circle for which `s` is the northernmost point.

Then for every `s' in D_s`,

`f(s) >= f(s')`.

This is now locally rebuilt in:

- [BASIC_LEMMA_RECONSTRUCTION.md](C:\Users\xliup\OneDrive\Documents\codex\researchinsleep\examples\gleason-theorem-accessible\BASIC_LEMMA_RECONSTRUCTION.md)

The key hidden step there is now explicit:

- `P4` implies the constant equator value is actually the global infimum.

So Section 4 is no longer a black box in our proof record.

## 5. The Section 5 geometric lemma

If `s,t in N` satisfy `l(s) > l(t)`, where

`l(s) = cos^2(angle(p,s))`,

then there exists a finite chain

`s = s_0, s_1, ..., s_n = t`

such that each `s_i` lies on the descent great circle `D_{s_{i-1}}`.

This is now locally reconstructed in:

- [GEOMETRIC_LEMMA_RECONSTRUCTION.md](C:\Users\xliup\OneDrive\Documents\codex\researchinsleep\examples\gleason-theorem-accessible\GEOMETRIC_LEMMA_RECONSTRUCTION.md)

The clean mechanism is:

1. project to the tangent plane,
2. one tangent turn by angle `phi` multiplies radius by `sec(phi)`,
3. many tiny turns let us match direction with arbitrarily small radius growth,
4. a two-step same-ray move reaches the exact target radius.

So the geometric lemma is also no longer just a figure-based sketch.

## 6. The Section 5 special-case theorem

Assume there is a point `p in S` such that:

1. `f(p)=M=sup f`,
2. `f(e)=m` for every `e` on the equator orthogonal to `p`.

Then for every `s in S`,

`f(s) = m + (M-m) cos^2(angle(p,s))`.

This is the first real quadratic-form theorem in the paper.

Its reconstruction is now split across:

- [SECTION5_RECONSTRUCTION.md](C:\Users\xliup\OneDrive\Documents\codex\researchinsleep\examples\gleason-theorem-accessible\SECTION5_RECONSTRUCTION.md)
- [BASIC_LEMMA_RECONSTRUCTION.md](C:\Users\xliup\OneDrive\Documents\codex\researchinsleep\examples\gleason-theorem-accessible\BASIC_LEMMA_RECONSTRUCTION.md)
- [GEOMETRIC_LEMMA_RECONSTRUCTION.md](C:\Users\xliup\OneDrive\Documents\codex\researchinsleep\examples\gleason-theorem-accessible\GEOMETRIC_LEMMA_RECONSTRUCTION.md)

The proof works as follows.

### 6.1 Normalize

If `M=m`, the conclusion is trivial. Otherwise replace `f` by

`(f-m)/(M-m)`.

So we may assume:

- `f(p)=1`,
- `f(e)=0` on the equator.

### 6.2 Monotonicity by latitude

By the basic lemma, one descent step cannot increase `f`.
By the geometric lemma, any lower-latitude point can be reached by finitely
many descent steps.

Hence if `l(s) > l(t)`, then

`f(s) >= f(t)`.

### 6.3 Upper and lower latitude envelopes

For each `l in [0,1]`, define:

- `bar_f(l) = sup { f(s) : l(s)=l }`,
- `under_f(l) = inf { f(s) : l(s)=l }`.

Monotonicity gives:

- `bar_f(1)=under_f(1)=1`,
- `bar_f(0)=under_f(0)=0`,
- if `l<l'`, then `bar_f(l) <= under_f(l')`.

### 6.4 The exceptional set is countable

Define

`C = { l : bar_f(l) > under_f(l) }`.

For each `l in C`, the interval

`(under_f(l), bar_f(l))`

is nonempty, and the separation property above makes these intervals pairwise
disjoint. Therefore `C` is at most countable.

### 6.5 Collapse to one variable

For `l notin C`, define

`F(l)=bar_f(l)=under_f(l)`.

Using the frame condition, `F` satisfies Warmup II, so

`F(l)=l`

for all `l notin C`.

### 6.6 Eliminate the exceptional set

Because `C` is countable, its complement is dense. Approaching any
`l_0 in C` from below and above through points outside `C`, the separation
property forces

`under_f(l_0)=bar_f(l_0)=l_0`,

contradicting `l_0 in C`.

So `C` is empty, and therefore

`f(s)=l(s)=cos^2(angle(p,s))`

in the normalized case, which is exactly

`f(s)=m+(M-m)cos^2(angle(p,s))`

before normalization.

This part of the proof is now in good shape.

## 7. Extremal values and first reduction

From here the paper moves to the general bounded frame function `f`.

Let

- `M = sup f`,
- `m = inf f`,
- `alpha = w(f)-M-m`.

The source paper next proves that bounded frame functions attain their
extremal values. This allows the choice of a frame `(p,q,r)` with:

- `f(p)=M`,
- `f(q)=alpha`,
- `f(r)=m`,

after a suitable coordinate choice.

In our project, this attainment step is now substantially reconstructed in:

- [SECTION6_RECONSTRUCTION.md](C:\Users\xliup\OneDrive\Documents\codex\researchinsleep\examples\gleason-theorem-accessible\SECTION6_RECONSTRUCTION.md)

What is now explicit there:

1. the almost-maximizing sequence `p_n -> p`,
2. the rigid-motion normalization `g_n`,
3. the symmetrization `h_n(s)=g_n(s)+g_n(hat_p s)`,
4. the equator-flattening property of `h_n`,
5. the compactness limit `h`,
6. the use of Section 5 to make `h` continuous,
7. the final approximate-basic-lemma argument forcing `f(p)=M`.

For the compactness/closure details, see:

- [SECTION6_TOPOLOGY_APPENDIX.md](C:\Users\xliup\OneDrive\Documents\codex\researchinsleep\examples\gleason-theorem-accessible\SECTION6_TOPOLOGY_APPENDIX.md)

So Section 6 is no longer a total black box. What remains imported there is
mainly the compactness/closure bookkeeping in the product space, not the whole
strategy.

## 8. Subtract the candidate quadratic

With such a frame fixed, define

`g(s) = M x^2 + alpha y^2 + m z^2`,

where `(x,y,z)` are the coordinates of `s` in the chosen frame.

This `g` is itself a frame function, with the same values as `f` at the three
coordinate axes and the same weight.

Set

`h = g - f`.

Then `h` is a bounded frame function with:

1. `w(h)=0`,
2. `h(p)=h(q)=h(r)=0`.

If we can show `h=0`, then `f=g` and the theorem is proved.

So the rest of the proof is a rigidity argument for weight-zero frame
functions.

## 9. The Section 7 six-circle comparison mechanism

The paper proves a key comparison claim:

If two frame functions agree at the three coordinate axes and one is the
quadratic comparison function, then they agree on the six symmetry great
circles

- `x=y`,
- `x=z`,
- `y=z`,
- `x=-y`,
- `x=-z`,
- `y=-z`.

In our project this mechanism is now much more explicit:

- [SECTION7_CLAIM_RECONSTRUCTION.md](C:\Users\xliup\OneDrive\Documents\codex\researchinsleep\examples\gleason-theorem-accessible\SECTION7_CLAIM_RECONSTRUCTION.md)
- [BRIDGE_DERIVATION.md](C:\Users\xliup\OneDrive\Documents\codex\researchinsleep\examples\gleason-theorem-accessible\BRIDGE_DERIVATION.md)
- [FRAME_RELATIVE_CLAIM.md](C:\Users\xliup\OneDrive\Documents\codex\researchinsleep\examples\gleason-theorem-accessible\FRAME_RELATIVE_CLAIM.md)
- [proof_checks.py](C:\Users\xliup\OneDrive\Documents\codex\researchinsleep\examples\gleason-theorem-accessible\proof_checks.py)

What is now locally established:

1. the quarter-turn identities can be written explicitly,
2. the six zero-circle consequences are explicit,
3. the whole claim is frame-relative and can be reused in any orthonormal
   coordinate system.

This is one of the strongest parts of our reconstruction.

## 10. The extremal endgame for `h`

Assume, toward contradiction, that `h` is not identically zero.

Choose a primed frame `(p',q',r')` adapted to `h`, with

- `h(p') = M' = sup h`,
- `h(q') = alpha'`,
- `h(r') = m' = inf h`.

Because `w(h)=0`,

`M' + alpha' + m' = 0`.

The paper's endgame shows this forces `h=0`.

Our local reconstruction of that endgame is spread across:

- [STEP_I_EXTREMAL_REDUCTION.md](C:\Users\xliup\OneDrive\Documents\codex\researchinsleep\examples\gleason-theorem-accessible\STEP_I_EXTREMAL_REDUCTION.md)
- [SADDLE_REDUCTION.md](C:\Users\xliup\OneDrive\Documents\codex\researchinsleep\examples\gleason-theorem-accessible\SADDLE_REDUCTION.md)
- [COORDINATE_CONTRADICTION.md](C:\Users\xliup\OneDrive\Documents\codex\researchinsleep\examples\gleason-theorem-accessible\COORDINATE_CONTRADICTION.md)
- [ENDGAME_INTERSECTION_LEMMA.md](C:\Users\xliup\OneDrive\Documents\codex\researchinsleep\examples\gleason-theorem-accessible\ENDGAME_INTERSECTION_LEMMA.md)
- [FINAL_ENDGAME_RECONSTRUCTION.md](C:\Users\xliup\OneDrive\Documents\codex\researchinsleep\examples\gleason-theorem-accessible\FINAL_ENDGAME_RECONSTRUCTION.md)

### 10.1 Step I: extremal reduction

The sharp local statement now is:

If `h` is nonzero and `w(h)=0`, then the primed extrema satisfy

- `M'=-m'`,
- `alpha'=0`.

This is reconstructed in:

- [STEP_I_EXTREMAL_REDUCTION.md](C:\Users\xliup\OneDrive\Documents\codex\researchinsleep\examples\gleason-theorem-accessible\STEP_I_EXTREMAL_REDUCTION.md)

The idea is:

1. if `m' > -M'`, then `alpha' < 0`,
2. on the great circle orthogonal to `p'`, every value is at most `alpha'`,
3. but one of the already-forced zero circles intersects that great circle,
4. contradiction.

Applying the same logic to `-h` rules out `m' < -M'`.

### 10.2 Step II: compare with the primed saddle

Define the comparison saddle

`H(x',y',z') = M'(x'^2 - z'^2)`.

Because the six-circle comparison claim is frame-relative, it applies in the
primed frame as well. So on the six primed symmetry great circles,

`h = H`.

This is the key correction to an earlier overstatement in our notes:

- we do **not** need a global identity `h=H` on all of `S`,
- we only need agreement on the six primed symmetry circles.

This is explained in:

- [FRAME_RELATIVE_CLAIM.md](C:\Users\xliup\OneDrive\Documents\codex\researchinsleep\examples\gleason-theorem-accessible\FRAME_RELATIVE_CLAIM.md)
- [SADDLE_REDUCTION.md](C:\Users\xliup\OneDrive\Documents\codex\researchinsleep\examples\gleason-theorem-accessible\SADDLE_REDUCTION.md)

### 10.3 Step III: the final contradiction

On the primed great circle `x'=y'`, the saddle `H` has exactly four zeros.

But the unprimed six-circle forcing argument already gives too many zero
constraints for a nonzero saddle to survive there. The contradiction is
captured in:

- [COORDINATE_CONTRADICTION.md](C:\Users\xliup\OneDrive\Documents\codex\researchinsleep\examples\gleason-theorem-accessible\COORDINATE_CONTRADICTION.md)
- [ENDGAME_INTERSECTION_LEMMA.md](C:\Users\xliup\OneDrive\Documents\codex\researchinsleep\examples\gleason-theorem-accessible\ENDGAME_INTERSECTION_LEMMA.md)
- [FINAL_ENDGAME_RECONSTRUCTION.md](C:\Users\xliup\OneDrive\Documents\codex\researchinsleep\examples\gleason-theorem-accessible\FINAL_ENDGAME_RECONSTRUCTION.md)

The cleaned-up geometric form is:

1. the six-circle mechanism forces specific antipodal zero pairs,
2. the only great circle through those pairs is a fixed symmetry circle,
3. that would make `h` vanish on an entire circle where the saddle has only
   four zeros,
4. contradiction.

Hence `h=0`.

Therefore `f=g`, so `f` is quadratic.

## 11. What is fully strong, and what is still imported

Here is the honest status of the proof stack.

### Strongly rebuilt locally

These parts are now in good or very good shape:

1. `P4`
2. the Section 4 basic lemma
3. the Section 5 geometric lemma
4. the one-variable core of the Section 5 special-case theorem
5. the six-circle comparison mechanism
6. the frame-relative reuse of the six-circle claim
7. the extremal reduction `M'=-m'`, `alpha'=0`

### Still imported or not yet fully rebuilt

These parts still depend materially on the source paper:

1. some standard compactness machinery inside Section 6 is cited rather than
   proved from first principles
2. some details of the last contradiction in the endgame, which are now quite
   explicit but are still best regarded as a faithful reconstruction rather
   than a completely independent derivation from first principles
3. the warmup theorems and Section 7 claim are now mostly reconstructed, though
   they are still not all compressed into a single self-contained formal paper
   proof

So the best current proof status is:

- **not** a fully independent new proof from scratch,
- but **yes**, a substantially rebuilt and much more explicit reconstruction of
  most of the paper's logical skeleton, especially the middle and late proof
  mechanisms.

## 12. The best honest conclusion

The strongest claim we can honestly make today is:

We now understand the Cooke--Keane--Moran proof at a much deeper structural
level than when this project started. The proof is no longer a mystery built
out of compressed page-long jumps. Its main mechanisms are visible:

1. descent geometry,
2. one-variable rigidity by latitude,
3. comparison with a quadratic candidate,
4. frame-relative six-circle forcing,
5. saddle contradiction.

What remains is no longer "the whole proof", but a much smaller set of
specific imported steps, chiefly the extremal-attainment machinery of Section
6 and some endgame bookkeeping.

That is what makes this the **best current full proof reconstruction**.
