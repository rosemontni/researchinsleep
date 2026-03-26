# Toward an Accessible Geometric Reconstruction of Gleason's Theorem in Dimension 3

## Author Note

This document is an expository reconstruction of a published proof, not a claim
of a new theorem or a wholly new proof. The goal is clarity, proof-structure
visibility, and pedagogical accessibility.

## Abstract

Gleason's theorem is a foundational rigidity result, but many proofs are hard
for non-specialists to read. This note presents a geometry-first reconstruction
of the Cooke--Keane--Moran elementary proof in dimension `3`. The reconstruction
has two goals: reduce dependence on advanced physics language and make the proof
architecture visible. The paper isolates the special-case latitude-rigidity
argument, reconstructs the comparison-with-quadratic strategy, and rewrites the
late proof as a sequence of symmetry and great-circle constraints. The result is
not claimed as a new proof; it is a best-current expository reconstruction of a
published elementary proof, supported by a technical appendix stack in the
surrounding project.

## 1. Introduction

In the sphere formulation of Gleason's theorem, one studies bounded functions
on the unit sphere `S` in `R^3` that satisfy a single consistency condition:
the sum of the function values on any orthonormal triple is constant. The
remarkable conclusion is that every such function must be quadratic in suitable
coordinates.

This statement is deep but surprisingly geometric. One does not need to begin
with density matrices or advanced quantum formalism. Instead, one can work with
ordinary sphere geometry, great circles, and a carefully structured rigidity
argument.

The paper by Cooke, Keane, and Moran remains the most relevant published source
for this geometric viewpoint. But parts of the proof are compressed, especially
the middle reduction to latitude and the final contradiction. This note presents
the proof in a cleaner layered form and separates:

1. the readable expository narrative
2. the strongest current technical reconstruction
3. the remaining imported standard machinery

## 2. The theorem

Let `S` be the unit sphere in `R^3`. A bounded function `f : S -> R` is a frame
function if there is a constant `w(f)` such that for every orthonormal triple
`(p,q,r)` on the sphere,

`f(p) + f(q) + f(r) = w(f)`.

Gleason's theorem in this setting says that there exists an orthonormal frame
and real numbers `M, alpha, m` such that

`f(x,y,z) = M x^2 + alpha y^2 + m z^2`

for every point `(x,y,z)` on `S`.

So the single frame-sum condition forces a very rigid algebraic form.

## 3. Proof architecture

The proof has two major halves.

### 3.1 Special-case rigidity

If the function is maximal at a pole and constant on the equator orthogonal to
that pole, then it must equal

`m + (M-m) cos^2(theta)`

where `theta` is the polar angle.

The proof idea is:

1. descent moves along special great circles cannot increase the function
2. every lower-latitude point can be reached by finitely many descent moves
3. this collapses the sphere problem to a one-variable problem in latitude
4. boundedness and the frame-sum rule force linearity in the latitude parameter

### 3.2 General-case comparison

For a general bounded frame function `f`, choose a frame adapted to extremal
values and define the quadratic comparison function

`g(x,y,z) = M x^2 + alpha y^2 + m z^2`.

Then set

`h = g - f`.

The rest of the proof shows that `h` must vanish identically.

The key late-proof steps are:

1. `h` vanishes on six symmetry great circles
2. in a primed extremal frame, the extrema of `h` force a saddle comparison
3. the primed saddle has only four zeros on one special circle
4. the unprimed zero circles force that same circle through two special
   antipodal pairs
5. that determines the circle uniquely as one of the unprimed zero circles
6. contradiction

## 4. The special-case theorem

Fix a pole `p`. Suppose:

1. `f(p)` is maximal
2. `f` is constant on the equator orthogonal to `p`

Then `f` is forced to depend only on latitude, and in fact quadratically.

The conceptual core is that the proof becomes one-variable after the descent
geometry is understood. Once the function is trapped between upper and lower
latitude envelopes, a warmup functional-equation theorem forces those envelopes
to collapse.

This is the part of the proof that becomes most intuitive after reconstruction.

## 5. The six-circle mechanism

The late proof relies on two quarter-turn rotations. They generate cancellation
identities for the difference function `h = g-f`. Those identities imply that if
one can send a point to its antipode by an odd word in the quarter-turns, then
the value of `h` at that point must be zero.

This mechanism forces `h=0` on six symmetry great circles:

- `x=y`
- `x=z`
- `y=z`
- `x=-y`
- `x=-z`
- `y=-z`

These circles become the geometric skeleton of the endgame.

## 6. The final contradiction

Assume `h` is not zero. Move to a primed frame adapted to the extrema of `h`.
The weight-zero condition forces symmetric extrema and a zero middle value, so
the natural comparison object is the saddle

`H(x',y',z') = M'(x'^2 - z'^2)`.

On the primed circle `x'=y'`, the function `h` agrees with `H`, so it has only
four zeros there.

But the already-known unprimed zero circles force this same primed circle
through two special antipodal pairs. Those four points determine a unique great
circle, which is one of the unprimed zero circles. So `h` must vanish
identically on that circle.

That contradicts the saddle behavior unless the saddle coefficient is zero.
Hence the extrema of `h` are all zero, so `h` itself is zero, and therefore
`f=g`.

## 7. What this paper claims

This paper claims:

1. a cleaner and more pedagogically visible reconstruction of the
   Cooke--Keane--Moran proof
2. a geometry-first explanation that avoids physics-first framing
3. a proof architecture that is easier to audit than the compressed source

This paper does not claim:

1. a new proof of Gleason's theorem
2. a fully independent proof from scratch
3. a fully elementary proof in the sense of being easy for a high-school
   student

## 8. What feedback is most useful

The most valuable review questions for this manuscript are:

1. Is the mathematical claim level honest?
2. Is the proof architecture clear to a mathematically mature outsider?
3. Are any parts still overcompressed or misleadingly presented as more closed
   than they are?
4. Is the exposition useful as a readable route into the Cooke proof?

## References

1. A. M. Gleason, *Measures on the Closed Subspaces of a Hilbert Space*, 1957.
2. Roger Cooke, Michael Keane, William Moran, *An elementary proof of
   Gleason's theorem*, 1985.
3. Fred Richman and Douglas Bridges, *A Constructive Proof of Gleason's
   Theorem*, 1999.
4. Ehud Hrushovski and Itamar Pitowsky, *Generalizations of Kochen and
   Specker's theorem and the effectiveness of Gleason's theorem*, 2004.
