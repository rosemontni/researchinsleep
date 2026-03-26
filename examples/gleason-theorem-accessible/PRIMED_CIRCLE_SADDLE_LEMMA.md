# Primed circle saddle lemma

This note isolates one small but important inference used in the late proof:

If the primed comparison saddle agrees with `h` on the primed circle

`C' = {x' = y'}`,

and if `h` vanishes identically on that circle, then the saddle coefficient
`M'` must be zero.

This is the exact micro-step used near the end of
[LATE_PROOF_DEPENDENCY_CHAIN.md](C:\Users\xliup\OneDrive\Documents\codex\researchinsleep\examples\gleason-theorem-accessible\LATE_PROOF_DEPENDENCY_CHAIN.md).

## 1. Setup

Let

`H(x',y',z') = M'(x'^2 - z'^2)`

and let

`C' = {x' = y'}`

be the primed great circle.

Assume:

1. `h = H` on `C'`,
2. `h = 0` identically on `C'`.

We want to show:

`M' = 0`.

## 2. Restrict the saddle to the circle

On `C'`, we have:

- `x' = y'`,
- `2x'^2 + z'^2 = 1`.

So the restriction of `H` to `C'` is

`H = M'(x'^2 - z'^2)`.

If `h=0` identically on `C'` and `h=H` on `C'`, then

`H=0`

identically on `C'`.

So for every point of `C'`,

`M'(x'^2 - z'^2) = 0`.

## 3. Why this forces `M'=0`

If `M' != 0`, then the equation above would imply

`x'^2 = z'^2`

for every point of `C'`.

But that is false.

For example, the point

`(1/sqrt(2), 1/sqrt(2), 0)`

lies on `C'`, and at that point

- `x'^2 = 1/2`,
- `z'^2 = 0`.

So

`x'^2 - z'^2 = 1/2 != 0`.

Therefore `H` is not identically zero on `C'` unless `M'=0`.

Hence:

`M' = 0`.

## 4. Why this matters

This lemma removes one last compressed sentence from the late-proof dependency
chain. The endgame no longer has to say vaguely:

- "the nonzero saddle cannot vanish identically on the circle."

It can instead cite this explicit fact.
