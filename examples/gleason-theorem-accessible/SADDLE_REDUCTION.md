# Saddle Reduction Without Overclaiming

This note explains the last imported step more carefully.

## The misconception to avoid

At one point in this project, the reconstruction drifted toward the stronger statement

> `h(x',y',z') = M'(x'^2-z'^2)` everywhere on the sphere.

That is stronger than what Cooke's proof actually needs at the last stage.

The cleaner and more faithful statement is:

> after the extremal reductions, the natural comparison function in the primed frame is the saddle
> `H(x',y',z') = M'(x'^2-z'^2)`,
> and the frame-relative six-circle claim shows that `h` agrees with `H` on the six primed-coordinate great circles.

That is enough for the contradiction.

## Step 1. Start with a nonzero weight-zero frame function

At the end of the proof we have:

- `h` is a bounded frame function
- the weight of `h` is `0`
- `h` is zero on the six unprimed symmetry circles

Assume `h` is not identically zero.

Choose an orthogonal frame `(p',q',r')` such that:

- `h(p') = M' = sup h`
- `h(r') = m' = inf h`
- `h(q') = alpha'`

## Step 2. Use the weight-zero condition

Since `h` has weight zero,

`M' + alpha' + m' = 0`.

Cooke's step (i) shows:

`M' = -m'`.

Then immediately:

`alpha' = 0`.

So in the primed frame the comparison data are exactly

- top value `M'`
- middle value `0`
- bottom value `-M'`

## Step 3. Build the primed comparison function

Now define the comparison function

`H(x',y',z') = M'(x'^2-z'^2)`.

This is the quadratic function that has exactly the required values on the primed frame:

- `H(1,0,0)=M'`
- `H(0,1,0)=0`
- `H(0,0,1)=-M'`

So `H` is the correct analogue of the earlier quadratic comparison function.

## Step 4. Reuse the six-circle claim in the primed frame

The earlier claim was always frame-relative:

- if a frame function and its comparison quadratic satisfy the quarter-turn sum identities relative to a chosen orthonormal frame, then they agree on the six equal-coordinate great circles for that frame

Apply that claim now to:

- the frame function `h`
- the comparison quadratic `H`
- the primed frame `(p',q',r')`

Then `h` and `H` agree on the six primed-coordinate great circles:

- `x'=y'`
- `x'=-y'`
- `x'=z'`
- `x'=-z'`
- `y'=z'`
- `y'=-z'`

This is the precise content that the final contradiction uses.

## Step 5. Why this is enough

The contradiction only needs one of those circles, namely `x'=y'`.

On that circle:

- `h = H`
- `H` has exactly four zero points

But the earlier unprimed zero-circle geometry forces the same primed circle to be an entire zero circle for `h`.

That is the contradiction.

So we do **not** need a global formula for `h`.

We only need:

- the primed comparison saddle `H`
- equality of `h` and `H` on the six primed symmetry circles

## Practical consequence

This closes a conceptual gap in the reconstruction:

- the proof no longer relies on an overstrong global saddle claim
- the endgame now matches the actual logic of Cooke's proof more closely

## Remaining dependency

What is still imported here is Cooke's step (i), the proof that `M'=-m'`.

Once that is granted, the rest of the saddle setup is straightforward:

- `alpha'=0` from weight zero
- `H` is the only natural quadratic comparison function
- the frame-relative six-circle claim can be reused in the primed frame

That step is now unpacked in [STEP_I_EXTREMAL_REDUCTION.md](C:\Users\xliup\OneDrive\Documents\codex\researchinsleep\examples\gleason-theorem-accessible\STEP_I_EXTREMAL_REDUCTION.md).
