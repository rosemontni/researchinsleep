# Endgame intersection lemma

This note tightens the highest-risk step identified in
[PROOF_AUDIT.md](C:\Users\xliup\OneDrive\Documents\codex\researchinsleep\examples\gleason-theorem-accessible\PROOF_AUDIT.md):
the zero-counting geometry in the final contradiction.

The goal is to make one point fully explicit:

If a great circle `C'` is forced to carry zeros from several unprimed symmetry
circles, then unless `C'` passes through the special shared antipodal pairs,
those intersections are distinct and create too many zeros.

This removes the soft phrase "too many zero constraints" and replaces it with a
clean case split.

## 1. The six unprimed symmetry circles

Write:

- `C_xy  : x = y`
- `C_xz  : x = z`
- `C_yz  : y = z`
- `C_xmy : x = -y`
- `C_xmz : x = -z`
- `C_ymz : y = -z`

All are great circles on the sphere.

The important shared antipodal pairs are:

- `u = (a,a,a)`, `-u = (-a,-a,-a)`, where `a = 1/sqrt(3)`
- `v = (a,-a,-a)`, `-v = (-a,a,a)`

and they satisfy:

- `C_xy ∩ C_xz = C_xy ∩ C_yz = C_xz ∩ C_yz = {u,-u}`
- `C_xmy ∩ C_xmz = {v,-v}`

## 2. Distinct great circles meet in one antipodal pair

Any two distinct great circles on the sphere are intersections of the sphere
with two distinct planes through the origin. Two distinct such planes meet in a
line through the origin, and that line meets the sphere in exactly one
antipodal pair.

So:

- if `C'` is a great circle different from `C_xy`, then `C' ∩ C_xy` is exactly
  one antipodal pair,
- similarly for each of the other symmetry circles.

## 3. Distinctness lemma for the first triple

Assume `C'` is a great circle that does **not** pass through `u` or `-u`.

Then the three intersection pairs

- `C' ∩ C_xy`
- `C' ∩ C_xz`
- `C' ∩ C_yz`

are three distinct antipodal pairs.

### Proof

Each intersection is a single antipodal pair because `C'` is distinct from each
of the three circles.

Suppose two of these pairs were equal, for example

`C' ∩ C_xy = C' ∩ C_xz`.

Then some point of `C'` lies in both `C_xy` and `C_xz`. But

`C_xy ∩ C_xz = {u,-u}`.

So `C'` would pass through `u` or `-u`, contrary to assumption.

The same argument works for the other pairs. Therefore the three intersection
pairs are distinct.

## 4. First consequence: `C'` must pass through `u,-u`

Now assume `h` vanishes on `C_xy`, `C_xz`, and `C_yz`, and assume also that on
the great circle `C'` the function `h` has only four zeros.

If `C'` did not pass through `u,-u`, then by the previous lemma the
intersections with `C_xy`, `C_xz`, and `C_yz` would give three distinct
antipodal pairs of zeros on `C'`.

That is already six distinct zeros on `C'`.

So any such `C'` must pass through `u` and `-u`.

## 5. Distinctness lemma for the second pair

Assume now that `C'` already passes through `u,-u`, and assume `C'` does
**not** pass through `v,-v`.

Then the two intersection pairs

- `C' ∩ C_xmy`
- `C' ∩ C_xmz`

are:

1. distinct from each other,
2. distinct from the pair `{u,-u}`.

### Proof

First, if the two intersection pairs were equal, then `C'` would pass through a
point in

`C_xmy ∩ C_xmz = {v,-v}`,

contrary to assumption.

Second, `u` and `-u` do not lie on either `C_xmy` or `C_xmz`, because

- `u=(a,a,a)` does not satisfy `x=-y`,
- `u=(a,a,a)` does not satisfy `x=-z`,

and similarly for `-u`.

So neither of the new intersection pairs can equal `{u,-u}`.

Therefore the two pairs are distinct from each other and from `{u,-u}`.

## 6. Second consequence: `C'` must pass through `v,-v`

Assume:

1. `C'` passes through `u,-u`,
2. `h` vanishes on `C_xmy` and `C_xmz`,
3. `h` has only four zeros on `C'`.

If `C'` did not pass through `v,-v`, then by Section 5 the intersections with
`C_xmy` and `C_xmz` would contribute two more distinct antipodal pairs of zeros
on `C'`, in addition to `{u,-u}`.

That yields at least six distinct zeros on `C'`.

So `C'` must also pass through `v,-v`.

## 7. Uniqueness of the great circle through those four points

Any great circle is determined by its underlying plane through the origin.

The points

- `u = (a,a,a)`
- `v = (a,-a,-a)`

span the plane `y=z`.

To see this, compute a normal vector:

`u × v = (0, 2a^2, -2a^2)`,

which is proportional to `(0,1,-1)`. So the plane through `u`, `v`, and the
origin is exactly

`y = z`.

Since `-u` and `-v` lie in the same plane, the unique great circle through all
four points is the symmetry circle

`C_yz : y = z`.

Thus any great circle passing through `u,-u,v,-v` must equal `C_yz`.

## 8. Application to the final contradiction

In the endgame we take

`C' = {x' = y'}`

in the primed frame.

On that circle, the primed saddle comparison shows that `h` has exactly four
zeros.

By Sections 4 and 6 above, `C'` must pass through `u,-u,v,-v`.
By Section 7, that forces

`C' = C_yz`.

But `h` vanishes identically on `C_yz`, because `C_yz` is one of the six
unprimed symmetry circles.

So `h` would vanish identically on `C'`, contradicting the fact that on `C'`
it agrees with the nonzero saddle and therefore has exactly four zeros.

This closes the geometric heart of the final contradiction.

## 9. Why this matters

This note removes the last major soft spot in the endgame reconstruction.

The contradiction is no longer:

- "somehow too many circles force too many zeros."

It is now:

1. if `C'` misses `{u,-u}`, it gets six zeros immediately,
2. once it contains `{u,-u}`, if it misses `{v,-v}`, it gets six zeros again,
3. so it must contain both pairs,
4. that forces `C' = C_yz`,
5. impossible because `h|_{C'}` cannot be both identically zero and a nonzero
   saddle restriction.
