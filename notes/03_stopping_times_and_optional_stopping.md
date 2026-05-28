# 03 - Stopping Times and Optional Stopping

## 1. Stopping times

A random time `tau` is a stopping time with respect to a filtration `(F_n)` if the event

```text
{tau <= n}
```

is known at time `n` for every `n`.

This means the decision to stop by time `n` must depend only on information available up to time `n`.

Example:

```text
tau = first n such that |S_n| >= a
```

is a stopping time for the natural filtration of the random walk.

## 2. Non-example

The time of the maximum over a fixed future horizon,

```text
tau = argmax_{0 <= k <= N} S_k
```

is generally not a stopping time. To know whether today is the maximum, one must know the future.

This distinction is not technical decoration. It prevents look-ahead bias.

## 3. Optional stopping intuition

If `(M_n)` is a martingale and `tau` is a bounded stopping time, then

```text
E[M_tau] = E[M_0].
```

For a symmetric random walk starting at zero, this says:

```text
E[S_tau] = 0.
```

In plain English: if a game is fair and the stopping rule is legitimate and bounded, the stopping rule alone does not create positive expectation.

## 4. Why boundedness matters

Optional stopping has conditions. Without boundedness or suitable integrability assumptions, the statement can fail.

A famous source of confusion is the idea that one can keep doubling a fair bet until winning. The mathematical issue is that the stopping time may have infinite expectation or require unbounded capital.

The theorem is not saying all stopping systems are harmless. It is saying that under disciplined conditions, stopping a martingale preserves its expectation.

## 5. Research interpretation

Stopping times are one of the cleanest mathematical ways to discuss timing rules without cheating.

A valid rule must be adapted to the information flow. This is directly relevant to systematic research, where signals, entries, exits, and filters must be tested without future information leaking into the decision rule.
