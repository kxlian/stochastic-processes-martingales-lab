"""Stopping-time utilities for discrete stochastic processes."""

from __future__ import annotations

import numpy as np
import pandas as pd


def bounded_first_exit_time(paths: pd.DataFrame, boundary: float, max_time: int | None = None) -> pd.Series:
    """First time |S_t| >= boundary, capped by max_time.

    The cap makes the stopping time bounded, which is the clean setting for the
    optional stopping experiment in this repository.
    """
    if boundary <= 0:
        raise ValueError("boundary must be positive")
    horizon = len(paths.index) - 1
    if max_time is None:
        max_time = horizon
    if max_time < 0 or max_time > horizon:
        raise ValueError("max_time must be between 0 and the path horizon")

    out = []
    for _, col in paths.items():
        arr = col.values[: max_time + 1]
        hits = np.where(np.abs(arr) >= boundary)[0]
        out.append(int(hits[0]) if len(hits) else int(max_time))
    return pd.Series(out, index=paths.columns, name="tau")


def terminal_at_stopping_time(paths: pd.DataFrame, stopping_times: pd.Series) -> pd.Series:
    """Return S_tau for each path."""
    values = []
    for col in paths.columns:
        tau = int(stopping_times.loc[col])
        values.append(paths.loc[tau, col])
    return pd.Series(values, index=paths.columns, name="S_tau")


def stopping_rule_summary(paths: pd.DataFrame, stopping_times: pd.Series) -> pd.DataFrame:
    """Summarize a bounded stopping rule."""
    stopped_values = terminal_at_stopping_time(paths, stopping_times)
    return pd.DataFrame(
        {
            "mean_tau": [float(stopping_times.mean())],
            "median_tau": [float(stopping_times.median())],
            "mean_stopped_value": [float(stopped_values.mean())],
            "std_stopped_value": [float(stopped_values.std(ddof=1))],
            "share_hit_before_cap": [float((stopping_times < stopping_times.max()).mean())],
        }
    )
