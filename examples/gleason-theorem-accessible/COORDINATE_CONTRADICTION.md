# Coordinate Contradiction For The Error Function

This note unpacks the last contradiction in the full proof at a more explicit coordinate level.

We start from the point where the proof has already shown:

- `h = g - f` is a frame function of weight `0`
- `h` vanishes on the six great circles
  - `x = y`
  - `x = -y`
  - `x = z`
  - `x = -z`
  - `y = z`
  - `y = -z`

and we want to prove that `h` must be identically zero.

Important honesty note:

- this note is a close reconstruction of Cooke's final contradiction
- the overall logic is faithful
- but some intersection-counting details are still presented at a guided-exposition level rather than as a fully formalized standalone proof

## 1. Assume `h` is not zero

Suppose `h` is not identically zero.

Then `h` has:

- a maximum `M'`
- a minimum `m'`
- an intermediate value `alpha'`

on some orthogonal frame `(p', q', r')`.

Use coordinates `(x',y',z')` adapted to that frame.

The same general argument used earlier for `f` can now be applied to `h`.

## 2. First reduction: the extrema are opposite

Because `h` has weight `0`, the values on an orthogonal frame add to `0`:

`M' + alpha' + m' = 0`.

Cooke first proves that actually

`M' = -m'`.

Why?

If `m' > -M'`, then `alpha' < 0`.

At this point Cooke invokes the earlier special-case analysis: in that situation, the middle value `alpha'` is the largest value of `h` on the great circle orthogonal to `p'`.

So the entire great circle orthogonal to `p'` would have values strictly below `0`.

But one of the known zero circles must intersect that great circle in at least two points, and at those intersection points `h=0`.

That contradicts the claim that the whole great circle is stuck below `0`.

Running the same argument with `-h` rules out `m' < -M'`.

So only

`M' = -m'`

is possible.

Then automatically:

`alpha' = 0`.

This is exactly Cooke's step (i).

## 3. Second reduction: the middle value is zero

Once `M'=-m'` is known and `h` has weight `0`, we have

`M' + alpha' + m' = 0`,

so automatically

`alpha' = 0`.

This is Cooke's step (ii).

## 4. Third reduction: the natural comparison function for `h` is the saddle

Since the top and bottom values are opposite and the middle value is zero, the corresponding quadratic comparison function becomes

`H(x',y',z') = M'(x'^2 - z'^2)`.

The crucial point is not that we have already proved `h=H` globally.

What we do know is that the earlier six-circle claim can now be reapplied to `h`, using the primed frame `(p',q',r')` and this comparison function `H`.

So on each of the six primed-coordinate great circles

- `x'=y'`
- `x'=-y'`
- `x'=z'`
- `x'=-z'`
- `y'=z'`
- `y'=-z'`

the function `h` agrees with the saddle comparison function `H`.

That is the exact amount of information needed for Cooke's final contradiction.

This is Cooke's step (iii).

## 5. Zero set of the saddle on the circle `x' = y'`

Now look at the great circle

`x' = y'`.

On the unit sphere, points on this circle have the form

`(t, t, z')`

with

`2t^2 + z'^2 = 1`.

For the saddle

`H(x',y',z') = M'(x'^2 - z'^2)`,

the zero condition is

`x'^2 = z'^2`.

Since also `x' = y'`, we get

`x'^2 = y'^2 = z'^2`.

So the only zero points on the circle `x' = y'` are the four sign patterns

- `(a, a, a)`
- `(a, a, -a)`
- `(-a, -a, a)`
- `(-a, -a, -a)`

where `a = 1/sqrt(3)`.

This is exactly what Cooke records.

Since `h=H` on the primed great circle `x'=y'`, it follows that `h` also vanishes there at exactly those four points.

## 6. The fixed zero circles force four specific geometric zero points

Now return to the six original zero circles in the original, unprimed coordinates.

Let

- `u = (a,a,a)`
- `-u = (-a,-a,-a)`
- `v = (a,-a,-a)`
- `-v = (-a,a,a)`

where `a = 1/sqrt(3)`.

These points are special because:

- `u` and `-u` lie on all three circles `x=y`, `x=z`, and `y=z`
- `v` and `-v` lie on both circles `x=-y` and `x=-z`

Since `h` vanishes on each of those circles, we know:

- `h(u)=h(-u)=0`
- `h(v)=h(-v)=0`

This is a statement about geometric points on the sphere, not about the primed coordinates.

The pairwise intersection facts used here are checked symbolically in [proof_checks.py](C:\Users\xliup\OneDrive\Documents\codex\researchinsleep\examples\gleason-theorem-accessible\proof_checks.py).

## 7. Why the adapted circle must pass through those points

Now look at the adapted great circle

`C' := {x' = y'}`.

From step 4, if `h` were the nonzero saddle, then `h` could have exactly four zeros on `C'`.

Suppose `C'` did not pass through `u` and `-u`.

Any two distinct great circles intersect in exactly two antipodal points. Therefore `C'` would intersect each of the zero circles `x=y`, `x=z`, and `y=z` in two points.

These three zero circles share only the pair `u,-u`. Since we assumed `C'` does not pass through that pair, the six intersection points would all be different.

So `h` would have at least six zero points on `C'`, contradicting the four-zero description of the saddle on `C'`.

So `C'` must contain `u` and `-u`.

By the same reasoning, if `C'` did not pass through `v` and `-v`, then its intersections with the zero circles `x=-y` and `x=-z` would again create too many zeros on `C'`.

So `C'` must also contain `v` and `-v`.

## 8. The unique great circle through those four points

There is only one great circle containing the four geometric points

- `u`
- `-u`
- `v`
- `-v`

and that great circle is the unprimed circle

`y = z`.

Therefore the adapted circle `C'` must actually coincide with the already-known zero circle `y=z`.

So `h` vanishes at every point of `C'`.

This is the geometric core of Cooke's step (iv).

## 9. Final contradiction

This is impossible for the nonzero saddle

`H(x',y',z') = M'(x'^2 - z'^2)`,

because on the great circle `x' = y'` it has exactly four zero points, not the entire circle. Since `h=H` on that great circle, the same contradiction applies to `h`.

That four-point zero set on `x'=y'` is also checked symbolically in [proof_checks.py](C:\Users\xliup\OneDrive\Documents\codex\researchinsleep\examples\gleason-theorem-accessible\proof_checks.py).

So the assumption that `h` is nonzero must be false.

Hence

`h = 0`

everywhere.

Since `h = g - f`, we conclude:

`f = g`,

and so the original frame function is quadratic.

## 10. Why this is the last hard step

The contradiction is subtle because it combines:

- a coordinate description of the only possible nonzero error
- the previously proved symmetry zero circles
- an intersection-counting argument on great circles

This is exactly why the last step is harder than the special-case argument, even though it is still geometrically natural.

## 11. What is now explicit and what is still imported

This note now makes explicit:

- the four special geometric zero points
- the six-versus-four zero counting contradiction on `C'`
- the uniqueness of the great circle through those four points

What is still imported from earlier parts of the proof:

- the extremal argument forcing `M'=-m'` and `alpha'=0`
- the frame-relative six-circle claim, now applied in the primed frame

See [FRAME_RELATIVE_CLAIM.md](C:\Users\xliup\OneDrive\Documents\codex\researchinsleep\examples\gleason-theorem-accessible\FRAME_RELATIVE_CLAIM.md).
See also [SADDLE_REDUCTION.md](C:\Users\xliup\OneDrive\Documents\codex\researchinsleep\examples\gleason-theorem-accessible\SADDLE_REDUCTION.md).
Cooke's step (i) itself is unpacked in [STEP_I_EXTREMAL_REDUCTION.md](C:\Users\xliup\OneDrive\Documents\codex\researchinsleep\examples\gleason-theorem-accessible\STEP_I_EXTREMAL_REDUCTION.md).
