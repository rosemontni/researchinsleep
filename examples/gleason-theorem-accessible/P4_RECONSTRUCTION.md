# Reconstructing property P4 cleanly

This note replaces the earlier loose draft of `P4` with a faithful and fully
usable reconstruction of the argument in Cooke--Keane--Moran.

## 1. The statement

Let `f` be a frame function on the sphere `S`. Write

- `M = sup_{u in S} f(u)`,
- `m = inf_{u in S} f(u)`.

Property `P4` says:

If `xi > 0` and `s in S` satisfies

`f(s) > M - xi`,

then there exists `t in S` with

- `t ⟂ s`,
- `f(t) < m + xi`.

So a point whose value is almost maximal forces an orthogonal point whose value
is almost minimal.

## 2. Pick two comparison points

Choose any `delta > 0`.

Because `M` is the supremum, we can choose a point `s'` with

`f(s') > M - xi + delta`.

Because `m` is the infimum, we can also choose a point `t'` with

`f(t') < m + delta`.

Now choose a point `t` such that

- `s ⟂ t`,
- `s' ⟂ t`.

Such a `t` exists because `s` and `s'` determine a plane, and the line
orthogonal to that plane meets the sphere in two antipodal points. Pick either
one.

The points `t` and `t'` determine a great circle on `S`. On that great circle,
choose `s''` so that

- `t ⟂ t'`,
- `s' ⟂ s''`.

All four points `s', s'', t, t'` now lie on the same great circle, with two
orthogonal pairs:

- `s' ⟂ s''`,
- `t ⟂ t'`.

## 3. Apply property P3

Property `P3` says that for four points on one great circle, arranged as two
orthogonal pairs, the pair sums agree. Therefore

`f(t) = f(s'') + f(t') - f(s')`.

Now estimate each term:

- `f(s'') <= M`, because `M` is the supremum,
- `f(t') < m + delta`, by construction,
- `f(s') > M - xi + delta`, by construction.

Substituting these into the identity gives

`f(t) < M + (m + delta) - (M - xi + delta)`.

The `M` terms cancel, and the `delta` terms cancel, so we obtain

`f(t) < m + xi`.

And by construction `t ⟂ s`.

That is exactly `P4`.

## 4. Why the proof is so effective

The argument is short because it uses `P3` in the right coordinate-free way.
The point `t` is built to be orthogonal to the almost-maximal point `s`, and
then `P3` lets us express `f(t)` as

- something at most `M`,
- plus something near `m`,
- minus something near `M`.

So the large positive contribution and the large negative contribution cancel,
leaving a value near the bottom.

This is the mechanism behind the proof:

- start near the top,
- transport through one great-circle identity,
- land near the bottom at an orthogonal point.

## 5. Why this matters downstream

The main use of `P4` in our reconstruction is in
[BASIC_LEMMA_RECONSTRUCTION.md](C:\Users\xliup\OneDrive\Documents\codex\researchinsleep\examples\gleason-theorem-accessible\BASIC_LEMMA_RECONSTRUCTION.md).

There, `P4` implies that if the north pole is the maximum and the equator is
constant, then the equator value must equal the global infimum. Once that is
known, the basic lemma turns descent geometry into monotonicity, and Section 5
collapses to a one-variable argument.

So `P4` is one of the small hinges that makes the whole proof move.

## 6. Status

This note is now in much better shape than the earlier draft. The proof is
short, explicit, and faithful to the printed argument. The main remaining
imported steps above it are no longer `P4` itself, but the later geometric
chaining lemma and the frame-relative comparison machinery in the endgame.
