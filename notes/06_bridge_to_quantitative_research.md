# 06 - Bridge to Quantitative Research

This repository is deliberately mathematical. Still, it supports a broader quantitative research profile.

## 1. Information sets

Filtrations formalize what is known at a point in time. This is directly connected to avoiding look-ahead bias in empirical research.

A signal should be measurable with respect to the information available when the decision is made.

## 2. Martingales and residual processes

A process being a martingale is a statement about conditional expectation relative to an information set.

In empirical work, one often asks whether a residual process still contains predictable structure after known effects have been removed.

## 3. Stopping times and timing rules

Stopping times formalize legitimate decision rules. A rule is valid only if it can be evaluated using information available at the decision time.

This is a clean mathematical counterpart to real backtest hygiene.

## 4. Quadratic variation and volatility

Quadratic variation is not a portfolio concept. It is a path property.

In later financial applications, realized variance and volatility estimators are practical descendants of the same mathematical idea.

## 5. Scaling limits

Donsker-style convergence shows how discrete random shocks can converge toward continuous stochastic processes.

This connects simple simulation, probability theory, and the deeper modeling language used in stochastic calculus.

## 6. Final positioning

The repository should not be read as: "I built another finance project."

It should be read as:

```text
I am building the mathematical foundation underneath systematic research.
```
