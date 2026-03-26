# Source Notes

## Primary source

- Roger Cooke, "Elementary Proof of Gleason's Theorem"
- URL: https://rogermcooke.net/rogermcooke_files/Elementary%20Proof%20of%20Gleasons%20Theorem.pdf

## High-level statement

The paper proves Gleason's theorem for separable real or complex Hilbert spaces of dimension greater than two.

Equivalent real 3-dimensional form used in the paper:

- work on the unit sphere `S` in `R^3`
- a **frame** is a triple of mutually perpendicular unit vectors
- a **frame function** is a function `f : S -> R` whose sum `f(p)+f(q)+f(r)` is the same for every frame `(p,q,r)`
- the goal is to show every bounded frame function comes from a quadratic form

## What the paper actually does

The paper is already much less physics-heavy than the theorem's usual motivation. The proof itself is mostly geometry plus real analysis.

Main proof structure from the paper:

1. Reduce the general theorem to the case `H = R^3`.
2. Replace the measure-on-subspaces language with bounded frame functions on the sphere.
3. Prove two warmup theorems about functions on `[0,1]` that behave linearly under `a+b+c=1`.
4. Prove a basic geometric lemma on the northern hemisphere using "latitude" and "descent" great circles.
5. Use that lemma to prove the simple case where the function has a maximum at a north pole and is constant on the equator.
6. Show bounded frame functions attain extrema.
7. Compare a general frame function with a quadratic candidate having the same extremal data, and prove the difference must vanish.

## Key technical moves

The paper's core moves are:

- convert subspace probabilities into a sphere-coloring style problem
- use compactness to get maxima and minima
- use a geometric propagation argument on the sphere
- prove a special case first, then bootstrap to the general case
- force the difference between two candidate frame functions to be identically zero

## Strongest reusable proof idea from the paper

The strongest piece for an accessible treatment is the special case in sections 4 and 5:

- north pole has maximal value
- equator has a constant value

Then the proof turns the whole problem into a statement about latitude.

That is the moment where the theorem becomes narratable:

- higher latitude means larger value
- equal latitudes should carry the same value
- the resulting latitude function satisfies a simple additivity rule on `[0,1]`
- that additivity forces linearity
- linearity in latitude means a quadratic formula in coordinates

This is the current best bridge between the full theorem and an accessible proof story.

## Why it is still hard for a high school audience

Even without advanced physics, the paper still expects:

- comfort with Hilbert-space language
- translation between subspaces and points on the sphere
- boundedness and continuity-style arguments
- compactness and extremal-value reasoning
- multi-step geometric lemmas on great circles

So the real obstacle is not quantum mechanics. It is the level of abstract geometry and analysis.

## Honest takeaway after first reading

The cited paper does not really require advanced physics to follow its proof. It mostly requires undergraduate-level real analysis and abstract linear geometry.

That means the best route toward a "high-school-accessible" version is probably not a fully faithful replacement proof of the whole theorem. A more realistic target is:

- a rigorous special case in ordinary 3D language, plus
- a clear explanation of how the full theorem extends beyond that special case

Pending close reading.
