# Step (i): Why `M' = -m'`

This note fills in Cooke's first reduction in the final contradiction.

## Setup

Assume `h` is a bounded frame function of weight `0` and is not identically zero.

Choose an orthogonal frame `(p',q',r')` with:

- `h(p') = M' = sup h`
- `h(r') = m' = inf h`
- `h(q') = alpha'`

Because `h` has weight `0`,

`M' + alpha' + m' = 0`.

Cooke's first step is to prove:

`M' = -m'`.

## Assume the contrary

Suppose

`m' > -M'`.

Then

`alpha' = -M' - m' < 0`.

So the middle value on the frame is negative.

## The great circle orthogonal to `p'`

Let `C_{p'}` be the great circle orthogonal to `p'`.

This circle contains both `q'` and `r'`.

Take any point `s` on `C_{p'}`. There is a unique point `t` on `C_{p'}` such that:

- `s ⟂ t`
- both `s` and `t` lie on `C_{p'}`

Likewise, `q' ⟂ r'` and both lie on `C_{p'}`.

Now property `P3` applies on that great circle:

`h(s) + h(t) = h(q') + h(r') = alpha' + m'`.

Since `m'` is the infimum of `h`, we know `h(t) >= m'`. Therefore

`h(s) <= alpha' + m' - m' = alpha'`.

So **every** point of the great circle `C_{p'}` has value at most `alpha'`.

And because `h(q') = alpha'`, this shows:

> `alpha'` is the maximum value of `h` on the great circle orthogonal to `p'`.

This is the key hidden step in Cooke's sentence "by P3, `alpha'` is the maximal value of `h` on the great circle orthogonal to `p'`."

## Why that gives a contradiction

Under the assumption `alpha' < 0`, the entire great circle `C_{p'}` has strictly negative values.

But from the earlier part of the proof, `h` is already known to vanish on the six unprimed symmetry circles:

- `x=y`
- `x=-y`
- `x=z`
- `x=-z`
- `y=z`
- `y=-z`

Now consider the unprimed great circle `x=y`.

There are two possibilities:

1. `C_{p'}` is exactly the circle `x=y`.
2. `C_{p'}` is a different great circle.

In case 1, since `h` vanishes on `x=y`, we get points of `C_{p'}` where `h=0`, contradicting the claim that every point of `C_{p'}` has value at most `alpha'<0`.

In case 2, any two distinct great circles on the sphere intersect in exactly two antipodal points. Since `h=0` on `x=y`, those two intersection points are zeros of `h` lying on `C_{p'}`. Again this contradicts the fact that every point of `C_{p'}` has value at most `alpha'<0`.

So the assumption `m' > -M'` is impossible.

## Reverse inequality

Apply exactly the same argument to `-h`.

Then the roles of maximum and minimum are exchanged, and we conclude that

`m' < -M'`

is also impossible.

Therefore the only possibility is

`M' = -m'`.

## Why this matters

This closes Cooke's step (i).

Once `M'=-m'` is known, the weight-zero identity immediately gives

`alpha' = 0`,

which is Cooke's step (ii).
