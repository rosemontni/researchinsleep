# Reconstructing the geometric lemma from Section 5

This note rebuilds the geometric lemma at the start of Section 5 in a more
explicit way than our earlier notes. The proof in Cooke--Keane--Moran is
correct but diagram-heavy. Here we isolate the real mechanism.

## 1. The statement

Let `s,t` lie in the northern hemisphere `N`, and suppose

`l(s) > l(t)`.

Then there exist points

`s_0, s_1, ..., s_n in N`

such that

- `s_0 = s`,
- `s_n = t`,
- for each `1 <= i <= n`, we have `s_i in D_{s_{i-1}}`.

So starting from `s`, we can reach any lower-latitude point `t` by a finite
chain of descent moves.

## 2. Pass to the tangent plane

Project the northern hemisphere `N` from the center of the sphere onto the
plane tangent to the sphere at the north pole `p`.

Under this projection:

- points of a fixed latitude become a circle centered at `p`,
- a descent great circle through a point becomes the tangent line to that
  latitude circle at the projected point.

So in the tangent plane, the lemma becomes a purely planar statement:

> Given two points `s,t` in the plane with `|t| > |s|`, we can go from `s` to
> `t` by finitely many moves, each move going from the current point to some
> other point on the tangent line to the centered circle through the current
> point.

Here `|x|` means distance from the center `p`.

## 3. The one-step tangent formula

Let `a` be a point in the plane with radius `r = |a|`, and let `b` be a point
reached from `a` by one tangent move.

Then the circle through `a` has tangent line

`a · x = r^2`.

So `b` lies on that tangent line exactly when

`a · b = r^2`.

Write `phi` for the angle between the rays `pa` and `pb`, and let `|b| = R`.
Then

`a · b = r R cos(phi) = r^2`,

so

`R = r sec(phi)`.

This is the key formula:

**a single tangent move that turns the direction by angle `phi` multiplies the
radius by `sec(phi)`.**

## 4. First move type: same-ray outward motion in two steps

Suppose `u` and `v` lie on the same ray from `p`, with

`|u| = r < R = |v|`.

We claim that `v` can be reached from `u` in exactly two tangent moves.

Rotate coordinates so

- `u = (r,0)`,
- `v = (R,0)`.

Choose an intermediate point

`w = (r, h)`,

where

`h = sqrt(r(R-r))`.

Then:

1. `w` lies on the tangent line at `u`, because the tangent line to the circle
   `x^2 + y^2 = r^2` at `(r,0)` is `x=r`.
2. `v` lies on the tangent line at `w`, because

   `w · v = rR = r^2 + h^2 = |w|^2`.

So

`u -> w -> v`

is a two-step tangent path.

This is the precise version of the paper's Figure 2.

## 5. Second move type: change direction while barely increasing radius

Now suppose we want to change direction by a total angle `Theta > 0` while
keeping the radius increase very small.

Take `n` equal turning steps, each of angle

`phi = Theta / n`.

By the one-step tangent formula, each step multiplies the radius by

`sec(phi)`,

so after `n` steps the total radius factor is

`sec(phi)^n = sec(Theta/n)^n`.

As `n -> infinity`,

`sec(Theta/n)^n -> 1`.

So by taking many very small tangent turns, we can rotate by any fixed total
angle `Theta` while increasing the radius by an arbitrarily small factor.

This is the real content behind the paper's Figure 3.

## 6. Build the full path to `t`

Let the projected starting point be `s`, and the projected target be `t`.
Since `l(s) > l(t)`, the target has larger projected radius:

`|t| > |s|`.

Write:

- `r = |s|`,
- `R = |t|`,
- `Theta` for the angle from the ray `ps` to the ray `pt`.

Because `R > r`, we can choose `n` so large that

`r sec(Theta/n)^n < R`.

Now take `n` small tangent steps, each turning by `Theta/n`. Starting from `s`,
this produces a point `u` with:

- `u` on the same ray from `p` as `t`,
- `|u| = r sec(Theta/n)^n < R = |t|`.

So `u` and `t` lie on the same ray, and `u` is closer to `p` than `t`.

By the two-step same-ray construction from Section 4, we can then go from `u`
to `t` in two more tangent moves.

Therefore `t` is reachable from `s` by a finite sequence of tangent moves.

Translating back to the sphere, this gives a finite sequence

`s = s_0, s_1, ..., s_m = t`

with

`s_i in D_{s_{i-1}}`

for each `i`.

That proves the geometric lemma.

## 7. Why this reconstruction is better

The printed proof packages the geometry into Figures 2 and 3. This note makes
the two underlying move types explicit:

1. **same-ray expansion** in two steps,
2. **small-angle turning** with radius factor `sec(phi)`.

Once those are isolated, the lemma becomes very transparent:

- use many tiny turns to match the target direction,
- stop while still inside the target radius,
- then use the two-step same-ray move to reach the target exactly.

## 8. Why this matters for the whole proof

Together with
[BASIC_LEMMA_RECONSTRUCTION.md](C:\Users\xliup\OneDrive\Documents\codex\researchinsleep\examples\gleason-theorem-accessible\BASIC_LEMMA_RECONSTRUCTION.md),
this lemma gives monotonicity by latitude:

- each descent step cannot increase `f`,
- the geometric lemma says any lower-latitude point is reachable by such steps,
- therefore higher latitude dominates lower latitude.

That is exactly what powers
[SECTION5_RECONSTRUCTION.md](C:\Users\xliup\OneDrive\Documents\codex\researchinsleep\examples\gleason-theorem-accessible\SECTION5_RECONSTRUCTION.md).

## 9. Status

This note gives a cleaner and more modular proof than our earlier sketch. The
main remaining imported parts of the overall Gleason reconstruction are now no
longer the Section 4 and Section 5 preliminaries, but the later extremal and
endgame steps.
