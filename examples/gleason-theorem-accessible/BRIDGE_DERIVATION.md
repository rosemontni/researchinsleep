# Bridge Derivation

This note expands the two most important mechanisms in the hard bridge:

1. why quarter-turn sums fall into the special-case theorem
2. why the error function must vanish on six great circles

The goal is not full formal completeness. The goal is to make the bridge feel mechanically understandable.

## Setup

Start with a bounded frame function `f` on the sphere.

Pick an orthogonal triple `(p,q,r)` such that:

- `f(p)=M` is the maximum
- `f(r)=m` is the minimum
- `f(q)=alpha`

Build the quadratic comparison function

`g(s)=M cos^2(theta(s,p)) + alpha cos^2(theta(s,q)) + m cos^2(theta(s,r))`.

Now define

`h = g - f`.

We want to show `h=0`.

## Part 1. Why quarter-turn sums are useful

### Rotate around the axis through `p`

Let `rot_p(s)` mean: rotate the sphere by 90 degrees around the axis through `p`.

This keeps the pole `p` fixed and rotates the equator perpendicular to `p`.

Now look at the function

`H_p(s)=f(s)+f(rot_p(s))`.

### Why `H_p` is constant on the equator

If `s` lies on the equator perpendicular to `p`, then:

- `s` is perpendicular to `p`
- `rot_p(s)` is also perpendicular to `p`
- `s` and `rot_p(s)` are perpendicular to each other

So `(s, rot_p(s), p)` is an orthonormal triple.

Therefore

`f(s)+f(rot_p(s))+f(p)=1`.

Since `f(p)=M`, we get

`H_p(s)=1-M`.

But `1-M` is exactly `alpha + m`, because the frame `(p,q,r)` gives

`M + alpha + m = 1`.

So on the equator,

`H_p(s)=alpha+m`.

That means `H_p` is constant on the equator.

### Why `H_p` is maximal at the pole

At the pole `p`, rotation does nothing:

`rot_p(p)=p`.

So

`H_p(p)=f(p)+f(p)=2M`.

Since `M` is the maximum value of `f`, no point can have `f(s)` or `f(rot_p(s))` bigger than `M`. Hence

`H_p(s) <= 2M`

for all `s`.

So `H_p` has its maximum at the pole `p`.

### Why the special-case theorem applies

We have now shown:

- `H_p` is a frame function
- `H_p` is maximal at `p`
- `H_p` is constant on the equator perpendicular to `p`

So the special-case theorem applies:

`H_p(s)=2M cos^2(theta(s,p)) + (alpha+m)(1-cos^2(theta(s,p)))`.

This is exactly the kind of formula derived in the special-case note.

## Part 2. Why the same formula holds for the quadratic candidate

Now compute the same rotated sum for `g`.

Because `g` was built from squared cosines relative to the orthogonal frame `(p,q,r)`, rotating around `p` swaps the `q` and `r` directions.

So:

- the `p` part stays the same
- the `q` and `r` parts trade places

Therefore

`g(s)+g(rot_p(s))`

has:

- value `2M` at the pole
- value `alpha+m` on the equator

So it has the same special-case formula as `H_p`.

Hence:

`f(s)+f(rot_p(s)) = g(s)+g(rot_p(s))`.

Subtracting gives

`h(s)+h(rot_p(s))=0`.

This is the first key symmetry identity.

## Part 3. The second quarter-turn identity

Do exactly the same thing around the axis through `r`, the minimum point.

Let `rot_r` be the 90-degree rotation around `r`.

Then

`H_r(s)=f(s)+f(rot_r(s))`

is:

- maximal at `r` for `-f`, equivalently minimal for `f`
- constant on the equator perpendicular to `r`

Running the same argument with `-f` gives

`f(s)+f(rot_r(s)) = g(s)+g(rot_r(s))`,

so

`h(s)+h(rot_r(s))=0`.

Now `h` has two different quarter-turn cancellation laws.

## Part 4. Why these identities are powerful

The identities mean:

- knowing `h` at one point tells you `h` at a quarter-turn point
- repeated quarter-turns force many exact sign relations

Because `h` is also a frame function of weight `0`, its values on orthogonal triples must add to `0`.

This combination is much stronger than either property alone.

## Part 5. Choosing coordinates

Write points in coordinates adapted to the frame `(p,q,r)`.

That means:

- `p = (1,0,0)` in the new coordinates
- `q = (0,1,0)`
- `r = (0,0,1)`

Now the quarter-turns become concrete coordinate moves.

In Cooke's notation, the two basic 90-degree rotations act like:

- around `p`: `(x,y,z) -> (x,-z,y)`
- around `r`: `(x,y,z) -> (-y,x,z)`

The exact sign conventions depend on orientation, but the key point is:

- one rotation preserves `x` and rotates the `yz`-plane
- the other preserves `z` and rotates the `xy`-plane

## Part 6. First easy zeros

Because `h` has weight `0` and agrees with `0` on the basis vectors `p,q,r`, it is already `0` at:

- `(1,0,0)`
- `(0,1,0)`
- `(0,0,1)`

and also at their antipodes, since frame functions satisfy `h(s)=h(-s)`.

So there are already six zero points.

But Cooke gets much more: six entire great circles of zeros.

## Part 7. Why equal-coordinate circles appear

The quarter-turn identities imply that certain coordinate symmetries preserve or negate the value of `h`.

When a point lies on a symmetry set such as

- `x=y`
- `x=-y`
- `x=z`
- `x=-z`
- `y=z`
- `y=-z`

the two quarter-turn relations become compatible only if the value is `0`.

Here is the intuition:

- a point on one of these circles is sent by a short sequence of quarter-turns to itself or to its antipode
- each quarter-turn flips the sign of `h`
- after an odd number of sign flips, you come back to the same value
- so the only possibility is `h=0`

That is why these symmetry circles become zero circles.

With Cooke's quarter-turn operators

- `\hat q(x,y,z)=(-y,x,z)`
- `\hat p(x,y,z)=(x,-z,y)`

the needed compositions can be written explicitly:

- if `x=y`, then `\hat p \hat p \hat q(s) = -s`
- if `x=z`, then `\hat p \hat q \hat q \hat q \hat p(s) = -s`
- if `y=z`, then `\hat p \hat q \hat q(s) = -s`
- if `x=-y`, then `\hat q \hat p \hat p(s) = -s`
- if `x=-z`, then `\hat p \hat q \hat p(s) = -s`
- if `y=-z`, then `\hat q \hat q \hat p(s) = -s`

Each quarter-turn flips the sign of `h`, so in every case

`h(-s) = -h(s)`.

But frame functions satisfy `h(-s)=h(s)`, hence `h(s)=0`.

So `h` really does vanish on all six equal-coordinate great circles.

These six composition words are also checked symbolically in [proof_checks.py](C:\Users\xliup\OneDrive\Documents\codex\researchinsleep\examples\gleason-theorem-accessible\proof_checks.py).

## Part 8. A sample calculation pattern

Suppose a point satisfies `x=y`.

Apply one quarter-turn around `p`, then one around `r`, and then repeat in the right order.

Because `x=y`, the resulting point lines up with either the original point or its antipode.

But each quarter-turn introduces a minus sign via

- `h(s)+h(rot_p(s))=0`
- `h(s)+h(rot_r(s))=0`

So after composing the moves, we get

`h(s) = -h(s)`

or

`h(s) = -h(-s) = -h(s)`.

Either way, `h(s)=0`.

The same pattern works on each of the six equal-coordinate great circles.

## Part 9. Why this almost finishes the proof

Once `h` vanishes on six great circles, any nonzero candidate for `h` is forced into an absurdly rigid corner.

Cooke then shows:

- if `h` were nonzero, the same extremal-value method would force it to look like
  `M'(x'^2-z'^2)`
  in some adapted coordinates
- but that saddle-shaped function cannot have all six required zero circles

So `h` must actually be identically zero.

## Part 10. Best cleaned-up summary

The bridge works because:

1. quarter-turn sums manufacture the special-case theorem
2. subtracting the quadratic candidate turns that theorem into cancellation identities for the error
3. those identities force the error to vanish on many symmetry circles
4. any nonzero error would have a much smaller zero set than that

That is the real engine of the full proof.
