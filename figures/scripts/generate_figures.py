from __future__ import annotations

import csv
import json
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


ROOT = Path(__file__).resolve().parents[2]
RUN_ROOT = ROOT / ".aris" / "runs" / "2026-03-24-factorized-gap-in-discrete-diffu"
FIG_ROOT = ROOT / "figures"

PALETTE = {
    "factorized": "#546A7B",
    "adrd": "#C8553D",
    "micro": "#2A7F62",
    "coupled": "#F0A202",
    "random": "#7E6B8F",
    "accent": "#214E7A",
}


def load_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def ensure_output_dir() -> None:
    FIG_ROOT.mkdir(parents=True, exist_ok=True)


def save(fig: plt.Figure, name: str) -> None:
    fig.tight_layout()
    fig.savefig(FIG_ROOT / name, bbox_inches="tight")
    plt.close(fig)


def plot_adrd_overview() -> None:
    fig, ax = plt.subplots(figsize=(10.5, 3.6))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    def box(x: float, y: float, w: float, h: float, text: str, color: str) -> None:
        patch = FancyBboxPatch(
            (x, y),
            w,
            h,
            boxstyle="round,pad=0.015,rounding_size=0.025",
            linewidth=1.5,
            edgecolor=color,
            facecolor="white",
        )
        ax.add_patch(patch)
        ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=10)

    box(0.03, 0.37, 0.17, 0.24, "Masked sequence\nand unresolved spans", PALETTE["accent"])
    box(0.25, 0.37, 0.17, 0.24, "Dependency estimator\ncopy / progression score", PALETTE["accent"])
    box(0.47, 0.37, 0.17, 0.24, "Budgeted router\nselect cheapest viable mode", PALETTE["adrd"])
    box(0.71, 0.68, 0.23, 0.16, "factorized\ncheap global update", PALETTE["factorized"])
    box(0.71, 0.42, 0.23, 0.16, "coupled-local\nshort joint span", PALETTE["coupled"])
    box(0.71, 0.16, 0.23, 0.16, "micro-sequential\nsmall ordered knot", PALETTE["micro"])
    box(0.47, 0.08, 0.17, 0.14, "Budget controller\ncap expensive tokens", PALETTE["random"])

    arrow = dict(arrowstyle="-|>", linewidth=1.3, color="#333333")
    ax.annotate("", xy=(0.25, 0.49), xytext=(0.20, 0.49), arrowprops=arrow)
    ax.annotate("", xy=(0.47, 0.49), xytext=(0.42, 0.49), arrowprops=arrow)
    ax.annotate("", xy=(0.71, 0.76), xytext=(0.64, 0.54), arrowprops=arrow)
    ax.annotate("", xy=(0.71, 0.50), xytext=(0.64, 0.50), arrowprops=arrow)
    ax.annotate("", xy=(0.71, 0.24), xytext=(0.64, 0.44), arrowprops=arrow)
    ax.annotate("", xy=(0.55, 0.22), xytext=(0.55, 0.37), arrowprops=arrow)

    ax.text(
        0.03,
        0.92,
        "ADRD on the local scaffold routes only high-risk spans to more expensive dependency handlers.",
        fontsize=11,
        fontweight="bold",
    )
    save(fig, "adrd_overview.pdf")


def plot_budget_frontier(review_rows: list[dict[str, str]]) -> None:
    by_id = {row["run_id"]: row for row in review_rows}
    series = [
        ("factorized_logging", "0%"),
        ("three_mode_budget05", "5%"),
        ("three_mode_budget10", "10%"),
        ("three_mode_span4", "20% cap"),
    ]
    x = [float(by_id[run]["average_expensive_token_fraction"]) * 100 for run, _ in series]
    token = [float(by_id[run]["token_accuracy"]) for run, _ in series]
    dep = [float(by_id[run]["dependency_accuracy"]) for run, _ in series]
    labels = [label for _, label in series]

    fig, axes = plt.subplots(1, 2, figsize=(10.2, 3.8))
    for ax, values, ylabel, color in [
        (axes[0], token, "Token accuracy", PALETTE["adrd"]),
        (axes[1], dep, "Dependency accuracy", PALETTE["accent"]),
    ]:
        ax.plot(x, values, marker="o", linewidth=2.5, color=color)
        for x_val, y_val, label in zip(x, values, labels):
            ax.annotate(label, (x_val, y_val), textcoords="offset points", xytext=(0, 8), ha="center", fontsize=8)
        ax.set_xlabel("Actual expensive-token fraction (%)")
        ax.set_ylabel(ylabel)
        ax.set_ylim(0.3, 0.72)
        ax.grid(alpha=0.25, linestyle="--")

    axes[0].set_title("Budget frontier")
    axes[1].set_title("Dependency recovery")
    save(fig, "budget_frontier.pdf")


def plot_same_budget(review_rows: list[dict[str, str]]) -> None:
    by_id = {row["run_id"]: row for row in review_rows}
    order = [
        ("factorized_logging", "Factorized", PALETTE["factorized"]),
        ("budgeted_micro_span4", "Micro only", PALETTE["micro"]),
        ("budgeted_coupled_span4", "Coupled only", PALETTE["coupled"]),
        ("random_span4", "Random", PALETTE["random"]),
        ("three_mode_span4", "ADRD", PALETTE["adrd"]),
    ]
    x = list(range(len(order)))
    token = [float(by_id[run]["token_accuracy"]) for run, _, _ in order]
    group = [float(by_id[run]["dependency_group_accuracy"]) for run, _, _ in order]
    colors = [color for _, _, color in order]
    labels = [label for _, label, _ in order]

    fig, ax = plt.subplots(figsize=(8.6, 4.2))
    width = 0.36
    ax.bar([i - width / 2 for i in x], token, width=width, color=colors, alpha=0.95, label="Token accuracy")
    ax.bar([i + width / 2 for i in x], group, width=width, color=colors, alpha=0.45, label="Dependency-group accuracy")
    ax.set_xticks(x, labels)
    ax.set_ylabel("Accuracy")
    ax.set_ylim(0, 0.78)
    ax.set_title("Relaxed span-4 budget: ADRD remains competitive, but coupled-only is strongest")
    ax.grid(axis="y", alpha=0.25, linestyle="--")
    ax.legend(frameon=False, ncol=2)
    save(fig, "same_budget_comparison.pdf")


def plot_long_context(review_rows: list[dict[str, str]]) -> None:
    by_id = {row["run_id"]: row for row in review_rows}
    runs = [
        ("long_context_factorized", "Factorized", PALETTE["factorized"]),
        ("long_context_span4", "ADRD", PALETTE["adrd"]),
    ]
    token = [float(by_id[run]["token_accuracy"]) for run, _, _ in runs]
    dep = [float(by_id[run]["dependency_accuracy"]) for run, _, _ in runs]
    labels = [label for _, label, _ in runs]
    colors = [color for _, _, color in runs]

    fig, ax = plt.subplots(figsize=(6.6, 4.0))
    width = 0.34
    x = list(range(len(runs)))
    ax.bar([i - width / 2 for i in x], token, width=width, color=colors, alpha=0.95, label="Token accuracy")
    ax.bar([i + width / 2 for i in x], dep, width=width, color=colors, alpha=0.50, label="Dependency accuracy")
    ax.set_xticks(x, labels)
    ax.set_ylim(0.3, 0.72)
    ax.set_ylabel("Accuracy")
    ax.set_title("Length-40 synthetic stress test")
    ax.grid(axis="y", alpha=0.25, linestyle="--")
    ax.legend(frameon=False)
    save(fig, "long_context.pdf")


def write_tables(main_rows: list[dict[str, str]], review_payload: dict, span4_payload: dict) -> None:
    main_order = ["factorized_logging", "two_mode_budget10", "three_mode_span4"]
    by_id = {row["run_id"]: row for row in main_rows}
    main_lines = [
        "\\begin{tabular}{lcccc}",
        "\\toprule",
        "System & Token acc. & Dep. acc. & Non-dep. acc. & Expensive frac.\\\\",
        "\\midrule",
    ]
    labels = {
        "factorized_logging": "Factorized",
        "two_mode_budget10": "Two-mode 10\\%",
        "three_mode_span4": "ADRD span-4",
    }
    for run_id in main_order:
        row = by_id[run_id]
        main_lines.append(
            f"{labels[run_id]} & {float(row['token_accuracy']):.4f} & {float(row['dependency_accuracy']):.4f} "
            f"& {float(row['non_dependency_accuracy']):.4f} & {100*float(row['average_expensive_token_fraction']):.2f}\\%\\\\"
        )
    main_lines.extend(["\\bottomrule", "\\end{tabular}"])
    (FIG_ROOT / "main_results_table.tex").write_text("\n".join(main_lines) + "\n", encoding="utf-8")

    metrics = span4_payload["metrics"]
    mode_lines = [
        "\\begin{tabular}{lccc}",
        "\\toprule",
        "Mode & Token count & Group count & Avg. span\\\\",
        "\\midrule",
    ]
    for key, label in [("factorized", "Factorized"), ("coupled-local", "Coupled-local"), ("micro-sequential", "Micro-sequential")]:
        mode_lines.append(
            f"{label} & {metrics['mode_token_counts'][key]} & {metrics['mode_group_counts'][key]} & "
            f"{metrics['average_span_size_by_mode'][key]:.2f}\\\\"
        )
    mode_lines.extend(["\\bottomrule", "\\end{tabular}"])
    (FIG_ROOT / "mode_usage_table.tex").write_text("\n".join(mode_lines) + "\n", encoding="utf-8")

    includes = [
        "\\newcommand{\\figOverviewPath}{../figures/adrd_overview.pdf}",
        "\\newcommand{\\figBudgetFrontierPath}{../figures/budget_frontier.pdf}",
        "\\newcommand{\\figSameBudgetPath}{../figures/same_budget_comparison.pdf}",
        "\\newcommand{\\figLongContextPath}{../figures/long_context.pdf}",
        "\\newcommand{\\tableMainResultsPath}{../figures/main_results_table.tex}",
        "\\newcommand{\\tableModeUsagePath}{../figures/mode_usage_table.tex}",
    ]
    (FIG_ROOT / "latex_includes.tex").write_text("\n".join(includes) + "\n", encoding="utf-8")


def main() -> None:
    ensure_output_dir()
    review_rows = load_csv(RUN_ROOT / "artifacts" / "auto-review-loop" / "review_suite.csv")
    main_rows = load_csv(RUN_ROOT / "artifacts" / "experiment-bridge" / "suite_summary.csv")
    review_payload = load_json(RUN_ROOT / "artifacts" / "auto-review-loop" / "review_suite.json")
    span4_payload = load_json(RUN_ROOT / "artifacts" / "auto-review-loop" / "three_mode_span4.json")

    plot_adrd_overview()
    plot_budget_frontier(review_rows)
    plot_same_budget(review_rows)
    plot_long_context(review_rows)
    write_tables(main_rows, review_payload, span4_payload)


if __name__ == "__main__":
    main()
