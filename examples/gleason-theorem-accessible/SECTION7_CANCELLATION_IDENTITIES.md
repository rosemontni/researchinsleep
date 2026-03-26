# Section 7 cancellation identities

This note isolates the two cancellation identities used throughout the late
proof.

Before this note, the Section 7 comparison claim used the rules

- `h(A s) = -h(s)`
- `h(B s) = -h(s)`

but treated them as inherited from earlier symmetrization machinery. The goal
here is to make those identities explicit as a local lemma.

## 1. Setup

Fix the unprimed frame `(p,q,r)` and let

`g(x,y,z) = M x^2 + alpha y^2 + m z^2`

be the quadratic comparison function for the bounded frame function `f`.

Define

`h = g - f`.

Let the two quarter-turns be:

- `A(x,y,z) = (x,-z,y)`, the `90` degree rotation about the `p`-axis
- `B(x,y,z) = (-y,x,z)`, the `90` degree rotation about the `r`-axis

We want to prove:

1. `h(s) + h(A s) = 0`
2. `h(s) + h(B s) = 0`

for every point `s` on the sphere.

## 2. The `A`-identity

Define

`F_A(s) = f(s) + f(A s)`.

We claim that `F_A` falls into the Section 5 special-case theorem with north
pole `p`.

### 2.1 `F_A` is maximal at `p`

Since `f(p)=M` and `A p = p`,

`F_A(p) = f(p) + f(A p) = 2M`.

For any `s`, each term is at most `M`, so

`F_A(s) <= 2M = F_A(p)`.

Thus `F_A` attains its maximum at `p`.

### 2.2 `F_A` is constant on the equator orthogonal to `p`

Take any equatorial point `e` orthogonal to `p`.

Because `A` is the quarter-turn about the `p`-axis, the points

- `p`
- `e`
- `A e`

form an orthonormal triple.

Therefore, by the frame-function rule,

`f(e) + f(A e) = w(f) - f(p) = w(f) - M`,

which is independent of `e`.

So `F_A` is constant on the equator orthogonal to `p`.

### 2.3 Apply the Section 5 special-case theorem

Since `F_A` is a bounded frame function, maximal at `p`, and constant on the
equator orthogonal to `p`, Section 5 forces `F_A` to be the unique quadratic
frame function with those same pole/equator data.

Now define similarly

`G_A(s) = g(s) + g(A s)`.

The same reasoning shows:

1. `G_A` is also a bounded frame function,
2. `G_A(p)=2M`,
3. `G_A` is constant on the equator orthogonal to `p` with the same value
   `w(f)-M`.

So the Section 5 theorem gives:

`F_A(s) = G_A(s)`

for every `s`.

Thus:

`f(s) + f(A s) = g(s) + g(A s)`.

Subtracting from both sides yields:

`h(s) + h(A s) = 0`.

This is the first cancellation identity.

## 3. The `B`-identity

Now define

`F_B(s) = f(s) + f(B s)`.

The geometry is analogous, but now the distinguished axis is `r`, not `p`.

### 3.1 `F_B` is minimal at `r`

Since `f(r)=m` and `B r = r`,

`F_B(r) = 2m`.

For any `s`, each term is at least `m`, so

`F_B(s) >= 2m = F_B(r)`.

Thus `F_B` attains its minimum at `r`.

### 3.2 `F_B` is constant on the equator orthogonal to `r`

Take any point `e` orthogonal to `r`.

Because `B` is the quarter-turn about the `r`-axis, the points

- `r`
- `e`
- `B e`

form an orthonormal triple.

So:

`f(e) + f(B e) = w(f) - f(r) = w(f) - m`,

which is independent of `e`.

Hence `F_B` is constant on the equator orthogonal to `r`.

### 3.3 Apply the special-case theorem to `-F_B`

The Section 5 theorem is phrased for functions maximal at a pole, not minimal
there. So apply it to `-F_B`.

Then:

1. `-F_B` is maximal at `r`,
2. `-F_B` is constant on the equator orthogonal to `r`.

By the same reasoning as before, `-F_B` is uniquely determined by those data.

Now define

`G_B(s) = g(s) + g(B s)`.

Again:

1. `G_B` is a bounded frame function,
2. `G_B(r)=2m`,
3. `G_B` is constant on the equator orthogonal to `r` with value `w(f)-m`.

So `-G_B` has the same pole/equator data as `-F_B`.

Applying Section 5 to `-F_B` and `-G_B`, we get:

`F_B(s) = G_B(s)`

for every `s`.

Therefore:

`f(s) + f(B s) = g(s) + g(B s)`,

and hence

`h(s) + h(B s) = 0`.

This is the second cancellation identity.

## 4. Conclusion

We have proved the two identities used in Section 7:

1. `h(s) + h(A s) = 0`
2. `h(s) + h(B s) = 0`

equivalently:

1. `h(A s) = -h(s)`
2. `h(B s) = -h(s)`

These are exactly the rewrite rules used in
[SECTION7_CLAIM_RECONSTRUCTION.md](C:\Users\xliup\OneDrive\Documents\codex\researchinsleep\examples\gleason-theorem-accessible\SECTION7_CLAIM_RECONSTRUCTION.md).

## 5. Why this matters

This note closes one of the main remaining local imports in the late proof.

The six-circle claim no longer depends on unnamed inherited machinery. It now
depends on a clearly stated local lemma whose proof is visible and short:

1. symmetrize with a quarter-turn,
2. observe "max at pole + flat equator" or "min at pole + flat equator",
3. invoke the Section 5 theorem,
4. subtract the quadratic comparison function.
