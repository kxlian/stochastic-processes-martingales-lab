import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

import numpy as np

from stochastic_lab.random_walk import symmetric_random_walk, scaled_random_walk


def test_symmetric_random_walk_shape_and_start():
    paths = symmetric_random_walk(n_steps=10, n_paths=4, seed=1)
    assert paths.shape == (11, 4)
    assert (paths.iloc[0] == 0).all()


def test_random_walk_increments_are_plus_or_minus_one():
    paths = symmetric_random_walk(n_steps=20, n_paths=5, seed=2)
    increments = paths.diff().dropna().to_numpy().ravel()
    assert set(np.unique(increments)).issubset({-1, 1})


def test_scaled_terminal_variance_is_reasonable():
    paths = symmetric_random_walk(n_steps=400, n_paths=3000, seed=3)
    scaled = scaled_random_walk(paths)
    terminal_var = scaled.iloc[-1].var(ddof=1)
    assert 0.85 < terminal_var < 1.15
