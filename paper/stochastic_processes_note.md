# Stochastic Processes & Martingales

## A Compact Mathematical Research Note

This note studies five objects that sit at the foundation of stochastic process theory: random walks, filtrations, martingales, stopping times, and quadratic variation. The goal is not to build a trading strategy. The goal is to present the mathematical language underneath dynamic uncertainty.

---

## 1. Random Walks and Information

Let `(X_i)_{i >= 1}` be independent random variables such that

```text
P(X_i = 1) = P(X_i = -1) = 1/2.
```

The symmetric random walk is defined by

```text
S_0 = 0,
S_n = X_1 + ... + X_n.
```

The natural filtration is

```text
F_n = sigma(X_1, ..., X_n).
```

It represents exactly the information revealed by the first `n` increments. This distinction between the path and the information available at time `n` is the starting point for dynamic probability.

---

## 2. Martingales

A process `(M_n)` is a martingale with respect to `(F_n)` if it is adapted, integrable, and satisfies

```text
E[M_n | F_m] = M_m,    m <= n.
```

For the symmetric random walk,

```text
E[S_n | F_m]
= E[S_m + X_{m+1} + ... + X_n | F_m]
= S_m.
```

The future increments are independent of `F_m` and have mean zero. Therefore the symmetric random walk is a martingale.

A second example is the exponential martingale

```text
M_n(theta) = exp(theta S_n) / (cosh(theta))^n.
```

The denominator appears because `E[exp(theta X_i)] = cosh(theta)`. The normalization removes the expected exponential growth and preserves the martingale property.

---

## 3. Stopping Times

A random time `tau` is a stopping time if the event `{tau <= n}` is known at time `n` for every `n`.

A first hitting time such as

```text
tau = inf{n >= 0 : |S_n| >= a}
```

is a stopping time for the natural filtration of the random walk. By contrast, the time at which the path reaches its maximum over a fixed future horizon is generally not a stopping time, because it requires future information.

This distinction is the mathematical version of avoiding look-ahead bias.

---

## 4. Optional Stopping

If `(M_n)` is a martingale and `tau` is a bounded stopping time, then

```text
E[M_tau] = E[M_0].
```

For a symmetric random walk starting at zero, this gives

```text
E[S_tau] = 0.
```

The message is precise: under suitable conditions, stopping a fair game does not create positive expectation.

The conditions matter. If stopping times are unbounded or integrability fails, optional stopping can fail. This is why the theorem is both powerful and delicate.

---

## 5. Brownian Motion

Brownian motion `(W_t)_{t >= 0}` is a continuous-time stochastic process satisfying:

1. `W_0 = 0`;
2. independent increments;
3. `W_t - W_s ~ Normal(0, t-s)` for `s < t`;
4. continuous sample paths.

It is the canonical continuous-time limit object for accumulated independent shocks.

---

## 6. Quadratic Variation

For a partition `0 = t_0 < t_1 < ... < t_n = T`, define the quadratic variation along the partition as

```text
sum_k (W_{t_{k+1}} - W_{t_k})^2.
```

For Brownian motion, this converges to

```text
[W]_T = T.
```

This result is mathematically striking. Brownian paths are continuous but not smooth. Their squared increments do not disappear in the limit; they accumulate into elapsed time.

This is one of the reasons stochastic calculus differs from ordinary calculus.

---

## 7. From Random Walks to Brownian Motion

Define the scaled random walk

```text
W_n(t) = S_{floor(nt)} / sqrt(n),    0 <= t <= 1.
```

At `t = 1`, the central limit theorem implies

```text
S_n / sqrt(n) => Normal(0,1).
```

Donsker's invariance principle extends this endpoint convergence to process-level convergence: the scaled and interpolated random walk converges in distribution toward Brownian motion.

This explains why Brownian motion appears as a universal limit object in probability.

---

## 8. Why This Matters for Quantitative Research

This note is not an investment memo. Its role is foundational.

Filtrations explain information sets. Martingales explain conditional fairness. Stopping times explain legitimate timing rules. Quadratic variation explains pathwise roughness. Scaling limits explain how discrete stochastic systems can converge to continuous models.

Together, these concepts form a mathematical base layer underneath later work in alpha research, empirical signal testing, and portfolio construction.

The correct reading is not:

```text
This is another finance project.
```

The correct reading is:

```text
This is the mathematical foundation underneath systematic research.
```
