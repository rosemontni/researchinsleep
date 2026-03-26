# A stronger reconstruction of Section 5

This note tightens the most important remaining middle step in our proof
record: the special-case theorem in Section 5 of Cooke--Keane--Moran.

The goal is to make the logic here as explicit as possible without importing
physics, Hilbert-space formalism, or any machinery beyond the earlier basic
lemma, the geometric lemma, and the two warmup theorems.

## 1. The setup

Work on the unit sphere `S` in ordinary `3`-dimensional space. Fix a point
`p` that we call the north pole, and write

- `N = {s in S : angle(p,s) <= pi/2}` for the northern hemisphere,
- `E = {s in S : s ⟂ p}` for the equator,
- `l(s) = cos^2(angle(p,s))` for the latitude parameter.

Suppose `f` is a frame function such that:

1. `f(p) = M = sup f`,
2. `f(e) = m` for every `e in E`.

As in Cooke, first normalize to the nontrivial case `M != m`, then replace
`f` by

`(f - m)/(M - m)`.

So from now on we may assume

- `m = 0`,
- `M = 1`,
- `f(p) = 1`,
- `f(e) = 0` for every `e in E`.

The theorem to prove is then

`f(s) = l(s) = cos^2(angle(p,s))`

for every `s in N`, and hence for all `s in S` by symmetry.

## 2. Monotonicity by latitude

Take `s,t in N` with `l(s) > l(t)`.

The geometric lemma says that there is a finite chain

`s = s_0, s_1, ..., s_n = t`

in `N` such that each `s_i` lies on the descent great circle through
`s_{i-1}`. The basic lemma then applies at each step and gives

`f(s_{i-1}) >= f(s_i)`.

Chaining these inequalities yields

`f(s) >= f(t)`.

So the value of `f` can only go down as we move to lower latitudes.

This lets us define two one-variable envelope functions on `[0,1]`:

- `bar_f(l) = sup { f(s) : s in N, l(s) = l }`,
- `under_f(l) = inf { f(s) : s in N, l(s) = l }`.

The monotonicity above implies:

1. `bar_f(1) = under_f(1) = 1`,
2. `bar_f(0) = under_f(0) = 0`,
3. if `l < l'`, then `bar_f(l) <= under_f(l')`.

The third fact is the crucial separation property.

## 3. The exceptional set is at most countable

Define

`C = { l in [0,1] : bar_f(l) > under_f(l) }`.

We want to show that `C` is at most countable.

For each `l in C`, consider the open interval

`I_l = (under_f(l), bar_f(l))`.

Because `bar_f(l) > under_f(l)`, this is a nonempty interval.

Now take `l < l'`. By the separation property,

`bar_f(l) <= under_f(l')`.

So the intervals `I_l` and `I_{l'}` are disjoint.

Thus the family `{I_l : l in C}` is a family of pairwise disjoint nonempty
open intervals in `[0,1]`. Each such interval contains a rational number, and
different intervals contain different rationals. Since the rationals are
countable, `C` must also be countable.

This is the same conclusion as in Cooke, but the proof is especially clean:
the bad latitudes inject into `Q`.

## 4. Collapse to a single function

For `l in [0,1] \\ C`, define

`F(l) = bar_f(l) = under_f(l)`.

So `F` is now a well-defined function on `[0,1] \\ C`.

It satisfies the hypotheses of Warmup Theorem II:

1. `F(0) = 0`.
2. If `a < b` and `a,b notin C`, then `F(a) <= F(b)` by monotonicity.
3. If `a,b,c notin C` and `a+b+c=1`, then there is a frame
   `(q,q',q'')` with
   `l(q)=a`, `l(q')=b`, `l(q'')=c`.
   Since `f` is a frame function,
   `f(q)+f(q')+f(q'') = 1`,
   so `F(a)+F(b)+F(c)=1`.

Warmup Theorem II therefore gives

`F(l) = l`

for every `l in [0,1] \\ C`.

So on every nonexceptional latitude, all points already have the correct
quadratic value.

## 5. The exceptional set is actually empty

Cooke states this quickly. Here is the explicit argument.

Assume, for contradiction, that `l_0 in C`.

Because `C` is countable, its complement is dense in `[0,1]`. So we can choose
sequences

- `a_n notin C` with `a_n < l_0` and `a_n -> l_0`,
- `b_n notin C` with `b_n > l_0` and `b_n -> l_0`.

For every `n`, the separation property gives

`F(a_n) = a_n <= under_f(l_0) <= bar_f(l_0) <= F(b_n) = b_n`.

Let `n -> infinity`. We get

`l_0 <= under_f(l_0) <= bar_f(l_0) <= l_0`.

Hence

`under_f(l_0) = bar_f(l_0) = l_0`,

which contradicts `l_0 in C`.

Therefore `C` is empty.

So for every `l in [0,1]`,

`bar_f(l) = under_f(l) = l`.

That means every point at latitude `l` has value exactly `l`.

Equivalently,

`f(s) = l(s) = cos^2(angle(p,s))`

for every `s in N`.

## 6. What this gives us

This fully closes the one-variable part of the Section 5 argument:

- the geometric lemma and basic lemma force monotonicity,
- monotonicity creates upper and lower latitude envelopes,
- the bad set where they differ is countable,
- Warmup II identifies the common value on the complement,
- density of the complement forces the bad set to disappear.

So the special-case theorem is stronger than we previously wrote it:
once the geometric lemma and basic lemma are granted, the rest of the proof is
now explicit and elementary.

## 7. What still remains imported

This note does **not** rebuild every earlier ingredient from scratch.
It still depends on:

1. the basic lemma from Section 4,
2. the geometric lemma from the beginning of Section 5,
3. the frame-existence fact that for `a+b+c=1` there is a frame with those
   three latitude values.

But among the remaining gaps in our overall proof record, this closes one of
the biggest ones. The special-case theorem is no longer just a vague sketch:
its one-variable reduction and elimination of exceptional latitudes are now
fully spelled out.
