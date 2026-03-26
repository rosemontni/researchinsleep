# Attacking The Hardest Bridge

This note is a closer attempt to simplify the hardest step in the full proof:

> given a general bounded frame function `f`, how do we build the right quadratic candidate and prove the difference is zero?

## The basic plan

The full theorem wants to show:

`f(x,y,z) = ax^2 + by^2 + cz^2`

for some constants `a,b,c`.

The natural strategy is:

1. build the "obvious" quadratic candidate `g`
2. look at the error `h = f - g`
3. prove `h` must be zero everywhere

So the whole difficulty is concentrated in the last sentence.

## Step 1. Build the candidate from extremal data

By the previous part of the proof, bounded frame functions attain a maximum and a minimum.

Choose:

- `p` with `f(p)=M` (maximum)
- `r` with `f(r)=m` (minimum)
- `q` perpendicular to both, with `f(q)=alpha`

Then `M + alpha + m = w(f)`, the constant frame-sum.

Now define the obvious quadratic candidate

`g(s) = M cos^2(theta(s,p)) + alpha cos^2(theta(s,q)) + m cos^2(theta(s,r))`.

This is exactly the quadratic function that matches `f` on the special orthogonal triple `(p,q,r)`.

So there is no mystery in how to choose `g`. It is forced by the extreme values and one orthogonal frame.

## Step 2. Why the special case suddenly reappears

Take the sum

`f(s) + f(rot_p(s))`,

where `rot_p` means a 90-degree rotation around the axis through `p`.

Why use this?

Because on the equator orthogonal to `p`, the two points `s` and `rot_p(s)` are perpendicular to each other and also perpendicular to `p`.

So their values must add to the same constant:

`w(f) - f(p) = alpha + m`.

And at the pole `p`, the sum becomes

`f(p)+f(p)=2M`.

So the function

`s -> f(s)+f(rot_p(s))`

fits exactly the special-case pattern:

- it has a maximum at the north pole `p`
- it is constant on the equator orthogonal to `p`

Therefore the special-case theorem applies and gives a quadratic formula for this rotated sum.

But the same rotated sum for `g` has exactly the same pole and equator data, so:

`f(s)+f(rot_p(s)) = g(s)+g(rot_p(s))`.

By doing the analogous trick around the minimum axis `r`, we also get:

`f(s)+f(rot_r(s)) = g(s)+g(rot_r(s))`.

This is the first major bridge insight:

> even if `f` itself is not yet in the special-case setup, certain rotated sums of `f` are.

## Step 3. The error function inherits strong symmetries

Now define

`h = g - f`.

Then the two identities above become:

- `h(s) + h(rot_p(s)) = 0`
- `h(s) + h(rot_r(s)) = 0`

Also, `h` is still a frame function, but now of weight zero.

That means:

- on some highly symmetric circles, opposite quarter-turn points cancel
- on the original frame `(p,q,r)`, the function is zero

From these cancellation identities, Cooke proves `h` vanishes on six important great circles:

- `x = y`
- `x = -y`
- `x = z`
- `x = -z`
- `y = z`
- `y = -z`

This is much more rigid than just saying "h has some symmetries."

## Step 4. Why vanishing on six great circles is deadly

Now suppose `h` is not zero everywhere.

Then `h` has its own maximum `M'`, minimum `m'`, and some middle value `alpha'` on an orthogonal frame `(p',q',r')`.

Apply the same special-case machinery to `h`.

Because `h` has weight zero, the middle value must actually be `0`, and the special-case argument forces

`h(x',y',z') = M'(x'^2 - z'^2)`

in the coordinates adapted to `(p',q',r')`.

So any nonzero error function must look like a very specific quadratic saddle.

That is an enormous reduction:

- from "any strange frame function"
- to one explicit formula

## Step 5. The contradiction

But a function of the form

`M'(x'^2 - z'^2)`

cannot vanish on all six symmetry great circles unless `M' = 0`.

Why not?

Because its zero set is too small and too structured.

Cooke's final geometric contradiction is:

1. one of the great circles where `h=0` must line up with a zero set of the saddle
2. intersection counting then forces more zero points than the saddle allows
3. the only way out is that the saddle amplitude is actually zero

So `M'=0`, hence `h=0`.

Therefore `f=g`, and the theorem is proved.

## What this means conceptually

The bridge is not random at all. It has a clean architecture:

1. **Choose the quadratic candidate from extremal data.**
2. **Use quarter-turn sums to manufacture the special-case situation.**
3. **Convert that into symmetry and vanishing information for the error.**
4. **Show any nonzero error would have to be a saddle with an impossible zero pattern.**

This is the strongest simplification of the full bridge found so far.

## Why it is still not high-school-easy

Even in this cleaned-up form, the bridge still requires:

- comfortable reasoning with rotations on the sphere
- confidence with subtracting off the "right" comparison object
- understanding why zeros on several great circles overdetermine a quadratic-type object

So this is more teachable than the raw paper, but it is still not a fully beginner proof.

## Best present formulation

The most honest high-level explanation of the full theorem now seems to be:

- the special case proves that the only latitude-controlled frame functions are quadratic
- the general case reduces to that special case after comparing with the right quadratic function
- the remainder must vanish because its symmetry-imposed zero set is too large for any nonzero quadratic error
