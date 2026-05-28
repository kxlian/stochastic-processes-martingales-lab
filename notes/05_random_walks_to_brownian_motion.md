# 05 - From Random Walks to Brownian Motion

## 1. Diffusive scaling

Let `(S_k)` be a symmetric random walk. Define the scaled process

```text
W_n(t) = S_{floor(nt)} / sqrt(n),    0 <= t <= 1.
```

The denominator `sqrt(n)` is the natural scale because the variance of `S_n` is `n`.

So

```text
Var(S_n / sqrt(n)) = 1.
```

## 2. Terminal convergence

At time `t = 1`, the scaled terminal value is

```text
S_n / sqrt(n).
```

By the central limit theorem, this converges in distribution to a standard normal random variable.

## 3. Process-level convergence

The stronger idea is that the full path converges, not only the endpoint.

Donsker's invariance principle states, roughly, that the linearly interpolated scaled random walk converges in distribution to Brownian motion as a stochastic process.

This is one of the great bridges between discrete and continuous probability.

## 4. Why the result matters

It explains why Brownian motion appears so naturally as a limit object.

Many microscopic independent shocks, when accumulated and scaled correctly, lead to the same macroscopic stochastic structure.

## 5. Research interpretation

For systematic research, this is not a trading claim. It is a modeling principle.

Discrete observations, shocks, residuals, and return increments can often be studied through limiting objects. The point is not that markets are exactly Brownian. The point is that Brownian motion gives a disciplined reference model for random evolution under aggregation.
