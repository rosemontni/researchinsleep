# Proof Dependencies

This file tracks what the cited proof really uses, what is elementary, and what is still conceptually advanced for a high school audience.

## Dependencies in the cited proof

### 1. Reduction to ordinary 3D geometry

This is good news for accessibility. The paper shows it is enough to understand the sphere in `R^3`.

### 2. Frame functions

This is the central replacement object:

- each direction on the sphere gets a number
- for every orthogonal triple, the three numbers add to the same constant

This can be stated without physics and is the best entry point for a younger audience.

### 3. Real-analysis warmup lemmas

The proof uses bounded functions on `[0,1]` and shows they must be linear under a strong additivity rule.

This is not impossible for a strong student, but it is already beyond standard high school.

### 4. Sphere geometry

The proof uses:

- great circles
- hemispheres
- parallels ("latitudes")
- geometric propagation along descent curves

This part can be explained visually, but the actual argument is still subtle.

### 5. Extremal-value arguments

The proof needs maxima and minima of bounded frame functions, then uses them to build a quadratic comparison function.

This is a genuine analysis step, not just a picture argument.

### 6. Final rigidity step

The hardest conceptual step is proving that the difference between the given frame function and the quadratic candidate must be identically zero.

That is where the proof stops being high-school natural.

## Accessibility diagnosis

### Good candidates for simplification

- remove quantum terminology completely
- work only in ordinary 3D Euclidean space
- phrase the theorem as a rule about assigning numbers to directions
- emphasize perpendicular triples and squares of coordinates
- use pictures on the sphere

### Likely irreducible difficulty

- proving the full general theorem rigorously without hiding real analysis
- justifying continuity/regularity-like behavior from the frame condition alone
- the final rigidity argument

## Current scope judgment

A fully rigorous, fully high-school-level proof of the full theorem is probably not realistic.

A realistic and valuable target is:

- a rigorous and intuitive proof of a carefully chosen 3D special case, or
- a proof of the 3D version with one extra regularity assumption, followed by an honest bridge to the full theorem
