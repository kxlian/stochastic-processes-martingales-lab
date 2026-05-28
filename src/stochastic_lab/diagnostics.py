"""Diagnostic summaries for stochastic simulations."""

from __future__ import annotations

import numpy as np
import pandas as pd


def path_moments(paths: pd.DataFrame) -> pd.DataFrame:
    """Compute cross-sectional mean and variance across paths for each time."""
    return pd.DataFrame(
        {
            "mean": paths.mean(axis=1),
            "variance": paths.var(axis=1, ddof=1),
            "std": paths.std(axis=1, ddof=1),
        }
    )


def terminal_summary(values: pd.Series) -> pd.DataFrame:
    """Compact terminal distribution summary."""
    q = values.quantile([0.01, 0.05, 0.50, 0.95, 0.99])
    return pd.DataFrame(
        {
            "mean": [float(values.mean())],
            "std": [float(values.std(ddof=1))],
            "q01": [float(q.loc[0.01])],
            "q05": [float(q.loc[0.05])],
            "median": [float(q.loc[0.50])],
            "q95": [float(q.loc[0.95])],
            "q99": [float(q.loc[0.99])],
        }
    )


def convergence_table(step_counts: list[int], n_paths: int, seed: int = 0) -> pd.DataFrame:
    """Compare scaled random walk terminal moments across step counts."""
    from .random_walk import symmetric_random_walk, scaled_random_walk

    rows = []
    for i, n_steps in enumerate(step_counts):
        paths = symmetric_random_walk(n_steps=n_steps, n_paths=n_paths, seed=seed + i)
        scaled = scaled_random_walk(paths)
        terminal = scaled.iloc[-1]
        rows.append(
            {
                "n_steps": n_steps,
                "mean_scaled_terminal": float(terminal.mean()),
                "var_scaled_terminal": float(terminal.var(ddof=1)),
                "std_scaled_terminal": float(terminal.std(ddof=1)),
            }
        )
    return pd.DataFrame(rows)
