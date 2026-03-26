# A High-School-Friendly Path Into Gleason's Theorem

This note does **not** claim to prove the full Gleason theorem.

Instead, it proves an important special case in plain 3D geometry and explains why that special case captures the heart of the theorem.

## 1. The game

Imagine the unit sphere in ordinary 3D space. Every point on the sphere gives a **direction**.

We want to assign a number to every direction.

Call that number `f(direction)`.

The rule is:

- if three directions are all perpendicular to each other, then their three numbers must add up to `1`

So whenever `(u,v,w)` is a perpendicular triple,

`f(u) + f(v) + f(w) = 1`.

That is the whole game.

## 2. An obvious family of examples

Pick three perpendicular axes:

- x-axis
- y-axis
- z-axis

Pick three nonnegative numbers `a`, `b`, and `c` with

`a+b+c=1`.

Now define

`f(x,y,z)=ax^2+by^2+cz^2`

for every point `(x,y,z)` on the unit sphere.

Why does this work?

Because if `(u,v,w)` is an orthonormal basis, then the x-coordinates of `u,v,w` satisfy

`u_x^2 + v_x^2 + w_x^2 = 1`,

and the same is true for the y- and z-coordinates.

So when you add

`f(u)+f(v)+f(w)`,

the `a` pieces add to `a`, the `b` pieces add to `b`, and the `c` pieces add to `c`. Total:

`a+b+c=1`.

So quadratic formulas in the squared coordinates always work.

## 3. The real question

Are there any other kinds of scoring rules?

Gleason's theorem says, roughly, **no**. Under suitable assumptions, every such rule must come from one of these quadratic formulas.

That full theorem is hard.

But there is a special case that already shows the main idea.

## 4. The special case

Assume:

- `f` is continuous
- `f` has its largest value `M` at the north pole `(0,0,1)`
- `f` is constant on the equator, with value `m`

We will explain why this forces

`f(x,y,z)=m+(M-m)z^2`.

That is already a quadratic formula.

## 5. Why `z^2` should appear

If you stay on the sphere, then points with the same height `z` lie on the same horizontal circle.

But the right quantity here is actually `z^2`.

Why square it?

Because in a perpendicular triple, the numbers `x^2`, `y^2`, and `z^2` naturally add to `1`.

So `z^2` is exactly the kind of quantity that fits the perpendicular-triple rule.

This suggests that the value of `f` should depend only on how far north or south the point is, measured by `z^2`.

## 6. The sphere turns into a latitude problem

For a point `s=(x,y,z)` on the sphere, define its **latitude parameter**

`l(s)=z^2`.

This number is:

- `1` at the north pole
- `0` on the equator
- somewhere in between on the northern hemisphere

So if the formula is true, then `f` should really be a function of just one variable:

`f(s)=G(l(s))`

for some function `G` on `[0,1]`.

Now the whole problem becomes:

- show points with the same latitude parameter have the same value
- figure out what `G` must be

## 7. Why higher latitude should mean larger value

Picture a point `s` in the northern hemisphere.

There is a great circle through `s` that has `s` as its top point and then slopes downward toward the equator on both sides.

Think of it as the downhill path through `s`.

The geometric heart of the proof is:

> as you move down that path, the value of `f` cannot go up

This is not obvious, but it comes from combining:

- the fact that the north pole is the maximum
- the fact that the equator has one constant value
- the perpendicular-triple rule

Once this is proved, it gives a monotonicity law:

- points farther north must have value at least as large as points farther south

So latitude controls size.

## 8. Why equal latitude should force equal value

Now imagine looking at all points with the same latitude parameter `l`.

Maybe different points on that circle have different values. Maybe not.

The proof compares:

- the biggest value on that latitude
- the smallest value on that latitude

Then it shows the set of bad latitudes, where these two differ, is extremely small.

Using the perpendicular-triple rule again, the proof squeezes out the bad cases and concludes:

> every latitude has just one value

So the sphere really does collapse to a one-variable function `G(l)`.

## 9. The interval problem

Now comes the nicest part.

Once we know `f(s)=G(z^2)`, the sphere geometry is mostly gone.

The perpendicular-triple rule turns into:

`G(a)+G(b)+G(c)=1`

whenever

`a+b+c=1`

and `a,b,c` are in `[0,1]`.

Also:

- `G(0)=m`
- `G(1)=M`
- `G` is increasing

This is now just a problem about a function on the interval `[0,1]`.

And that problem has a very rigid answer:

`G(l)=m+(M-m)l`.

That is, `G` must be linear.

## 10. Final formula

Substitute `l=z^2`:

`f(x,y,z)=G(z^2)=m+(M-m)z^2`.

So in this special case, the scoring rule is forced to be quadratic.

## 11. Why this matters

This is the first place where Gleason's theorem becomes intuitive.

The message is:

- a rule on perpendicular triples looks weak at first
- but once you add continuity and a little geometry, it becomes very rigid
- the only surviving functions are quadratic ones

That rigidity is the soul of Gleason's theorem.

## 12. What this note does not prove

This note does **not** yet prove the full theorem.

What is still missing:

- the full reduction from Hilbert spaces to the 3D sphere picture
- the general argument when the function is not already normalized by a north pole maximum and an equator constant
- the last global comparison step that kills all remaining freedom

So this note should be read as:

- a genuine proof of an important special case
- an honest doorway into the full theorem

## 13. One-sentence summary

If a continuous scoring rule on directions in 3D always makes perpendicular triples add to `1`, and if the rule is highest at the north pole and flat along the equator, then the rule must be a quadratic function of height:

`f(x,y,z)=m+(M-m)z^2`.
