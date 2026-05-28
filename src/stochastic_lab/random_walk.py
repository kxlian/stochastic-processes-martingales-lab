"""Random walk utilities.

The symmetric random walk is the canonical discrete-time martingale:

    S_n = X_1 + ... + X_n,     P(X_i = 1) = P(X_i = -1) = 1/2.

The natural filtration F_n contains exactly the information revealed by the
first n increments.
"""

from __future__ import annotations

import numpy as np
import pandas as pd


def symmetric_random_walk(n_steps: int, n_paths: int, seed: int | None = None) -> pd.DataFrame:
    """Simulate independent symmetric random walk paths.

    Parameters
    ----------
    n_steps:
        Number of increments. The returned path includes time 0, so it has
        n_steps + 1 rows.
    n_paths:
        Number of independent paths.
    seed:
        Optional random seed.

    Returns
    -------
    pandas.DataFrame
        Rows are times 0,...,n_steps and columns are path identifiers.
    """
    if n_steps <= 0:
        raise ValueError("n_steps must be positive")
    if n_paths <= 0:
        raise ValueError("n_paths must be positive")

    rng = np.random.default_rng(seed)
    increments = rng.choice([-1, 1], size=(n_steps, n_paths))
    paths = np.vstack([np.zeros((1, n_paths), dtype=int), np.cumsum(increments, axis=0)])
    return pd.DataFrame(paths, index=np.arange(n_steps + 1), columns=[f"path_{i}" for i in range(n_paths)])


def scaled_random_walk(paths: pd.DataFrame) -> pd.DataFrame:
    """Apply diffusive scaling S_k / sqrt(n) to random walk paths.

    For a walk with n increments, the scaled terminal value S_n / sqrt(n) has
    variance approximately one. Under linear interpolation, this is the object
    appearing in the Donsker-style convergence intuition.
    """
    n_steps = len(paths.index) - 1
    if n_steps <= 0:
        raise ValueError("paths must contain at least one increment")
    scaled = paths.astype(float) / np.sqrt(n_steps)
    scaled.index = paths.index / n_steps
    scaled.index.name = "t"
    return scaled


def random_walk_terminal_distribution(n_steps: int, n_paths: int, seed: int | None = None) -> pd.Series:
    """Return terminal values S_n from independent symmetric random walks."""
    paths = symmetric_random_walk(n_steps=n_steps, n_paths=n_paths, seed=seed)
    terminal = paths.iloc[-1].rename("S_n")
    return terminal


def first_hitting_time(path: pd.Series | np.ndarray, upper: float, lower: float | None = None) -> int:
    """Return the first time a path exits an interval.

    If lower is None, the lower boundary is -upper. If the boundary is never
    reached, the final index is returned. This makes the time bounded by the
    simulation horizon.
    """
    arr = np.asarray(path)
    if lower is None:
        lower = -upper
    hits = np.where((arr >= upper) | (arr <= lower))[0]
    if len(hits) == 0:
        return len(arr) - 1
    return int(hits[0])


def hitting_times(paths: pd.DataFrame, upper: float, lower: float | None = None) -> pd.Series:
    """Compute first hitting times path-by-path."""
    return paths.apply(lambda col: first_hitting_time(col.values, upper=upper, lower=lower), axis=0).rename("tau")
