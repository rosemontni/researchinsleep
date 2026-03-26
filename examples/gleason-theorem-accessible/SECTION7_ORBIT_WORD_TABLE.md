# Section 7 orbit word table

This note records the explicit odd words used in the six-circle comparison
claim.

Its purpose is simple:

- make the six words part of the written proof package,
- let `proof_checks.py` serve as corroboration rather than as the main place the
  words are stored.

Throughout:

- `A(x,y,z) = (x,-z,y)`
- `B(x,y,z) = (-y,x,z)`

Words are read left to right as successive applications.

## Table

| Circle condition | Generic point `s` | Odd word `W` | Result |
|---|---|---|---|
| `x = y` | `(x,x,z)` | `BAA` | `W(s) = -s` |
| `x = z` | `(x,y,x)` | `ABBBA` | `W(s) = -s` |
| `y = z` | `(x,y,y)` | `BBA` | `W(s) = -s` |
| `x = -y` | `(x,-x,z)` | `AAB` | `W(s) = -s` |
| `x = -z` | `(x,y,-x)` | `ABA` | `W(s) = -s` |
| `y = -z` | `(x,y,-y)` | `ABB` | `W(s) = -s` |

## How the table is used

In [SECTION7_CLAIM_RECONSTRUCTION.md](C:\Users\xliup\OneDrive\Documents\codex\researchinsleep\examples\gleason-theorem-accessible\SECTION7_CLAIM_RECONSTRUCTION.md),
the cancellation rules imply:

- `h(A s) = -h(s)`
- `h(B s) = -h(s)`

So any odd-length word `W` satisfies:

`h(W(s)) = -h(s)`.

If the table gives `W(s) = -s`, then by evenness:

`h(s) = h(-s) = h(W(s)) = -h(s)`,

hence

`h(s)=0`.

That is the common proof template for all six circles.

## Status

The table entries are corroborated by
[proof_checks.py](C:\Users\xliup\OneDrive\Documents\codex\researchinsleep\examples\gleason-theorem-accessible\proof_checks.py),
but the table is now the primary written record inside the proof package.
