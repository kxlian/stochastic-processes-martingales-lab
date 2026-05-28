# 04 - Quadratic Variation

## 1. Path variation

For a process `X_t`, the quadratic variation along a partition is the sum

```text
sum_k (X_{t_{k+1}} - X_{t_k})^2.
```

This measures accumulated squared movement along the path.

For smooth deterministic functions, the quadratic variation tends to zero as the partition becomes fine. For Brownian motion, the quadratic variation over `[0,T]` is `T`.

## 2. Brownian motion

Brownian motion `(W_t)` satisfies:

1. `W_0 = 0`;
2. independent increments;
3. `W_t - W_s ~ Normal(0, t-s)` for `s < t`;
4. continuous paths.

Although Brownian paths are continuous, they are extremely rough. Quadratic variation captures that roughness.

## 3. Core result

For Brownian motion,

```text
[W]_T = T.
```

The notation `[W]_T` denotes quadratic variation up to time `T`.

Intuition:

- each increment over length `dt` has variance `dt`;
- squared increments therefore contribute roughly `dt` on average;
- summing across the partition gives total contribution approximately `T`.

## 4. Why this is mathematically deep

Quadratic variation explains why ordinary calculus is not enough for Brownian paths.

For a smooth function, second-order terms vanish in the limit. For Brownian motion, the squared increments accumulate into time itself. This is one reason Ito's formula contains a second derivative term.

## 5. Research interpretation

Quadratic variation is the mathematical ancestor of realized variance and volatility estimation.

But in this repository, the focus remains mathematical: Brownian motion is not just a continuous random path; it has a precise pathwise variation structure.
