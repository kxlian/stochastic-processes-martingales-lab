import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from stochastic_lab.random_walk import symmetric_random_walk
from stochastic_lab.martingales import exponential_martingale, stopped_process, optional_stopping_summary
from stochastic_lab.stopping_times import bounded_first_exit_time


def test_exponential_martingale_starts_at_one():
    paths = symmetric_random_walk(n_steps=50, n_paths=100, seed=10)
    m = exponential_martingale(paths, theta=0.1)
    assert (m.iloc[0] == 1.0).all()


def test_exponential_martingale_mean_approximately_one():
    paths = symmetric_random_walk(n_steps=100, n_paths=5000, seed=11)
    m = exponential_martingale(paths, theta=0.05)
    terminal_mean = m.iloc[-1].mean()
    assert 0.95 < terminal_mean < 1.05


def test_stopped_process_is_constant_after_stopping():
    paths = symmetric_random_walk(n_steps=60, n_paths=20, seed=12)
    tau = bounded_first_exit_time(paths, boundary=4, max_time=60)
    stopped = stopped_process(paths, tau)
    for col in stopped.columns:
        t = int(tau.loc[col])
        assert (stopped.loc[t:, col] == stopped.loc[t, col]).all()


def test_optional_stopping_mean_close_to_zero():
    paths = symmetric_random_walk(n_steps=200, n_paths=5000, seed=13)
    tau = bounded_first_exit_time(paths, boundary=8, max_time=200)
    summary = optional_stopping_summary(paths, tau)
    assert abs(summary.loc[0, "stopped_mean"]) < 0.25
