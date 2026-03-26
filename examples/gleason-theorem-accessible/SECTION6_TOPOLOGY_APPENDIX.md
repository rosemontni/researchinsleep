# Section 6 topology appendix

This appendix tightens the remaining topological bookkeeping inside
[SECTION6_RECONSTRUCTION.md](C:\Users\xliup\OneDrive\Documents\codex\researchinsleep\examples\gleason-theorem-accessible\SECTION6_RECONSTRUCTION.md).

The goal is modest but important:

1. make the compactness step explicit,
2. make the closure-of-frame-functions step explicit,
3. make the final two-step transfer estimate explicit enough that Section 6 is
   no longer carrying a vague topological import.

## 1. Compactness of the ambient function space

Let `I = [2m,2M]`, a compact interval in `R`.

Consider the product space

`X = I^S`,

the set of all functions from the sphere `S` to `I`, equipped with the product
topology.

By Tychonoff's theorem, an arbitrary product of compact spaces is compact.
Since each factor `I` is compact, `X` is compact.

So any sequence of functions `h_n : S -> I` has at least one accumulation point
in `X`. Concretely, that means there exists `h in X` and a subnet, or in the
present sequential setting a suitably chosen diagonal subsequence on a countable
dense set, whose values converge pointwise to `h`.

For the purposes of the Cooke proof, pointwise accumulation is enough.

## 2. Why the limit stays a frame function

Fix an orthonormal triple `(a,b,c)` on the sphere.

For every `n`, the frame-function rule gives

`h_n(a) + h_n(b) + h_n(c) = w(h_n)`.

In the Section 6 setup, all `h_n` have the same weight, because:

`h_n = g_n + g_n o hat_p`

and each `g_n` is a rigid motion of the same frame function `f`, so

`w(h_n) = 2 w(f)`.

Now let `h` be a pointwise limit of a convergent subsequence `h_{n_j}`.
Taking limits in the displayed equality gives

`h(a) + h(b) + h(c) = 2 w(f)`.

Since the triple `(a,b,c)` was arbitrary, `h` is itself a frame function.

So the set of frame functions of the relevant fixed weight is closed under the
pointwise convergence used in Section 6.

## 3. Why the equator stays flat in the limit

For each `n`, the function `h_n` is constant on the equator `E`.

That means:

for any `e,e' in E`,

`h_n(e) = h_n(e')`.

Passing to the pointwise limit gives

`h(e) = h(e')`.

So the limiting function `h` is also constant on the equator.

This justifies the direct application of the Section 5 special-case theorem to
the limit function.

## 4. Why `h(p)=2M`

For every `n`,

`h_n(p) = 2 g_n(p) = 2 f(p_n)`.

Since `f(p_n) -> M`, we get

`h_n(p) -> 2M`.

Also every `h_n` takes values in `[2m,2M]`, so any pointwise limit `h` still
takes values in that interval. Therefore

- `h(p)=2M`,
- `sup h <= 2M`.

Hence

`h(p)=sup h = 2M`.

This is the exact hypothesis needed to invoke the Section 5 theorem.

## 5. The final two-step transfer estimate

The last delicate point in Section 6 is the estimate

`h_n(c_n) > h_n(c) - 2 delta_n`

where `delta_n > 2M - h_n(p)` and `delta_n -> 0`.

Here is the clean reason.

Choose `c` on the fixed meridian `C_0` very close to `p`, and let `c_n -> p`
along the same meridian.

For large `n`, we can arrange the points on `C_0` in the order

`p, c_n, d_n, c`,

where:

1. `d_n` lies on the descent circle of `c_n`,
2. `c` lies on the descent circle of `d_n`.

So `c` is reached from `c_n` by exactly two descent steps.

Now apply the approximate basic lemma to `h_n`.
Because

`h_n(p) > 2M - delta_n`,

and because `h_n` is constant on the equator, the approximate basic lemma says
that one descent step can lower the value by at most `delta_n`.

Therefore:

- from `c_n` to `d_n`, the drop is at most `delta_n`,
- from `d_n` to `c`, the drop is at most `delta_n`.

Adding the two inequalities gives

`h_n(c_n) > h_n(c) - 2 delta_n`.

This is exactly the estimate used at the end of Section 6.

## 6. What this improves

With this appendix in place, the remaining imports in Section 6 are now much
smaller:

1. Tychonoff compactness is cited explicitly instead of being hand-waved,
2. closure of frame functions under the chosen pointwise limit is explicit,
3. the transfer estimate is written as a literal two-step application of the
   approximate basic lemma.

So Section 6 is now much closer to being locally closed.
