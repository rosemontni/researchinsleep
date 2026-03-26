# Reconstructing the warmup theorems

This note rebuilds the two warmup theorems from Section 3 of
Cooke--Keane--Moran.

They are short, but they do important conceptual work:

1. they convert the frame-function constraint into a one-variable functional
   equation,
2. they show that boundedness plus the `a+b+c=1` rule forces linearity,
3. they are the template for the Section 5 latitude argument.

Source pages:
- [pages 120--122 of the Cooke paper](https://rogermcooke.net/rogermcooke_files/Elementary%20Proof%20of%20Gleasons%20Theorem.pdf)

## 1. Warmup Theorem I

### Statement

Let `f:[0,1] -> R` be bounded, and suppose there is a constant `w` such that

`f(a) + f(b) + f(c) = w`

whenever `a,b,c in [0,1]` and `a+b+c=1`.

Then

`f(a) = (w - 3 f(0)) a + f(0)`

for every `a in [0,1]`.

So `f` must be affine.

### Proof

Subtract the constant `f(0)` from `f`. More precisely, define

`F(a) = f(a) - f(0)`.

Then `F` is still bounded, and if `a+b+c=1`, we have

`F(a) + F(b) + F(c) = w - 3f(0) =: w_tilde`.

Also `F(0)=0`.

So it is enough to prove that

`F(a) = w_tilde a`.

Now choose `c=0` and `b=1-a`. Then

`F(a) + F(1-a) = w_tilde`,

so

`F(a) = w_tilde - F(1-a)`.

Next choose `c = 1-(a+b)` whenever `a,b,a+b in [0,1]`. Then

`F(a) + F(b) + F(1-(a+b)) = w_tilde`.

Using the previous identity on the third term,

`F(1-(a+b)) = w_tilde - F(a+b)`,

we get

`F(a) + F(b) = F(a+b)`

whenever `a,b,a+b in [0,1]`.

So `F` is additive on `[0,1]`.

In particular, for each rational `q in [0,1]`,

`F(q) = q F(1)`.

But choosing `a=1` and `b=c=0` in the defining relation gives

`F(1) = w_tilde`.

Hence

`F(q)=w_tilde q`

for all rational `q in [0,1]`.

Now use boundedness to get continuity at `0`. If `a in [0,1]` and `n a <= 1`,
then additivity gives

`F(n a) = n F(a)`.

So

`|F(a)| = |F(n a)| / n`.

Because `F` is bounded on `[0,1]`, the right-hand side goes to `0` as `a -> 0`.
Thus `F` is continuous at `0`.

An additive function that is continuous at `0` is continuous everywhere, and
therefore agrees with its rational values on all of `[0,1]`. So

`F(a) = w_tilde a`

for all `a in [0,1]`.

Undoing the normalization gives

`f(a) = (w - 3 f(0)) a + f(0)`.

That is Warmup I.

## 2. Warmup Theorem II

### Statement

Let `C` be a finite or countable subset of `(0,1)`. Let

`f : [0,1] \\ C -> R`

satisfy:

1. `f(0)=0`,
2. if `a,b in [0,1] \\ C` and `a<b`, then `f(a) <= f(b)`,
3. if `a,b,c in [0,1] \\ C` and `a+b+c=1`, then
   `f(a)+f(b)+f(c)=1`.

Then

`f(a)=a`

for every `a in [0,1] \\ C`.

### Proof idea

The theorem says that even if we remove countably many bad points, the same
functional equation plus monotonicity still forces the identity function.

The proof has three stages:

1. choose one special point `a_0` avoiding a countable obstruction set,
2. prove linearity on rational multiples of `a_0`,
3. use monotonicity to extend that linearity to every point outside `C`,
   then use the `a+b+c=1` rule to identify the slope as `1`.

### Step 1: choose a good anchor point

Define

`C_hat = { r c : c in C, r rational } U { r(1-c) : c in C, r rational }`.

This set is still finite or countable, so we may choose

`a_0 in (0,1) \\ C_hat`.

The reason for this choice is:

If `r` is rational and `r a_0 in [0,1]`, then neither `r a_0` nor
`1-r a_0` belongs to `C`.

Indeed:

- if `r a_0 = c in C`, then `a_0 = c/r in C_hat`,
- if `1-r a_0 = c in C`, then `a_0 = (1-c)/r in C_hat`,

both impossible.

### Step 2: additivity on rational multiples of `a_0`

Take rational `r,r'` such that

- `r a_0 in [0,1]`,
- `r' a_0 in [0,1]`,
- `(r+r') a_0 in [0,1]`.

Then the three points

- `r a_0`,
- `r' a_0`,
- `1-(r+r')a_0`

all lie in `[0,1] \\ C`, and their sum is `1`. So condition (3) gives

`f(r a_0) + f(r' a_0) + f(1-(r+r')a_0) = 1`.

Likewise, applying (3) to the pair `((r+r')a_0, 1-(r+r')a_0, 0)` gives

`f((r+r')a_0) + f(1-(r+r')a_0) + f(0) = 1`.

Since `f(0)=0`, subtracting the two equations yields

`f(r a_0) + f(r' a_0) = f((r+r')a_0)`.

So `f` is additive on rational multiples of `a_0`.

Exactly as in Warmup I, this implies

`f(r a_0) = r f(a_0)`

for all rational `r` with `r a_0 in [0,1]`.

### Step 3: monotonicity extends linearity

Take any `a in [0,1] \\ C`.

Choose rational sequences

- `r_n ↑ a/a_0`,
- `s_n ↓ a/a_0`

such that `r_n a_0, s_n a_0 in [0,1]`.

Then

`r_n a_0 <= a <= s_n a_0`,

so by monotonicity,

`r_n f(a_0) = f(r_n a_0) <= f(a) <= f(s_n a_0) = s_n f(a_0)`.

Letting `n -> infinity`, we obtain

`f(a) = (f(a_0)/a_0) a`

for every `a in [0,1] \\ C`.

So `f` is linear on its whole domain:

`f(a) = lambda a`

with

`lambda = f(a_0)/a_0`.

### Step 4: identify the slope

Now pick `a in (0,1) \\ C`. Since `C` is countable, we can choose such an `a`
with `a < 1/2`.

Next choose `b in (0,1-a) \\ (C U (1-a-C))`.

This is possible because `C U (1-a-C)` is countable, while `(0,1-a)` is an
interval. Then set

`c = 1-a-b`.

By construction:

1. `b notin C`,
2. `c = 1-a-b notin C`,
3. `a+b+c=1`.

Using the linear form just proved,

`1 = f(a)+f(b)+f(c) = lambda(a+b+c) = lambda`.

So `lambda = 1`.

Hence

`f(a)=a`

for all `a in [0,1] \\ C`.

That is Warmup II.

## 3. Why these theorems matter

Warmup I and Warmup II are the one-variable backbone of Section 5:

1. Warmup I explains why a bounded additive rule on `[0,1]` forces linearity.
2. Warmup II shows that even with a countable exceptional set, monotonicity and
   the same ternary rule still force linearity.

So Section 5 is not a miracle. It reduces a frame function on the sphere to a
one-variable function of latitude, then applies exactly this logic.

## 4. Status

These warmup theorems are now effectively reconstructed locally. They are no
longer major imported black boxes in this project.
