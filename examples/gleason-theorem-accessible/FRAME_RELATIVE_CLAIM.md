# Frame-Relative Six-Circle Claim

This note isolates the reusable lemma that powers both the first comparison step and the final contradiction.

## Why this lemma matters

In the last stage of the proof, we need to reuse an earlier comparison claim for a new frame `(p',q',r')`.

The key point is:

- the claim is not tied to one special coordinate system
- it is really a statement relative to any chosen orthonormal frame

Once that is made explicit, the final contradiction becomes much cleaner.

## General setup

Let `(u,v,w)` be any orthonormal frame on the sphere.

Write `(x,y,z)` for the coordinates of a point `s` in this frame.

Suppose:

- `F` is a bounded frame function
- `Q` is the quadratic comparison function built from the values of `F` on the frame `(u,v,w)`
- around the `u`-axis and the `w`-axis, the quarter-turn sum identities hold:
  - `F(s)+F(\hat u s)=Q(s)+Q(\hat u s)`
  - `F(s)+F(\hat w s)=Q(s)+Q(\hat w s)`

Define

`E = Q - F`.

Then:

- `E(s)+E(\hat u s)=0`
- `E(s)+E(\hat w s)=0`

and `E` is a weight-zero frame function.

## The claim

Under those conditions, `E` vanishes on the six frame-relative great circles:

- `x=y`
- `x=-y`
- `x=z`
- `x=-z`
- `y=z`
- `y=-z`

These equations are always understood in the coordinates of the chosen frame `(u,v,w)`.

## Why the proof is frame-relative

The proof never uses any special global meaning of the original `x,y,z` axes.

It uses only:

1. quarter-turns about two axes of the chosen frame
2. the fact that a weight-zero frame function satisfies `E(-s)=E(s)`
3. explicit compositions of those quarter-turns that send points on certain symmetry circles to their antipodes

Those three ingredients exist in exactly the same form for any orthonormal frame.

So once the claim is proved in one coordinate system, it automatically holds in any rotated coordinate system.

## Explicit coordinate-free reading

To say "the circle `x=y` in the frame `(u,v,w)`" means:

- the set of points whose `u`- and `v`-coordinates are equal in that frame

Likewise:

- `x=z` means equal `u`- and `w`-coordinates
- `y=-z` means the `v`-coordinate is the negative of the `w`-coordinate

These are not six universal circles on the sphere. They are six circles attached to the chosen frame.

That is exactly what we need in the final contradiction:

- first, the original frame gives one family of six zero circles
- later, the primed frame gives a second family of six comparison circles for `h`

## Why this closes the conceptual gap

The final contradiction uses two different coordinate systems:

- the original frame, where some zero circles are already known for `h`
- the primed extremal frame, where the saddle comparison function `H` is naturally written

The frame-relative claim explains why this is legitimate:

- the same six-circle lemma can be run again in the primed frame
- so on the primed circle `x'=y'`, the function `h` agrees with the primed comparison function `H`

That is the exact bridge needed before the intersection-counting contradiction.

## Practical summary

The reusable lemma is:

> whenever a weight-zero error function satisfies the two quarter-turn cancellation identities relative to a chosen orthonormal frame, it vanishes on the six equal-coordinate great circles for that frame.

This is the cleanest way to state the piece that gets reused at the end of Cooke's proof.
