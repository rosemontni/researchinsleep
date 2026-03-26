# Final endgame reconstruction

This note gives the cleanest current reconstruction of the last pages of the
Cooke--Keane--Moran proof, corresponding to the four endgame steps on pages
127--128.

Its job is narrower than
[BEST_CURRENT_FULL_PROOF.md](C:\Users\xliup\OneDrive\Documents\codex\researchinsleep\examples\gleason-theorem-accessible\BEST_CURRENT_FULL_PROOF.md):
it focuses only on the last rigidity argument for the error function

`h = g - f`.

For a standalone version of the great-circle case split used below, see also
[ENDGAME_INTERSECTION_LEMMA.md](C:\Users\xliup\OneDrive\Documents\codex\researchinsleep\examples\gleason-theorem-accessible\ENDGAME_INTERSECTION_LEMMA.md).

Here:

- `g` is the quadratic comparison function in the unprimed frame,
- `h` is a bounded frame function,
- `w(h)=0`,
- `h` vanishes on the six unprimed symmetry great circles
  `x = ± y`, `x = ± z`, `y = ± z`.

We assume, toward contradiction, that `h` is not identically zero.

## 1. Choose primed extremal coordinates

Because `h` is bounded and Section 6 gives extremal attainment, choose an
orthonormal frame `(p',q',r')` such that:

- `h(p') = M' = sup h`,
- `h(q') = alpha'`,
- `h(r') = m' = inf h`.

Write `(x',y',z')` for coordinates in this primed frame.

Since `w(h)=0`, we have

`M' + alpha' + m' = 0`.

## 2. Step (i): force symmetric extrema

The first endgame claim is:

`M' = -m'`.

This is reconstructed in
[STEP_I_EXTREMAL_REDUCTION.md](C:\Users\xliup\OneDrive\Documents\codex\researchinsleep\examples\gleason-theorem-accessible\STEP_I_EXTREMAL_REDUCTION.md),
but the key idea is short:

1. Assume `m' > -M'`.
2. Then `alpha' = -(M' + m') < 0`.
3. By `P3`, the value `alpha'` becomes the maximal value of `h` on the great
   circle orthogonal to `p'`.
4. But one of the already-known unprimed zero circles must intersect that
   great circle in an antipodal pair, forcing the value `0` there.
5. Since `0 > alpha'`, contradiction.

Applying the same argument to `-h` rules out `m' < -M'`.

Therefore

`M' = -m'`.

## 3. Step (ii): force the middle value to vanish

Now use the weight-zero identity:

`M' + alpha' + m' = 0`.

Since `m' = -M'`, this immediately gives

`alpha' = 0`.

So the primed extremal data collapse to

- top value `M'`,
- middle value `0`,
- bottom value `-M'`.

## 4. Step (iii): compare `h` with the primed saddle

Define the primed comparison saddle

`H(x',y',z') = M'(x'^2 - z'^2)`.

This is a frame function with:

- maximum `M'` at `p'`,
- minimum `-M'` at `r'`,
- value `0` at `q'`,
- weight `0`.

Now apply the Section 7 comparison claim in the **primed** frame.

This is legitimate because the claim is frame-relative; see
[FRAME_RELATIVE_CLAIM.md](C:\Users\xliup\OneDrive\Documents\codex\researchinsleep\examples\gleason-theorem-accessible\FRAME_RELATIVE_CLAIM.md).

Since `h` and `H` agree at the three primed coordinate axes and have the same
weight, the comparison claim gives:

`h = H`

on the six primed symmetry great circles:

- `x' = y'`,
- `x' = z'`,
- `y' = z'`,
- `x' = -y'`,
- `x' = -z'`,
- `y' = -z'`.

This is the exact place where our earlier notes had briefly overreached.
The needed conclusion is **not** that `h=H` globally, only that they agree on
those six primed circles.

## 5. Step (iv): analyze the primed circle `x' = y'`

Restrict `H` to the primed great circle `x' = y'`.

On the sphere, this circle is given by

- `x' = y'`,
- `2x'^2 + z'^2 = 1`.

Along this circle,

`H = M'(x'^2 - z'^2)`.

So `H=0` exactly when

`x'^2 = z'^2`.

Together with `x'=y'`, this gives exactly four points:

- `(a,a,a)`,
- `(a,a,-a)`,
- `(-a,-a,a)`,
- `(-a,-a,-a)`,

where `a = 1/sqrt(3)`.

Since `h=H` on `x'=y'`, the function `h` also has exactly these four zeros on
that primed great circle.

This is the "only four zeros" fact that drives the contradiction.

## 6. The unprimed zero circles force two antipodal pairs

Now return to the six **unprimed** zero circles, on which `h` is already known
to vanish.

Write:

- `C_xy  : x = y`
- `C_xz  : x = z`
- `C_yz  : y = z`
- `C_xmy : x = -y`
- `C_xmz : x = -z`

and set

- `u = (a,a,a)`, `-u = (-a,-a,-a)`
- `v = (a,-a,-a)`, `-v = (-a,a,a)`

where `a = 1/sqrt(3)`.

Then:

- `C_xy ∩ C_xz = C_xy ∩ C_yz = C_xz ∩ C_yz = {u,-u}`
- `C_xmy ∩ C_xmz = {v,-v}`

Also, any two distinct great circles meet in exactly one antipodal pair.

### 6.1 First antipodal pair

The three unprimed circles

- `x=y`,
- `x=z`,
- `y=z`

all meet in the antipodal pair

- `u = (a,a,a)`,
- `-u = (-a,-a,-a)`.

Since `h` vanishes on each of those circles, both `u` and `-u` are zero points
of `h`.

If the primed circle `x'=y'` did **not** pass through `u` and `-u`, then it
would intersect each of the three circles `x=y`, `x=z`, `y=z` in an antipodal
pair distinct from `u,-u`.

These three antipodal pairs must also be distinct from each other. For if two
of them were the same, then `x'=y'` would pass through a point lying in the
intersection of two of the circles `C_xy`, `C_xz`, `C_yz`, and every such
intersection is exactly `{u,-u}`. That would contradict the assumption that
`x'=y'` misses `u,-u`.

That would create six zero points of `h` on `x'=y'`, contradicting the fact
that `h` has only four zeros there.

Therefore the primed circle `x'=y'` must pass through `u` and `-u`.

### 6.2 Second antipodal pair

Similarly, the two unprimed circles

- `x = -y`,
- `x = -z`

meet in the antipodal pair

- `v = (a,-a,-a)`,
- `-v = (-a,a,a)`.

Again `h(v)=h(-v)=0`.

If `x'=y'` did **not** pass through `v` and `-v`, then its intersections with
the circles `x=-y` and `x=-z` would each contribute an antipodal pair of zeros.
These two pairs are distinct from each other, because otherwise `x'=y'` would
pass through a point of

`C_xmy ∩ C_xmz = {v,-v}`,

contrary to assumption.

They are also distinct from `{u,-u}`, because neither `u` nor `-u` lies on
`x=-y` or `x=-z`.

So together with the already-forced pair `{u,-u}`, the circle `x'=y'` would
carry at least three distinct antipodal zero pairs, i.e. at least six zeros.

So the primed circle `x'=y'` must also pass through `v` and `-v`.

## 7. Uniqueness of the great circle through those four points

We have now shown that the primed great circle `x'=y'` passes through the four
points

- `(a,a,a)`,
- `(-a,-a,-a)`,
- `(a,-a,-a)`,
- `(-a,a,a)`.

But there is only one great circle containing all four of them:

`y = z`.

Why? A great circle is the intersection of the sphere with a plane through the
origin. The points `u=(a,a,a)` and `v=(a,-a,-a)` span the plane `y=z`, and the
antipodes `-u,-v` lie in the same plane. So the unique great circle through
those four points is precisely the circle `y=z`.

Therefore the primed circle `x'=y'` must in fact be the same geometric circle
as the unprimed circle `y=z`.

## 8. The contradiction

But `h` vanishes identically on the unprimed circle `y=z`, because that is one
of the six unprimed symmetry circles.

So if `x'=y'` is the same circle as `y=z`, then `h` must vanish at **every**
point of `x'=y'`.

That contradicts Section 5 above, where we proved that on `x'=y'`, the function
`h` agrees with the nonzero saddle `H` and therefore has exactly four zeros.

Hence the assumption that `h` is nonzero is impossible.

So

`h = 0`

identically, which means

`f = g`.

Therefore `f` is quadratic, proving Gleason's theorem in dimension `3`.

## 9. Status of this reconstruction

This is the clearest current local version of the final contradiction, and the
great-circle intersection logic is now internal to the note rather than living
only in a separate supporting file.

What is now strong:

1. the primed extrema reduction,
2. the frame-relative reuse of the comparison claim,
3. the four-zero analysis on `x'=y'`,
4. the six-zero-circle forcing argument,
5. the geometric uniqueness of the final great circle.

What still deserves honesty:

1. this note still leans on the source paper's comparison claim from Section 7,
   though we have unpacked it substantially elsewhere,
2. the zero-counting argument is now clear, but it is still best understood as
   a faithful reconstruction of Cooke's endgame rather than a completely new
   proof strategy.

Still, at this point the remaining gap is very small. The endgame is no longer
opaque; it is a concrete geometric rigidity argument.
