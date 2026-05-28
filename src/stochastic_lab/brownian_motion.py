"""Brownian motion simulation and quadratic variation."""

from __future__ import annotations

import numpy as np
import pandas as pd


def simulate_brownian_motion(
    n_steps: int,
    n_paths: int,
    T: float = 1.0,
    seed: int | None = None,
) -> pd.DataFrame:
    """Simulate Brownian motion paths on [0,T].

    Brownian increments satisfy W_{t+dt} - W_t ~ Normal(0, dt), independently
    across non-overlapping intervals.
    """
    if n_steps <= 0:
        raise ValueError("n_steps must be positive")
    if n_paths <= 0:
        raise ValueError("n_paths must be positive")
    if T <= 0:
        raise ValueError("T must be positive")

    rng = np.random.default_rng(seed)
    dt = T / n_steps
    increments = rng.normal(loc=0.0, scale=np.sqrt(dt), size=(n_steps, n_paths))
    paths = np.vstack([np.zeros((1, n_paths)), np.cumsum(increments, axis=0)])
    index = np.linspace(0.0, T, n_steps + 1)
    return pd.DataFrame(paths, index=index, columns=[f"path_{i}" for i in range(n_paths)])


def quadratic_variation(paths: pd.DataFrame) -> pd.Series:
    """Compute discrete quadratic variation sum (Delta X)^2 for each path."""
    increments = paths.diff().dropna()
    qv = (increments ** 2).sum(axis=0).rename("quadratic_variation")
    return qv


def quadratic_variation_by_time(paths: pd.DataFrame) -> pd.DataFrame:
    """Compute cumulative quadratic variation path-by-path."""
    increments = paths.diff().fillna(0.0)
    qv = (increments ** 2).cumsum(axis=0)
    qv.index.name = "t"
    return qv
