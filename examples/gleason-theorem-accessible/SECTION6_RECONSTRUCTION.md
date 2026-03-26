# Reconstructing Section 6: extremal values are attained

This note rebuilds Section 6 of Cooke--Keane--Moran in a more explicit way.

Its purpose is to shrink what had been the largest remaining imported block in
our proof record: the claim that bounded frame functions attain their
extremal values.

Source:
[Cooke--Keane--Moran, "An elementary proof of Gleason's theorem"](https://rogermcooke.net/rogermcooke_files/Elementary%20Proof%20of%20Gleasons%20Theorem.pdf), pages 125--127.

For the compactness and closure bookkeeping used below, see also
[SECTION6_TOPOLOGY_APPENDIX.md](C:\Users\xliup\OneDrive\Documents\codex\researchinsleep\examples\gleason-theorem-accessible\SECTION6_TOPOLOGY_APPENDIX.md).

## 1. The goal

Let `f` be a bounded frame function on the sphere `S`, and let

`M = sup_{s in S} f(s)`.

We want to prove that there exists a point `p in S` such that

`f(p) = M`.

The same argument applied to `-f` then gives attainment of the infimum.

## 2. Start with an almost-maximizing sequence

Choose a sequence `p_n in S` such that

`f(p_n) -> M`.

Because the sphere `S` is compact, some subsequence converges. Passing to that
subsequence, we may assume

`p_n -> p`

for some `p in S`.

By switching hemispheres if needed, we may also assume all `p_n` lie in the
northern hemisphere `N` determined by `p`.

So now the whole problem is:

- the points `p_n` approach `p`,
- the values `f(p_n)` approach `M`,
- prove `f(p)=M`.

## 3. Step 1: change coordinates so each `p_n` becomes the north pole

Choose and fix a point `e_0` on the equator `E` orthogonal to `p`.
Let `C_0` be the great-circle segment from `p` to `e_0`.

For each `n`, let `rho_n : S -> S` be a rigid motion of the sphere such that:

1. `rho_n(p) = p_n`,
2. `rho_n(c_n) = p`

for some point `c_n in C_0`.

Geometrically: rotate the sphere so that the old north pole `p` moves to
`p_n`, while a point `c_n` on the fixed meridian `C_0` rotates into `p`.

Because `p_n -> p`, these auxiliary points satisfy

`c_n -> p`.

Now define a new sequence of frame functions:

`g_n(s) = f(rho_n(s))`.

Each `g_n` is again a frame function, since rigid motions preserve orthogonality.

The key properties are:

1. `g_n(p) = f(p_n) -> M`,
2. `sup g_n = M` for every `n`,
3. `inf g_n = inf f = m` for every `n`,
4. `g_n(c_n) = f(p)` for every `n`.

So each `g_n` has almost-maximal value at the common north pole `p`, and at the
nearby point `c_n` it records the fixed value `f(p)` that we want to prove is
equal to `M`.

## 4. Step 2: symmetrize around the north pole

Let `hat_p` denote the rotation of the sphere by `90` degrees around the axis
through `p`.

Define

`h_n(s) = g_n(s) + g_n(hat_p s)`.

Again each `h_n` is a frame function.

The point of this symmetrization is that it forces the equator to become flat.

### 4.1 Why `h_n` is constant on the equator

Take any equatorial point `e`. The two points `e` and `hat_p e` lie on the
equator and are orthogonal.

Complete them with the north pole `p` to an orthonormal triple:

`(p,e,hat_p e)`.

By the frame-function rule,

`g_n(e) + g_n(hat_p e) = w(g_n) - g_n(p)`,

and the right-hand side is independent of `e`.

So

`h_n(e) = g_n(e) + g_n(hat_p e)`

is constant on the equator.

This is the key reason for introducing `h_n`.

### 4.2 Basic bounds for `h_n`

From the bounds on `g_n`, we get:

1. `sup h_n <= 2M`,
2. `inf h_n >= 2m`,
3. `h_n(p) = g_n(p) + g_n(hat_p p) = 2 g_n(p) -> 2M`.

The last identity uses `hat_p p = p`.

### 4.3 The crucial value at `c_n`

Because `rho_n(c_n)=p`,

`g_n(c_n)=f(p)`.

Also `hat_p c_n` lies on the equator orthogonal to `c_n` after transport, and
the source paper records the estimate

`h_n(c_n) <= M + f(p)`.

This is immediate from

- `g_n(c_n)=f(p)`,
- `g_n(hat_p c_n) <= M`.

So:

`h_n(c_n) <= M + f(p)` for every `n`.

This is the inequality that will eventually force `f(p)` up to `M`.

## 5. Step 3: take a compactness limit

Each `h_n` is a function from `S` into the compact interval `[2m,2M]`.

View the sequence `(h_n)` as living in the product space

`[2m,2M]^S`.

Under the product topology, this space is compact. So `(h_n)` has an
accumulation point; call one such limit `h`.

The paper notes three properties of this limit:

1. `h(p)=2M=sup h`,
2. `h` is constant on the equator,
3. `h` is still a frame function, because the set of frame functions is closed
   in the product space.

The first item comes from:

- `h_n(p) -> 2M`,
- `sup h_n <= 2M`.

The second comes from the fact that each `h_n` is constant on the equator.

The third is a closure statement: the defining frame equations are preserved
under pointwise limits.

Now Section 5 applies to `h`: since `h` attains its supremum at `p` and is
constant on the equator, the special-case theorem tells us that `h` has the
explicit quadratic form

`h(s) = a + (2M-a) cos^2(angle(p,s))`

for some constant equatorial value `a`.

In particular, `h` is continuous.

That continuity is the only new feature we need from the limit.

## 6. Step 4: push the limiting information back to `f(p)`

Choose `epsilon > 0`.

Because `h` is continuous and `h(p)=2M`, we can choose a point `c` on the
fixed meridian `C_0` so close to `p` that

`h(c) > 2M - epsilon`.

Since `h_n` accumulates to `h`, pass to a subsequence `h_{n_j}` such that

`h_{n_j}(c) -> h(c)`.

So for large `j`,

`h_{n_j}(c) > 2M - epsilon`.

Now compare `c_{n_j}` to `c`.

Both points lie on the same meridian `C_0`, and since `c_{n_j} -> p`, for large
`j` we can reach `c` from `c_{n_j}` in two descent steps. This is the easiest
case of the geometric lemma.

Apply the **approximate basic lemma** to `h_{n_j}`. Because `h_{n_j}(p)` is
very close to `2M`, moving down those two descent steps can reduce the value by
at most a very small error. Writing

`delta_n > 2M - h_n(p) -> 0`,

the paper gets:

`h_n(c_n) > h_n(c) - 2 delta_n`

for sufficiently large `n`.

Passing to the subsequence `n_j`, we obtain

`liminf h_{n_j}(c_{n_j}) >= liminf (h_{n_j}(c) - 2 delta_{n_j}) > 2M - epsilon`.

But from Section 4.3 we always have

`h_{n_j}(c_{n_j}) <= M + f(p)`.

Therefore

`M + f(p) > 2M - epsilon`.

So

`f(p) > M - epsilon`.

Since `epsilon > 0` was arbitrary, it follows that

`f(p) = M`.

This proves that bounded frame functions attain their supremum.

Applying the same argument to `-f` proves attainment of the infimum.

## 7. Why this argument works

The proof has a beautiful structure:

1. move each almost-maximizer `p_n` back to a common north pole,
2. symmetrize to flatten the equator,
3. pass to a limit and apply the special-case theorem to get continuity,
4. push the near-maximal value back along short descent chains,
5. conclude the limiting point already had the maximal value.

So the proof of extremal attainment is not magic compactness alone. It uses the
special-case theorem as a rigidity principle for the limit of symmetrized
functions.

## 8. What this closes, and what remains

This note substantially shrinks the previously imported Section 6 block.

What is now explicit:

1. why the coordinate change is introduced,
2. why the symmetrized functions have flat equators,
3. why the compactness limit is useful,
4. how continuity of the limit is converted into `f(p)=M`.

What is still not fully rebuilt here:

1. the appendix cites standard compactness machinery rather than reproving it
   from scratch,
2. the pointwise-limit argument is now explicit, but still uses standard
   topological facts.

Those are much smaller imports than before. The main theorem is now supported
by a substantially more complete local reconstruction.
