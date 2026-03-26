# Special-Case Proof

This file develops the strongest genuinely elementary proof direction found so far.

## The special case

Work on the unit sphere in ordinary 3D space.

Let `f` assign a real number to each direction, with the rule that for every orthonormal triple `(u,v,w)`,

`f(u) + f(v) + f(w) = 1`.

Assume also:

- `f` is continuous
- `f` reaches its maximum `M` at the north pole `p = (0,0,1)`
- `f` is constant on the equator, with value `m`

Then the claim is:

`f(x,y,z) = m + (M-m) z^2`.

This is already a substantial and meaningful piece of the Gleason story.

## Why this case matters

This is the first place where a real rigidity phenomenon becomes visible:

- the rule about perpendicular triples does not merely constrain `f`
- together with continuity and one symmetry condition, it forces a quadratic formula

So this is the best current target for a high-school-friendly version.

## Step 1. Latitude as the right variable

For a point `s` on the sphere, define its **latitude parameter**

`l(s) = z^2 = cos^2(theta(s,p))`.

If the final formula is true, then `f` should only depend on `l(s)`.

So the real task is:

1. prove points higher up have at least as large a value
2. prove points with the same latitude actually have the same value
3. identify that common value

## Step 2. Descent curves

For a point `s` in the northern hemisphere, there is a great circle through `s` whose highest point is `s` itself and which then descends toward the equator on both sides.

Call this the descent curve through `s`.

The key monotonicity lemma used in Cooke's proof is:

> if `s'` lies below `s` on the descent curve through `s`, then `f(s) >= f(s')`.

Why this feels plausible:

- the top point of the descent curve is geometrically special
- because the north pole is maximal and the equator is flat, the frame rule forces values to decrease as you slide down the descent curve

This is the first genuinely nontrivial geometric step.

## Step 3. Comparing two different latitudes

There is also a geometric lemma:

> if `s` and `t` are in the northern hemisphere and `l(s) > l(t)`, then you can move from `s` to `t` by a finite chain of descent steps.

Combining this with the previous step gives:

> if `l(s) > l(t)`, then `f(s) >= f(t)`.

So higher latitude means larger value.

## Step 4. Turn the sphere into a function on `[0,1]`

For each latitude level `l`, define:

- `F_upper(l)` = largest value of `f` on that parallel
- `F_lower(l)` = smallest value of `f` on that parallel

The monotonicity from Step 3 shows both of these are increasing functions of `l`.

If `F_upper(l) = F_lower(l)`, then `f` has a single value on that latitude.

Let `C` be the set of bad latitudes where `F_upper(l) > F_lower(l)`.

The proof shows that `C` must be at most countable.

## Step 5. Use the frame rule on latitude triples

For a point `s = (x,y,z)`, the numbers `x^2`, `y^2`, and `z^2` add to `1`.

So for every triple of nonnegative numbers `(a,b,c)` with `a+b+c=1`, there is an orthonormal frame whose latitude parameters are exactly `a`, `b`, and `c`.

That means the common latitude-value function should satisfy:

`G(a) + G(b) + G(c) = 1`

whenever `a+b+c=1`.

Also:

- `G(0)=m`
- `G(1)=M`
- `G` is increasing

This is now an ordinary interval problem, not a sphere problem.

## Step 6. Interval rigidity

Cooke proves warmup results showing that an increasing function on `[0,1]` with this triple-sum rule must be linear.

So the latitude-value function must be

`G(l) = m + (M-m) l`.

Therefore

`f(s) = m + (M-m) l(s) = m + (M-m) z^2`.

That is exactly the quadratic form we wanted.

## What remains hard

This still does not complete the full theorem, because the full theorem still has to justify:

- why one may reduce to this special setup
- why the difference between a general frame function and the right quadratic candidate fits this special case after normalization
- why the final comparison kills all remaining degrees of freedom

## Honest assessment

This special-case proof is the strongest current candidate for a genuinely accessible explanation.

It still uses some real geometry and continuity. But compared with the full theorem, it has a much clearer story:

- values move monotonically with latitude
- equal-latitude values collapse to a single function `G`
- the frame rule forces `G` to be linear
- linearity in `z^2` means the whole function is quadratic
