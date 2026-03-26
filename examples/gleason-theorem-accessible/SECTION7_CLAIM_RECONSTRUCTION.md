# Reconstructing the Section 7 comparison claim

This note gives a more explicit reconstruction of the Section 7 comparison
claim in Cooke--Keane--Moran.

The claim says that once a bounded frame function `f` is compared with the
quadratic function `g` built from its extremal values, the difference

`h = g - f`

must vanish on six symmetry great circles.

The present version is stronger than our earlier note because it uses one
uniform template for all six circles:

1. derive two quarter-turn cancellation rules,
2. give an explicit odd-length word in those quarter-turns for each circle,
3. conclude `h(s)=0` from evenness.

That makes the proof much closer to a full line-by-line argument.

## 1. The setup

Fix an orthonormal frame `(p,q,r)` and write `(x,y,z)` for coordinates with
respect to that frame.

Let `f` be a bounded frame function and define

- `M = f(p)`,
- `alpha = w(f) - M - m`,
- `m = f(r)`.

Let

`g(x,y,z) = M x^2 + alpha y^2 + m z^2`,

and set

`h = g - f`.

Then `h` is a bounded frame function and, by construction,

- `h(p)=0`,
- `h(q)=0`,
- `h(r)=0`.

The goal is to prove that `h=0` on the six great circles

- `x = y`,
- `x = z`,
- `y = z`,
- `x = -y`,
- `x = -z`,
- `y = -z`.

## 2. The two quarter-turn operators

Define two `90` degree rotations:

- `A(x,y,z) = (x,-z,y)`,
- `B(x,y,z) = (-y,x,z)`.

Geometrically:

- `A` is the quarter-turn about the `x`-axis,
- `B` is the quarter-turn about the `z`-axis.

These are exactly the operators used in our symbolic checks in
[proof_checks.py](C:\Users\xliup\OneDrive\Documents\codex\researchinsleep\examples\gleason-theorem-accessible\proof_checks.py).

## 3. The two cancellation rules

The two identities are now isolated and proved in:

- [SECTION7_CANCELLATION_IDENTITIES.md](C:\Users\xliup\OneDrive\Documents\codex\researchinsleep\examples\gleason-theorem-accessible\SECTION7_CANCELLATION_IDENTITIES.md)

They state:

- `f(s) + f(A s) = g(s) + g(A s)`,
- `f(s) + f(B s) = g(s) + g(B s)`.

Subtracting from the corresponding identities for `g`, we obtain the two basic
rules for `h`:

- `h(A s) = - h(s)`,
- `h(B s) = - h(s)`.

These are the only algebraic rules we need.

Since `h` is a frame function, it is even:

`h(-s) = h(s)`.

## 4. A uniform word lemma

Let `W = L_1 L_2 ... L_k` be a word in the letters `A` and `B`, and interpret
it as left-to-right composition:

`W(s) = L_k(...(L_2(L_1(s)))...)`.

Then repeated use of the two cancellation rules gives

`h(W(s)) = (-1)^k h(s)`.

This is proved by induction on `k`:

1. for `k=1`, it is exactly one of the two basic rules,
2. if it holds for a word `W`, then for `L in {A,B}`,
   `h(L(W(s))) = -h(W(s)) = -(-1)^k h(s) = (-1)^{k+1} h(s)`.

Therefore:

If `W` has odd length and `W(s) = -s`, then

`h(s) = h(-s) = h(W(s)) = -h(s)`,

so

`h(s)=0`.

This is the master principle for all six circle cases.

## 5. The six explicit words

The remaining task is to give, for a point on each symmetry circle, one
odd-length word `W` in `A,B` such that `W(s)=-s`.

These words were checked symbolically in
[SECTION7_ORBIT_WORD_TABLE.md](C:\Users\xliup\OneDrive\Documents\codex\researchinsleep\examples\gleason-theorem-accessible\SECTION7_ORBIT_WORD_TABLE.md),
with
[proof_checks.py](C:\Users\xliup\OneDrive\Documents\codex\researchinsleep\examples\gleason-theorem-accessible\proof_checks.py)
serving as symbolic corroboration.

### 5.1 The circle `x = y`

Take

`s = (x,x,z)`.

Then the word

`W = BAA`

has odd length `3` and satisfies

`W(s) = -s`.

So `h(s)=0`.

### 5.2 The circle `x = z`

Take

`s = (x,y,x)`.

Then the word

`W = ABBBA`

has odd length `5` and satisfies

`W(s) = -s`.

So `h(s)=0`.

### 5.3 The circle `y = z`

Take

`s = (x,y,y)`.

Then the word

`W = BBA`

has odd length `3` and satisfies

`W(s) = -s`.

So `h(s)=0`.

### 5.4 The circle `x = -y`

Take

`s = (x,-x,z)`.

Then the word

`W = AAB`

has odd length `3` and satisfies

`W(s) = -s`.

So `h(s)=0`.

### 5.5 The circle `x = -z`

Take

`s = (x,y,-x)`.

Then the word

`W = ABA`

has odd length `3` and satisfies

`W(s) = -s`.

So `h(s)=0`.

### 5.6 The circle `y = -z`

Take

`s = (x,y,-y)`.

Then the word

`W = ABB`

has odd length `3` and satisfies

`W(s) = -s`.

So `h(s)=0`.

## 6. The full comparison claim

Combining the six cases, we obtain:

`h = 0`

on all six symmetry great circles

- `x = y`,
- `x = z`,
- `y = z`,
- `x = -y`,
- `x = -z`,
- `y = -z`.

Equivalently,

`f = g`

on those six circles.

This is exactly the Section 7 comparison claim needed later in the proof.

## 7. Why this matters

This claim is the bridge from the quadratic comparison function to the final
rigidity argument.

Once `h` vanishes on these six circles:

1. the extremal reduction can force constraints using unavoidable great-circle
   intersections,
2. the same claim can be reused in the primed frame,
3. the endgame becomes a geometric contradiction about zero sets on one great
   circle.

So this is one of the decisive mechanisms in the whole proof.

## 8. Status

This note is now much closer to a fully closed local proof of the Section 7
claim than the earlier version.

What is explicit:

1. the quarter-turn operators,
2. the two cancellation rules,
3. the odd-word lemma,
4. one explicit odd word for each of the six circles.

What is still imported:

1. the cancellation-rule note still depends on the Section 5 special-case
   theorem,
2. the exact orbit words are now recorded in
   [SECTION7_ORBIT_WORD_TABLE.md](C:\Users\xliup\OneDrive\Documents\codex\researchinsleep\examples\gleason-theorem-accessible\SECTION7_ORBIT_WORD_TABLE.md),
   while
   [proof_checks.py](C:\Users\xliup\OneDrive\Documents\codex\researchinsleep\examples\gleason-theorem-accessible\proof_checks.py)
   remains a corroboration tool.

Those are now small imports. The main logical structure of the comparison claim
is locally explicit.
