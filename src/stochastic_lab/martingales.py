"""Martingale examples and diagnostics."""

from __future__ import annotations

import numpy as np
import pandas as pd


def exponential_martingale(paths: pd.DataFrame, theta: float) -> pd.DataFrame:
    """Construct the exponential martingale for a symmetric random walk.

    For S_n = X_1 + ... + X_n with P(X_i = +/-1) = 1/2,

        M_n(theta) = exp(theta S_n) / (cosh(theta))^n

    is a martingale with E[M_n] = M_0 = 1.
    """
    if not np.isfinite(theta):
        raise ValueError("theta must be finite")
    times = paths.index.to_numpy(dtype=float)
    normalizer = np.cosh(theta) ** times
    values = np.exp(theta * paths.to_numpy(dtype=float)) / normalizer[:, None]
    return pd.DataFrame(values, index=paths.index, columns=paths.columns)


def stopped_process(paths: pd.DataFrame, stopping_times: pd.Series) -> pd.DataFrame:
    """Return the stopped process X_{t wedge tau}."""
    stopped = paths.copy()
    for col in paths.columns:
        tau = int(stopping_times.loc[col])
        if tau < len(paths.index) - 1:
            stopped.loc[tau:, col] = paths.loc[tau, col]
    return stopped


def optional_stopping_summary(paths: pd.DataFrame, stopping_times: pd.Series) -> pd.DataFrame:
    """Summarize E[S_tau] for a bounded stopping experiment."""
    stopped_values = []
    for col in paths.columns:
        tau = int(stopping_times.loc[col])
        stopped_values.append(paths.loc[tau, col])
    stopped_values = pd.Series(stopped_values, index=paths.columns, name="S_tau")
    return pd.DataFrame(
        {
            "initial_mean": [float(paths.iloc[0].mean())],
            "terminal_mean_without_stopping": [float(paths.iloc[-1].mean())],
            "stopped_mean": [float(stopped_values.mean())],
            "stopped_std": [float(stopped_values.std(ddof=1))],
            "mean_stopping_time": [float(stopping_times.mean())],
            "median_stopping_time": [float(stopping_times.median())],
        }
    )


def empirical_martingale_means(process: pd.DataFrame) -> pd.Series:
    """Return path-averaged means E_hat[X_t] across time."""
    return process.mean(axis=1).rename("cross_sectional_mean")
