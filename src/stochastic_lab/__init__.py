"""Stochastic Processes & Martingales Lab.

A small research-oriented Python package for simulating random walks,
martingales, stopping times, quadratic variation, and Brownian motion.
"""

from stochastic_lab.random_walk import symmetric_random_walk, scaled_random_walk
from stochastic_lab.stopping_times import bounded_first_exit_time, terminal_at_stopping_time
from stochastic_lab.martingales import (
    exponential_martingale,
    empirical_martingale_means,
    optional_stopping_summary,
)
from stochastic_lab.brownian_motion import (
    simulate_brownian_motion,
    quadratic_variation,
    quadratic_variation_by_time,
)

__all__ = [
    "symmetric_random_walk",
    "scaled_random_walk",
    "bounded_first_exit_time",
    "terminal_at_stopping_time",
    "exponential_martingale",
    "empirical_martingale_means",
    "optional_stopping_summary",
    "simulate_brownian_motion",
    "quadratic_variation",
    "quadratic_variation_by_time",
]
