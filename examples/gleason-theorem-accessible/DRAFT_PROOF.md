# Draft Proof

## Current honest draft target

I am not yet claiming a complete new proof of the full theorem.

What follows is the start of an accessible reformulation and proof strategy for a rigorous 3D version with an explicit regularity assumption.

## Accessible reformulation

Imagine that every direction in ordinary 3D space has a score between 0 and 1.

Rule:

- whenever you pick three mutually perpendicular directions, their scores add up to 1

Question:

- what can such a scoring rule look like?

Natural examples already exist:

- choose three perpendicular coordinate axes
- pick nonnegative numbers `a`, `b`, and `c` with `a+b+c=1`
- define
  `q(x,y,z)=ax^2+by^2+cz^2`
  for every unit vector `(x,y,z)`

Then for every orthonormal triple, the three scores add to 1, because the sums of the squares of the coordinates add correctly.

So the real task is to show that every reasonable scoring rule must look like this.

## First proof skeleton

### Step 1. Fix three perpendicular axes

Let

- `a = f(1,0,0)`
- `b = f(0,1,0)`
- `c = f(0,0,1)`

Then `a+b+c=1` by the perpendicular-triple rule.

Build the quadratic candidate

`q(x,y,z)=ax^2+by^2+cz^2`.

### Step 2. Compare `f` with `q`

Define

`h(x,y,z)=f(x,y,z)-q(x,y,z)`.

Then `h` still has the perpendicular-triple sum rule, but now:

- `h(1,0,0)=0`
- `h(0,1,0)=0`
- `h(0,0,1)=0`

So it is enough to prove:

> if a continuous scoring rule has perpendicular-triple sums equal to 0 and vanishes on one orthonormal basis, then it vanishes everywhere.

This is the true rigidity statement.

### Step 3. Restrict to a great circle

On the equator `z=0`, every point `(x,y,0)` has a unique perpendicular partner `(-y,x,0)` in the same equator, and both are perpendicular to the north-south axis `(0,0,1)`.

So the rule gives

`h(x,y,0) + h(-y,x,0) + h(0,0,1) = 0`,

hence

`h(x,y,0) + h(-y,x,0) = 0`.

This is already a strong symmetry relation on the circle.

### Step 4. Try to propagate this symmetry

If similar relations can be proved on many rotated great circles, continuity may force `h` to be 0 everywhere.

This is the point where the draft is still incomplete.

## Current status

What is established:

- the theorem has a clean 3D non-physics reformulation
- quadratic examples are easy to construct
- subtracting such a quadratic example reduces the problem to a rigidity statement

What is not yet established:

- a complete high-school-level proof of the rigidity statement

## Honest next move

The next serious attempt should either:

- complete the rigidity argument with only elementary sphere geometry, or
- narrow the theorem to a special case where such an elementary rigidity proof really works

## Stronger progress after the second pass

There is now a serious candidate for the "elementary rigidity argument":

- not for the full theorem
- but for the special case where the function has a maximum at the north pole and is constant on the equator

In that case, the proof strategy is:

1. prove monotonicity along descent great circles
2. compare latitudes by chaining descent steps
3. collapse the sphere problem to a monotone function `G` on `[0,1]`
4. use the triple-sum rule to prove `G` is linear
5. conclude `f(x,y,z)=m+(M-m)z^2`

That is the first place where the theorem really starts to look explainable without advanced physics.

See [SPECIAL_CASE_PROOF.md](C:\Users\xliup\OneDrive\Documents\codex\researchinsleep\examples\gleason-theorem-accessible\SPECIAL_CASE_PROOF.md).
