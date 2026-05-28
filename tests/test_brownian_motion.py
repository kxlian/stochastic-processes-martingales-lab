import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from stochastic_lab.brownian_motion import simulate_brownian_motion, quadratic_variation


def test_brownian_motion_shape_and_initial_value():
    paths = simulate_brownian_motion(n_steps=100, n_paths=3, T=1.0, seed=21)
    assert paths.shape == (101, 3)
    assert (paths.iloc[0] == 0.0).all()


def test_brownian_quadratic_variation_near_time_horizon():
    paths = simulate_brownian_motion(n_steps=1000, n_paths=2000, T=1.0, seed=22)
    qv = quadratic_variation(paths)
    assert 0.94 < qv.mean() < 1.06
