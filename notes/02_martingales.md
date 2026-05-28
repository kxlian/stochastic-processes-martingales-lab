# 02 - Martingales

## 1. Definition

A process `(M_n)` is a martingale with respect to a filtration `(F_n)` if:

1. `M_n` is adapted to `F_n`;
2. `E[|M_n|] < infinity`;
3. for `m <= n`,

```text
E[M_n | F_m] = M_m.
```

The interpretation is that, given the present information, the best prediction of the future value is the current value.

## 2. Symmetric random walk as a martingale

Let

```text
S_n = X_1 + ... + X_n
```

with independent increments satisfying `E[X_i] = 0`.

Then for `m < n`,

```text
E[S_n | F_m]
= E[S_m + X_{m+1} + ... + X_n | F_m]
= S_m + E[X_{m+1} + ... + X_n | F_m]
= S_m.
```

The future increments have zero conditional mean because they are independent of current information.

Therefore the symmetric random walk is a martingale.

## 3. Exponential martingale

A deeper example is the exponential martingale. For a symmetric random walk,

```text
M_n(theta) = exp(theta S_n) / (cosh(theta))^n.
```

This is a martingale because

```text
E[exp(theta X_{n+1})] = cosh(theta).
```

So the normalization exactly removes the expected exponential growth.

## 4. Research interpretation

The martingale concept formalizes the idea of no predictable drift relative to a given information set.

That last phrase matters. A process can be a martingale under one filtration and not under another. The information set is part of the mathematical claim.

This is why martingales are foundational for thinking about fair games, efficient price processes, stopping rules, and residual processes after known structure has been removed.
