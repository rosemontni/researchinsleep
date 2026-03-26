# An Accessible Path Toward Gleason's Theorem

## 1. What this project is trying to do

Gleason's theorem is a famous theorem about assigning probabilities to directions or subspaces in spaces of dimension at least three.

It is often introduced through quantum mechanics, which makes it feel physics-heavy. But after reading Cooke, Keane, and Moran's paper carefully, the real difficulty seems different:

- the proof is already mostly geometry and analysis
- the hard part is not advanced physics
- the hard part is the rigidity of a certain geometric scoring rule

This essay explains the strongest accessible version currently established in this project.

Important honesty note:

- this is **not** a full high-school-level proof of the full Gleason theorem
- it **is** an honest, rigorous path to an important special case
- and it explains the architecture of the full proof much more clearly than the raw paper alone

## 2. The game on the sphere

Work on the unit sphere in ordinary 3D space.

Every point on the sphere represents a direction.

Now imagine assigning a number to every direction. Call that number `f(direction)`.

The rule is:

- whenever three directions are mutually perpendicular, their three numbers add up to `1`

So for every orthonormal triple `(u,v,w)`,

`f(u) + f(v) + f(w) = 1`.

This is the 3D sphere version of the problem.

## 3. The obvious quadratic examples

Choose three perpendicular axes and three nonnegative numbers `a`, `b`, `c` with

`a+b+c=1`.

Define

`f(x,y,z)=ax^2+by^2+cz^2`

for each point `(x,y,z)` on the unit sphere.

This works because in any orthonormal basis, the squared x-coordinates add to `1`, the squared y-coordinates add to `1`, and the squared z-coordinates add to `1`.

So these quadratic functions always satisfy the perpendicular-triple rule.

Gleason's theorem says, in essence, that these are the only possibilities.

## 4. Why the full theorem is hard

The full theorem does not just say "here is a nice family of examples."

It says:

- every bounded scoring rule satisfying the frame condition must be quadratic

Cooke's paper proves this in a way that is far more elementary than the original, but it still relies on:

- real-analysis warmup lemmas
- geometry of great circles on the sphere
- extremal-value arguments
- a delicate comparison between a general function and a quadratic candidate

So the natural question for this project became:

> can the theorem be pushed into something a strong high school student could meaningfully understand?

The honest answer so far is:

- not the full theorem in complete rigor
- but yes for an important special case, and yes for the overall proof strategy

## 5. The special case that unlocks the picture

Assume the function `f` is continuous and satisfies:

- it reaches its largest value `M` at the north pole
- it is constant on the equator, with value `m`

Then the claim is:

`f(x,y,z)=m+(M-m)z^2`.

This is already a real theorem, and it is the first place where the rigidity becomes intuitive.

Why does this special case matter?

Because once the north pole and equator are pinned down, the sphere starts behaving like a simple height problem.

## 6. Latitude is the right variable

For a point `s=(x,y,z)` on the sphere, define its latitude parameter by

`l(s)=z^2`.

This number is:

- `1` at the north pole
- `0` on the equator
- somewhere in between elsewhere on the northern hemisphere

If the final formula is true, then the value of `f` should depend only on `z^2`.

So the problem becomes:

1. show higher latitude means larger value
2. show equal latitudes have equal value
3. deduce the exact formula

## 7. The geometric engine of the special case

For each point in the northern hemisphere, there is a great circle through it that descends toward the equator.

The key geometric fact is:

- as you move downward along that curve, the value of `f` cannot increase

Then another geometric lemma shows:

- if one point has larger latitude than another, you can reach the lower one by a chain of these descent steps

Therefore:

- larger latitude implies larger value

This turns the sphere into a one-variable monotonicity problem.

## 8. From the sphere to the interval `[0,1]`

For each latitude level `l`, define the biggest and smallest values of `f` on that horizontal circle.

The geometric comparison shows both are increasing functions of `l`.

Then the frame condition forces the bad latitudes, where the biggest and smallest values differ, to disappear.

So in the end the function really depends only on `l=z^2`.

That means there is a function `G` on `[0,1]` such that

`f(s)=G(z^2)`.

Now the frame rule becomes:

`G(a)+G(b)+G(c)=1`

whenever

`a+b+c=1`.

Since `G` is increasing, Cooke's warmup interval lemmas force `G` to be linear.

So:

`G(l)=m+(M-m)l`.

Substituting `l=z^2` gives:

`f(x,y,z)=m+(M-m)z^2`.

That is the special-case proof.

## 9. Why this already captures the soul of the theorem

This special case shows the central phenomenon:

- a very weak-looking rule on perpendicular triples
- together with continuity and geometry
- forces a quadratic law

That is the heart of Gleason's theorem.

## 10. The bridge to the full theorem

The full theorem starts with a completely general bounded frame function `f`.

It does **not** assume in advance that:

- some chosen pole is the maximum
- some chosen equator is constant

So the proof must manufacture that special-case situation.

Here is the cleanest version of the bridge found so far.

### Step A. Pick extremal data

Find:

- a point `p` where `f` is maximal, value `M`
- a point `r` where `f` is minimal, value `m`
- a point `q` perpendicular to both, with value `alpha`

Now define the quadratic candidate

`g(s)=M cos^2(theta(s,p)) + alpha cos^2(theta(s,q)) + m cos^2(theta(s,r))`.

This is the obvious quadratic function matching the key frame data.

### Step B. Compare `f` to `g`

Set

`h = g - f`.

If we can prove `h=0`, then `f=g`, so the theorem is done.

### Step C. Use quarter-turn sums

Rotate points by 90 degrees around the axis through `p`.

The function

`s -> f(s)+f(rot_p(s))`

has:

- a maximum at `p`
- a constant value on the equator perpendicular to `p`

So the special-case theorem applies to that rotated sum.

The same is true for the quadratic function `g`, and they have the same pole and equator data, so

`f(s)+f(rot_p(s)) = g(s)+g(rot_p(s))`.

Subtracting gives

`h(s)+h(rot_p(s))=0`.

Doing the same thing around the minimum axis `r` gives another cancellation identity:

`h(s)+h(rot_r(s))=0`.

So the error function inherits two strong quarter-turn symmetries.

## 11. Six zero great circles

From those quarter-turn identities and the fact that `h` is still a frame function of weight zero, Cooke shows that `h` vanishes on six important great circles:

- `x=y`
- `x=-y`
- `x=z`
- `x=-z`
- `y=z`
- `y=-z`

This is the moment where the error function becomes overconstrained.

## 12. The final contradiction

Now suppose `h` is not identically zero.

Run the same extremal-value argument on `h`.

Cooke breaks the endgame into four reductions:

1. the maximum and minimum of `h` must be opposites
2. the middle value on the adapted orthogonal frame must be `0`
3. therefore the natural comparison function for `h` in the primed frame is the saddle
   `H(x',y',z') = M'(x'^2-z'^2)`, and the earlier six-circle claim applies to `h` against this `H`
4. that saddle cannot have the zero-circle pattern already forced on `h`

The last contradiction is now much clearer than it was at the start of this project:

- the six zero-circle step is explicit
- the special intersection points are explicit
- the four-zero set of the saddle on `x'=y'` is explicit

What still remains partially imported is the extremal reduction and the reused six-circle comparison claim in the primed frame.

That reused comparison step is now isolated explicitly in [FRAME_RELATIVE_CLAIM.md](C:\Users\xliup\OneDrive\Documents\codex\researchinsleep\examples\gleason-theorem-accessible\FRAME_RELATIVE_CLAIM.md).
The corrected saddle setup is isolated in [SADDLE_REDUCTION.md](C:\Users\xliup\OneDrive\Documents\codex\researchinsleep\examples\gleason-theorem-accessible\SADDLE_REDUCTION.md).

That contradiction forces

`h = 0`.

Therefore

`f = g`,

and the original frame function is quadratic.

## 13. What is established and what is not

What this project now has:

- a clean 3D reformulation with no advanced physics language
- a guided special-case proof sketch that is genuinely much more accessible
- a much clearer map of the bridge to the full theorem
- an explicit quarter-turn derivation of the six zero-circle step
- a guided reconstruction of the final contradiction

What it does **not** yet have:

- a full theorem proof that is honestly at normal high-school level
- a fully self-contained formal reconstruction of every geometric intersection detail in the last contradiction

## 14. Final honest conclusion

The original hope was:

> find a proof of Gleason's theorem that does not need advanced physics and can be explained to a high school student.

The status now is:

- **advanced physics:** yes, we successfully avoided it
- **high-school-level full proof:** not honestly, not yet
- **high-school-level important core special case:** yes, much closer
- **clear conceptual path to the full theorem:** yes

So the project has not solved the whole problem, but it has found the most honest accessible version currently within reach.
