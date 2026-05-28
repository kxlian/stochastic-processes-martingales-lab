"""Run the full Stochastic Processes & Martingales Lab analysis."""

from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "src"))

import pandas as pd

from stochastic_lab.random_walk import symmetric_random_walk, scaled_random_walk
from stochastic_lab.stopping_times import bounded_first_exit_time, terminal_at_stopping_time
from stochastic_lab.martingales import exponential_martingale, empirical_martingale_means, optional_stopping_summary
from stochastic_lab.brownian_motion import simulate_brownian_motion, quadratic_variation, quadratic_variation_by_time
from stochastic_lab.diagnostics import convergence_table, terminal_summary
from stochastic_lab.plotting import (
    plot_random_walk_scaling,
    plot_optional_stopping,
    plot_quadratic_variation_convergence,
    plot_brownian_paths,
    plot_stochastic_dashboard,
)
from stochastic_lab.report import write_markdown_summary


def main() -> None:
    data_dir = ROOT / "data"
    figures_dir = ROOT / "figures"
    reports_dir = ROOT / "reports"
    for d in [data_dir, figures_dir, reports_dir]:
        d.mkdir(exist_ok=True)

    # Random walk and martingale experiment
    walks = symmetric_random_walk(n_steps=500, n_paths=2000, seed=42)
    scaled_walks = scaled_random_walk(walks)
    stopping_times = bounded_first_exit_time(walks, boundary=12, max_time=500)
    stopped_values = terminal_at_stopping_time(walks, stopping_times)
    optional_summary = optional_stopping_summary(walks, stopping_times)

    exp_m = exponential_martingale(walks, theta=0.08)
    exp_m_means = empirical_martingale_means(exp_m)

    # Brownian motion and quadratic variation
    brownian = simulate_brownian_motion(n_steps=500, n_paths=2000, T=1.0, seed=7)
    qv_by_time = quadratic_variation_by_time(brownian)

    qv_rows = []
    for i, n_steps in enumerate([25, 50, 100, 250, 500, 1000]):
        bm = simulate_brownian_motion(n_steps=n_steps, n_paths=1500, T=1.0, seed=100 + i)
        qv = quadratic_variation(bm)
        qv_rows.append(
            {
                "n_steps": n_steps,
                "mean_qv": float(qv.mean()),
                "std_qv": float(qv.std(ddof=1)),
                "target_T": 1.0,
            }
        )
    qv_table = pd.DataFrame(qv_rows)

    conv = convergence_table(step_counts=[25, 50, 100, 250, 500, 1000], n_paths=2500, seed=20)

    # Persist data
    scaled_walks.iloc[:, :25].to_csv(data_dir / "scaled_random_walk_sample.csv")
    brownian.iloc[:, :25].to_csv(data_dir / "brownian_motion_sample.csv")
    stopping_times.to_csv(data_dir / "stopping_times.csv")
    stopped_values.to_csv(data_dir / "stopped_values.csv")
    optional_summary.to_csv(data_dir / "optional_stopping_summary.csv", index=False)
    qv_table.to_csv(data_dir / "quadratic_variation_convergence.csv", index=False)
    conv.to_csv(data_dir / "random_walk_scaling_convergence.csv", index=False)
    terminal_summary(scaled_walks.iloc[-1]).to_csv(data_dir / "scaled_terminal_summary.csv", index=False)

    # Figures
    plot_random_walk_scaling(scaled_walks, figures_dir / "random_walk_scaling.png")
    plot_optional_stopping(stopped_values, figures_dir / "optional_stopping.png")
    plot_quadratic_variation_convergence(qv_table, figures_dir / "quadratic_variation_convergence.png")
    plot_brownian_paths(brownian, figures_dir / "brownian_motion_paths.png")
    plot_stochastic_dashboard(
        scaled_paths=scaled_walks,
        brownian_paths=brownian,
        qv_by_time=qv_by_time,
        martingale_means=exp_m_means,
        output_path=figures_dir / "stochastic_processes_dashboard.png",
    )

    # Social preview mirrors the dashboard for GitHub profile use
    (ROOT / "assets").mkdir(exist_ok=True)
    (ROOT / "assets" / "social_preview.png").write_bytes((figures_dir / "stochastic_processes_dashboard.png").read_bytes())

    write_markdown_summary(
        reports_dir / "stochastic_processes_summary.md",
        optional_stopping=optional_summary,
        qv_table=qv_table,
        convergence=conv,
    )

    print("Stochastic Processes & Martingales Lab analysis complete.")
    print(f"Wrote outputs to: {data_dir}, {figures_dir}, {reports_dir}")


if __name__ == "__main__":
    main()
