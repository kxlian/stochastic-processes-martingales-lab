# Mathematical Roadmap

This roadmap outlines how the repository can be extended if the project becomes a longer research track.

## Current Level

The current version covers:

1. Random walks and filtrations
2. Martingales
3. Stopping times and optional stopping
4. Quadratic variation
5. Random-walk scaling toward Brownian motion

This is enough to form a coherent undergraduate-to-early-graduate probability research artifact.

## Next Mathematical Extensions

### 1. Doob Inequalities

Add Doob's maximal inequality and simulate the maximum of a stopped martingale.

Core question:

```text
How large can a martingale become before a fixed horizon?
```

### 2. Predictable Processes

Introduce predictable processes in discrete time.

Core question:

```text
What kind of strategy is allowed to depend only on past information?
```

### 3. Discrete Stochastic Integration

Define stochastic integrals of the form

```text
(H · M)_n = sum_{k=1}^n H_k (M_k - M_{k-1})
```

where `H_k` is predictable.

### 4. Ito Integral Construction

Move from discrete stochastic sums to the Ito integral for Brownian motion.

Core idea:

```text
Integrands must be adapted; future information cannot be used.
```

### 5. Ito Formula

Introduce Ito's formula and connect it to quadratic variation.

Key insight:

```text
The second-order term survives because Brownian quadratic variation is non-zero.
```

### 6. Change of Measure

Introduce Radon-Nikodym derivatives and Girsanov-style intuition.

This is mathematically deeper and should only be added after martingales and stochastic integration are solid.

## Optional Quant Research Bridge

Only after the math layer is clear, add one short note on empirical research hygiene:

- filtrations -> no look-ahead bias;
- stopping times -> valid timing rules;
- martingales -> residual unpredictability;
- quadratic variation -> realized variance;
- scaling limits -> reference models for aggregated shocks.

The project should remain mathematically led.
