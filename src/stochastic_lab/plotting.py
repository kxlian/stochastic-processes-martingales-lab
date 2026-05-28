"""Plotting functions for the stochastic processes lab."""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


def _ensure(path: str | Path) -> Path:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    return path


def plot_random_walk_scaling(scaled_paths: pd.DataFrame, output_path: str | Path, max_paths: int = 12) -> None:
    fig, ax = plt.subplots(figsize=(9, 5))
    scaled_paths.iloc[:, :max_paths].plot(ax=ax, legend=False, linewidth=1.2)
    ax.axhline(0, linewidth=0.8)
    ax.set_title("Diffusively Scaled Random Walk Paths")
    ax.set_xlabel("t")
    ax.set_ylabel("S_[nt] / sqrt(n)")
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(_ensure(output_path), dpi=180)
    plt.close(fig)


def plot_optional_stopping(stopped_values: pd.Series, output_path: str | Path) -> None:
    fig, ax = plt.subplots(figsize=(8, 5))
    stopped_values.value_counts().sort_index().plot(kind="bar", ax=ax)
    ax.axhline(0, linewidth=0.8)
    ax.set_title("Distribution of Stopped Random Walk Values")
    ax.set_xlabel("S_tau")
    ax.set_ylabel("Frequency")
    ax.grid(True, axis="y", alpha=0.3)
    fig.tight_layout()
    fig.savefig(_ensure(output_path), dpi=180)
    plt.close(fig)


def plot_quadratic_variation_convergence(qv_table: pd.DataFrame, output_path: str | Path) -> None:
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(qv_table["n_steps"], qv_table["mean_qv"], marker="o", label="Mean quadratic variation")
    ax.axhline(qv_table["target_T"].iloc[0], linestyle="--", linewidth=1.0, label="Target T")
    ax.set_xscale("log")
    ax.set_title("Quadratic Variation Convergence")
    ax.set_xlabel("Number of time steps")
    ax.set_ylabel("Average sum of squared increments")
    ax.grid(True, alpha=0.3)
    ax.legend()
    fig.tight_layout()
    fig.savefig(_ensure(output_path), dpi=180)
    plt.close(fig)


def plot_brownian_paths(paths: pd.DataFrame, output_path: str | Path, max_paths: int = 12) -> None:
    fig, ax = plt.subplots(figsize=(9, 5))
    paths.iloc[:, :max_paths].plot(ax=ax, legend=False, linewidth=1.2)
    ax.axhline(0, linewidth=0.8)
    ax.set_title("Simulated Brownian Motion Paths")
    ax.set_xlabel("t")
    ax.set_ylabel("W_t")
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(_ensure(output_path), dpi=180)
    plt.close(fig)


def plot_stochastic_dashboard(
    scaled_paths: pd.DataFrame,
    brownian_paths: pd.DataFrame,
    qv_by_time: pd.DataFrame,
    martingale_means: pd.Series,
    output_path: str | Path,
) -> None:
    fig, axes = plt.subplots(2, 2, figsize=(12, 8))

    scaled_paths.iloc[:, :8].plot(ax=axes[0, 0], legend=False, linewidth=1.1)
    axes[0, 0].set_title("Scaled Random Walk")
    axes[0, 0].set_xlabel("t")
    axes[0, 0].grid(True, alpha=0.3)

    brownian_paths.iloc[:, :8].plot(ax=axes[0, 1], legend=False, linewidth=1.1)
    axes[0, 1].set_title("Brownian Motion")
    axes[0, 1].set_xlabel("t")
    axes[0, 1].grid(True, alpha=0.3)

    qv_by_time.iloc[:, :12].plot(ax=axes[1, 0], legend=False, linewidth=1.0)
    axes[1, 0].plot(qv_by_time.index, qv_by_time.index, linestyle="--", linewidth=1.0)
    axes[1, 0].set_title("Cumulative Quadratic Variation")
    axes[1, 0].set_xlabel("t")
    axes[1, 0].grid(True, alpha=0.3)

    martingale_means.plot(ax=axes[1, 1], linewidth=1.4)
    axes[1, 1].axhline(1.0, linestyle="--", linewidth=1.0)
    axes[1, 1].set_title("Exponential Martingale: Empirical Mean")
    axes[1, 1].set_xlabel("time")
    axes[1, 1].set_ylabel("mean across paths")
    axes[1, 1].grid(True, alpha=0.3)

    fig.suptitle("Stochastic Processes & Martingales Lab", fontsize=14)
    fig.tight_layout(rect=[0, 0, 1, 0.97])
    fig.savefig(_ensure(output_path), dpi=180)
    plt.close(fig)
