# Reconstructing the Section 4 basic lemma

This note expands the proof of the basic lemma from Section 4 of
Cooke--Keane--Moran. The original proof is short and correct, but it compresses
two ideas that are worth making fully explicit:

1. why the equator value must equal the global infimum,
2. why orthogonality on one descent great circle compares two points by a
   single frame-function identity.

Throughout, `S` is the unit sphere in ordinary `3`-space, `p` is the north
pole, `N` is the northern hemisphere, and `E` is the equator.

## 1. The statement

Assume `f` is a frame function such that:

1. `f(p) = sup_{s in S} f(s)`,
2. `f(e)` has the same value for every `e in E`.

Then for every `s in N \\ {p}` and every `s'` on the descent great circle
`D_s`, we have

`f(s) >= f(s')`.

In words: once the north pole is the maximum and the equator is flat, values
can only go down as you move along a descent great circle away from the pole.

## 2. Why the equator value is the global minimum

Let

- `M = sup_{u in S} f(u) = f(p)`,
- `m = inf_{u in S} f(u)`.

Let `c` be the common value of `f` on the equator `E`.

We already know `m <= c`, because `m` is the global infimum.

To prove the reverse inequality, use property `P4` from the paper:

If `f(s) > M - xi`, then there exists a point `t ⟂ s` such that

`f(t) < m + xi`.

Apply this with `s = p`. Since `f(p) = M`, the hypothesis holds for every
`xi > 0`. So for every `xi > 0`, there exists `t ⟂ p` with

`f(t) < m + xi`.

But `t ⟂ p` means exactly `t in E`, and all equatorial points have value `c`.
So for every `xi > 0`,

`c < m + xi`.

Letting `xi -> 0`, we get `c <= m`.

Together with `m <= c`, this gives

`c = m`.

So the equator is not merely constant: it is the bottom value of the whole
frame function.

## 3. The geometry of a descent circle

Fix `s in N \\ {p}`, and let `D_s` be its descent great circle. By definition,
`D_s` is the great circle through `s` whose northernmost point is `s`.

Now take any `s' in D_s`.

Because `D_s` is a great circle, it behaves like an ordinary circle. On that
circle:

1. there is a unique point `t in D_s` with `t ⟂ s`,
2. there is a unique point `t' in D_s` with `t' ⟂ s'`.

The key observation is that `t` lies on the equator.

Why? The descent circle `D_s` was chosen so that `s` is its northernmost
point. Moving a quarter-turn along that circle from `s` lands exactly at
latitude `0`, which is the equator. So the point on `D_s` orthogonal to `s`
is an equatorial point.

Hence

`t in E`,

and therefore, by the previous section,

`f(t) = m`.

The point `t'` need not lie on the equator, but of course

`f(t') >= m`

because `m` is the global infimum.

## 4. The frame-function identity

All four points `s,t,s',t'` lie on the same great circle `D_s`, and we chose
them so that

- `s ⟂ t`,
- `s' ⟂ t'`.

Property `P3` from the paper says:

If four points lie on the same great circle and come in two orthogonal pairs,
then the sums of the frame-function values on those pairs are equal.

So here we have

`f(s) + f(t) = f(s') + f(t')`.

Substitute `f(t)=m`:

`f(s) + m = f(s') + f(t')`.

Rearrange:

`f(s) - f(s') = f(t') - m`.

Since `f(t') >= m`, the right-hand side is nonnegative. Therefore

`f(s) - f(s') >= 0`,

so

`f(s) >= f(s')`.

That is exactly the basic lemma.

## 5. The approximate version

Cooke also records an approximate form. It says:

If `xi > 0` and

1. `f(p) > sup_{u != p} f(u) - xi`,
2. `f(e)` is constant on the equator,

then for every `s in N \\ {p}` and every `s' in D_s`,

`f(s) > f(s') - xi`.

The proof is the same, with one softened estimate.

As above, property `P4` now shows that every equatorial point satisfies

`f(e) < m + xi`.

Using the same points `t,t'` and the same identity from `P3`,

`f(s) - f(s') = f(t') - f(t)`.

Since `t in E`, we have `f(t) < m + xi`, while `f(t') >= m`. Therefore

`f(s) - f(s') > m - (m + xi) = -xi`,

which is equivalent to

`f(s) > f(s') - xi`.

So the approximate version really is just the same argument with a slightly
blurred lower bound on the equator.

## 6. Why this matters for the whole proof

This lemma is the engine behind the special-case theorem in Section 5.
It turns the geometric notion of "descent" into a one-sided inequality:

- higher-latitude points dominate lower points along a descent circle,
- chaining descents gives monotonicity by latitude,
- monotonicity lets the proof collapse from a function on the sphere to a
  function of one variable.

So once this lemma and the geometric chaining lemma are in place, the rest of
Section 5 becomes a one-variable argument.

## 7. What remains imported

This reconstruction still uses:

1. property `P3`,
2. property `P4`,
3. the geometric definition of the descent circle `D_s`.

But it removes the hidden steps inside the proof itself. In particular, the
equator-minimum identification is now fully explicit.
