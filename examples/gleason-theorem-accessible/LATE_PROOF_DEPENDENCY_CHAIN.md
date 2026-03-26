# Late Proof Dependency Chain

This note rewrites the late part of the Gleason proof reconstruction as a
numbered dependency chain.

Its purpose is to make the back half of the proof easier to audit, reference,
and semi-formalize.

Primary supporting notes:

- [SECTION7_CANCELLATION_IDENTITIES.md](C:\Users\xliup\OneDrive\Documents\codex\researchinsleep\examples\gleason-theorem-accessible\SECTION7_CANCELLATION_IDENTITIES.md)
- [SECTION7_CLAIM_RECONSTRUCTION.md](C:\Users\xliup\OneDrive\Documents\codex\researchinsleep\examples\gleason-theorem-accessible\SECTION7_CLAIM_RECONSTRUCTION.md)
- [FRAME_RELATIVE_CLAIM.md](C:\Users\xliup\OneDrive\Documents\codex\researchinsleep\examples\gleason-theorem-accessible\FRAME_RELATIVE_CLAIM.md)
- [STEP_I_EXTREMAL_REDUCTION.md](C:\Users\xliup\OneDrive\Documents\codex\researchinsleep\examples\gleason-theorem-accessible\STEP_I_EXTREMAL_REDUCTION.md)
- [FINAL_ENDGAME_RECONSTRUCTION.md](C:\Users\xliup\OneDrive\Documents\codex\researchinsleep\examples\gleason-theorem-accessible\FINAL_ENDGAME_RECONSTRUCTION.md)
- [PRIMED_CIRCLE_SADDLE_LEMMA.md](C:\Users\xliup\OneDrive\Documents\codex\researchinsleep\examples\gleason-theorem-accessible\PRIMED_CIRCLE_SADDLE_LEMMA.md)

## 1. Standing setup

Let `f` be a bounded frame function. Fix an unprimed orthonormal frame
`(p,q,r)` realizing the comparison data:

- `f(p)=M`
- `f(q)=alpha`
- `f(r)=m`

Define

`g(x,y,z) = M x^2 + alpha y^2 + m z^2`

and

`h = g - f`.

Then:

1. `h` is a bounded frame function.
2. `w(h)=0`.
3. `h(p)=h(q)=h(r)=0`.

Goal:

4. show `h=0`.

Then `f=g`, so `f` is quadratic.

## 2. Late-proof inputs

The late proof uses these already-established inputs.

### Input A: six-circle comparison claim

From [SECTION7_CLAIM_RECONSTRUCTION.md](C:\Users\xliup\OneDrive\Documents\codex\researchinsleep\examples\gleason-theorem-accessible\SECTION7_CLAIM_RECONSTRUCTION.md):

5. `h=0` on the six unprimed symmetry great circles

- `x=y`
- `x=z`
- `y=z`
- `x=-y`
- `x=-z`
- `y=-z`

### Input B: frame-relative reuse

From [FRAME_RELATIVE_CLAIM.md](C:\Users\xliup\OneDrive\Documents\codex\researchinsleep\examples\gleason-theorem-accessible\FRAME_RELATIVE_CLAIM.md):

6. the six-circle comparison mechanism can be reused in any orthonormal frame

### Input C: extremal attainment

From [SECTION6_RECONSTRUCTION.md](C:\Users\xliup\OneDrive\Documents\codex\researchinsleep\examples\gleason-theorem-accessible\SECTION6_RECONSTRUCTION.md)
and [SECTION6_TOPOLOGY_APPENDIX.md](C:\Users\xliup\OneDrive\Documents\codex\researchinsleep\examples\gleason-theorem-accessible\SECTION6_TOPOLOGY_APPENDIX.md):

7. bounded frame functions attain their extrema

## 3. Primed extremal setup

By (7), choose a primed orthonormal frame `(p',q',r')` such that:

8. `h(p') = M' = sup h`
9. `h(q') = alpha'`
10. `h(r') = m' = inf h`

Since `w(h)=0`, we have:

11. `M' + alpha' + m' = 0`

## 4. Extremal reduction

From [STEP_I_EXTREMAL_REDUCTION.md](C:\Users\xliup\OneDrive\Documents\codex\researchinsleep\examples\gleason-theorem-accessible\STEP_I_EXTREMAL_REDUCTION.md):

12. `M' = -m'`

Combining (11) and (12):

13. `alpha' = 0`

So the primed extremal data are exactly:

14. `h(p') = M'`
15. `h(q') = 0`
16. `h(r') = -M'`

## 5. Primed comparison saddle

Define

`H(x',y',z') = M'(x'^2 - z'^2)`.

Then:

17. `H` is a frame function
18. `w(H)=0`
19. `H(p')=M'`
20. `H(q')=0`
21. `H(r')=-M'`

By (14)-(16) and (19)-(21), `h` and `H` agree at the three primed coordinate
axes and have the same weight.

Using (6), apply the six-circle comparison claim in the primed frame:

22. `h=H` on the six primed symmetry circles

In particular:

23. `h=H` on the primed great circle `C' := {x'=y'}`

## 6. Zero pattern on the primed circle

Restrict `H` to `C'`.

On `C'`:

- `x'=y'`
- `2x'^2 + z'^2 = 1`

and

`H = M'(x'^2 - z'^2)`.

So:

24. `H=0` on `C'` exactly when `x'^2 = z'^2`

This gives exactly four zero points on `C'`.

By (23):

25. `h` has exactly four zero points on `C'`

## 7. First forced antipodal pair

Let

- `u = (a,a,a)`
- `-u = (-a,-a,-a)`

where `a=1/sqrt(3)`.

These are exactly the common intersection of the three unprimed circles

- `x=y`
- `x=z`
- `y=z`

By (5):

26. `h(u)=h(-u)=0`

From the explicit great-circle case split in
[FINAL_ENDGAME_RECONSTRUCTION.md](C:\Users\xliup\OneDrive\Documents\codex\researchinsleep\examples\gleason-theorem-accessible\FINAL_ENDGAME_RECONSTRUCTION.md)
and [ENDGAME_INTERSECTION_LEMMA.md](C:\Users\xliup\OneDrive\Documents\codex\researchinsleep\examples\gleason-theorem-accessible\ENDGAME_INTERSECTION_LEMMA.md):

27. if `C'` missed `u,-u`, then the intersections of `C'` with the three
    circles `x=y`, `x=z`, `y=z` would produce three distinct antipodal pairs of
    zeros on `C'`

Therefore:

28. `C'` must contain `u,-u`

## 8. Second forced antipodal pair

Let

- `v = (a,-a,-a)`
- `-v = (-a,a,a)`

These are the common intersection of the two unprimed circles

- `x=-y`
- `x=-z`

Again by (5):

29. `h(v)=h(-v)=0`

And from the explicit intersection lemma:

30. if `C'` contained `u,-u` but missed `v,-v`, then its intersections with
    `x=-y` and `x=-z` would contribute two more distinct antipodal zero pairs on
    `C'`

Together with (28), this would force at least six zeros on `C'`, contradicting
(25). Therefore:

31. `C'` must contain `v,-v`

## 9. Uniqueness of the great circle

The four points `u,-u,v,-v` lie on the unique great circle `y=z`.

Hence from (28) and (31):

32. `C' = {y=z}`

By (5), `h=0` identically on the unprimed circle `y=z`. Therefore:

33. `h=0` identically on `C'`

## 10. Final scalar collapse

By (23) and (33), `H=0` identically on `C'`.

By [PRIMED_CIRCLE_SADDLE_LEMMA.md](C:\Users\xliup\OneDrive\Documents\codex\researchinsleep\examples\gleason-theorem-accessible\PRIMED_CIRCLE_SADDLE_LEMMA.md):

34. `M' = 0`

Using (12):

35. `m' = 0`

Using (13):

36. `alpha' = 0`

Now:

- `sup h = M' = 0`
- `inf h = m' = 0`

Therefore every value of `h` lies between `0` and `0`. Hence:

37. `h=0` on all of `S`

Therefore:

38. `f=g`

which proves the theorem.

## 11. What remains imported here

This dependency chain is now very explicit. The remaining imported ingredients
are narrow:

1. the Section 5 symmetrization identities behind the two cancellation rules
   used in the six-circle claim, now isolated in
   [SECTION7_CANCELLATION_IDENTITIES.md](C:\Users\xliup\OneDrive\Documents\codex\researchinsleep\examples\gleason-theorem-accessible\SECTION7_CANCELLATION_IDENTITIES.md)
2. standard compactness machinery in Section 6

Everything else in the late proof now appears in numbered logical form.
