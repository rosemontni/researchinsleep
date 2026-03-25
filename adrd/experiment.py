from __future__ import annotations

import argparse
import csv
import json
from dataclasses import asdict
from pathlib import Path
from typing import Any

from adrd.config import BudgetConfig, ExperimentConfig, Mode
from adrd.core import DecodeMetrics, evaluate
from adrd.synthetic import make_dataset


PRESET_ORDER = ["factorized_logging", "two_mode_budget10", "three_mode_span4"]
REVIEW_SUITE_ORDER = [
    "factorized_logging",
    "budgeted_micro_budget10",
    "budgeted_coupled_budget10",
    "random_budget10",
    "three_mode_budget05",
    "three_mode_budget10",
    "budgeted_micro_span4",
    "budgeted_coupled_span4",
    "random_span4",
    "three_mode_span4",
    "long_context_factorized",
    "long_context_span4",
]

PRESETS: dict[str, dict[str, Any]] = {
    "factorized_logging": {
        "description": "Factorized baseline with per-token confidence and error logging.",
        "strategy": "factorized",
        "config": {
            "dataset_size": 192,
            "seq_len": 24,
            "diffusion_steps": 4,
            "seed": 7,
            "dependency_probability": 0.8,
            "min_dependency_span": 2,
            "max_dependency_span": 5,
            "log_examples": 3,
        },
        "budget": {},
        "plan_block": "Block 1: Feasibility",
        "success_hint": "Use as the sanity baseline and instrumentation reference.",
    },
    "two_mode_budget10": {
        "description": "Two-mode ADRD with a strict 10% expensive-token budget.",
        "strategy": "adrd",
        "config": {
            "dataset_size": 192,
            "seq_len": 24,
            "diffusion_steps": 4,
            "seed": 7,
            "dependency_probability": 0.8,
            "min_dependency_span": 2,
            "max_dependency_span": 5,
            "allowed_modes": ("factorized", "micro-sequential"),
            "log_examples": 3,
        },
        "budget": {
            "max_coupled_groups_per_step": 0,
            "max_micro_seq_groups_per_step": 2,
            "max_non_factorized_fraction": 0.10,
            "max_micro_seq_tokens_per_step": 2,
        },
        "plan_block": "Block 1: Feasibility",
        "success_hint": "Quality should improve over factorized while keeping expensive routing sparse.",
    },
    "budgeted_micro_budget10": {
        "description": "Budget-matched micro-sequential-only routing under a strict 10% expensive-token budget.",
        "strategy": "budgeted-micro-sequential",
        "config": {
            "dataset_size": 192,
            "seq_len": 24,
            "diffusion_steps": 4,
            "seed": 7,
            "dependency_probability": 0.8,
            "min_dependency_span": 2,
            "max_dependency_span": 5,
            "allowed_modes": ("factorized", "micro-sequential"),
            "log_examples": 3,
        },
        "budget": {
            "max_coupled_groups_per_step": 0,
            "max_micro_seq_groups_per_step": 2,
            "max_non_factorized_fraction": 0.10,
            "max_micro_seq_tokens_per_step": 2,
        },
        "plan_block": "Review Loop: Matched-Budget Ablations",
        "success_hint": "Tests whether the router helps beyond always choosing micro-sequential when budget permits.",
    },
    "budgeted_coupled_budget10": {
        "description": "Budget-matched coupled-local-only routing under a strict 10% expensive-token budget.",
        "strategy": "budgeted-coupled-local",
        "config": {
            "dataset_size": 192,
            "seq_len": 24,
            "diffusion_steps": 4,
            "seed": 7,
            "dependency_probability": 0.8,
            "min_dependency_span": 2,
            "max_dependency_span": 5,
            "allowed_modes": ("factorized", "coupled-local"),
            "max_coupled_span_len": 4,
            "log_examples": 3,
        },
        "budget": {
            "max_coupled_groups_per_step": 2,
            "max_micro_seq_groups_per_step": 0,
            "max_non_factorized_fraction": 0.10,
            "max_coupled_tokens_per_step": 2,
        },
        "plan_block": "Review Loop: Matched-Budget Ablations",
        "success_hint": "Tests whether the router helps beyond always choosing coupled-local when budget permits.",
    },
    "random_budget10": {
        "description": "Random matched-budget routing over coupled-local and micro-sequential decisions.",
        "strategy": "random-budgeted",
        "config": {
            "dataset_size": 192,
            "seq_len": 24,
            "diffusion_steps": 4,
            "seed": 7,
            "dependency_probability": 0.8,
            "min_dependency_span": 2,
            "max_dependency_span": 5,
            "allowed_modes": ("factorized", "coupled-local", "micro-sequential"),
            "max_coupled_span_len": 4,
            "log_examples": 3,
        },
        "budget": {
            "max_coupled_groups_per_step": 2,
            "max_micro_seq_groups_per_step": 1,
            "max_non_factorized_fraction": 0.10,
            "max_coupled_tokens_per_step": 2,
            "max_micro_seq_tokens_per_step": 2,
        },
        "plan_block": "Review Loop: Matched-Budget Ablations",
        "success_hint": "Tests whether ADRD beats a non-adaptive routing policy under the same budget.",
    },
    "three_mode_budget05": {
        "description": "Full ADRD with a stricter 5% non-factorized token budget.",
        "strategy": "adrd",
        "config": {
            "dataset_size": 192,
            "seq_len": 24,
            "diffusion_steps": 4,
            "seed": 7,
            "dependency_probability": 0.8,
            "min_dependency_span": 2,
            "max_dependency_span": 5,
            "allowed_modes": ("factorized", "coupled-local", "micro-sequential"),
            "max_coupled_span_len": 4,
            "log_examples": 3,
        },
        "budget": {
            "max_coupled_groups_per_step": 1,
            "max_micro_seq_groups_per_step": 1,
            "max_non_factorized_fraction": 0.05,
            "max_coupled_tokens_per_step": 1,
            "max_micro_seq_tokens_per_step": 1,
        },
        "plan_block": "Review Loop: Budget Sweep",
        "success_hint": "A stricter-budget check for compute-quality tradeoffs.",
    },
    "three_mode_budget10": {
        "description": "Full ADRD with a matched 10% non-factorized token budget.",
        "strategy": "adrd",
        "config": {
            "dataset_size": 192,
            "seq_len": 24,
            "diffusion_steps": 4,
            "seed": 7,
            "dependency_probability": 0.8,
            "min_dependency_span": 2,
            "max_dependency_span": 5,
            "allowed_modes": ("factorized", "coupled-local", "micro-sequential"),
            "max_coupled_span_len": 4,
            "log_examples": 3,
        },
        "budget": {
            "max_coupled_groups_per_step": 1,
            "max_micro_seq_groups_per_step": 1,
            "max_non_factorized_fraction": 0.10,
            "max_coupled_tokens_per_step": 2,
            "max_micro_seq_tokens_per_step": 2,
        },
        "plan_block": "Review Loop: Matched-Budget Ablations",
        "success_hint": "Primary apples-to-apples ADRD comparison for the auto-review loop.",
    },
    "budgeted_micro_span4": {
        "description": "Micro-sequential-only routing under the relaxed span-4 review budget.",
        "strategy": "budgeted-micro-sequential",
        "config": {
            "dataset_size": 192,
            "seq_len": 24,
            "diffusion_steps": 4,
            "seed": 7,
            "dependency_probability": 0.8,
            "min_dependency_span": 2,
            "max_dependency_span": 5,
            "allowed_modes": ("factorized", "micro-sequential"),
            "log_examples": 3,
        },
        "budget": {
            "max_coupled_groups_per_step": 0,
            "max_micro_seq_groups_per_step": 2,
            "max_non_factorized_fraction": 0.20,
            "max_micro_seq_tokens_per_step": 4,
        },
        "plan_block": "Review Loop: Matched-Budget Ablations",
        "success_hint": "Same global budget as the best span-4 run, but without coupled-local routing.",
    },
    "budgeted_coupled_span4": {
        "description": "Coupled-local-only routing under the relaxed span-4 review budget.",
        "strategy": "budgeted-coupled-local",
        "config": {
            "dataset_size": 192,
            "seq_len": 24,
            "diffusion_steps": 4,
            "seed": 7,
            "dependency_probability": 0.8,
            "min_dependency_span": 2,
            "max_dependency_span": 5,
            "allowed_modes": ("factorized", "coupled-local"),
            "max_coupled_span_len": 4,
            "log_examples": 3,
        },
        "budget": {
            "max_coupled_groups_per_step": 2,
            "max_micro_seq_groups_per_step": 0,
            "max_non_factorized_fraction": 0.20,
            "max_coupled_tokens_per_step": 4,
        },
        "plan_block": "Review Loop: Matched-Budget Ablations",
        "success_hint": "Same global budget as the best span-4 run, but without micro-sequential routing.",
    },
    "random_span4": {
        "description": "Random routing under the relaxed span-4 review budget.",
        "strategy": "random-budgeted",
        "config": {
            "dataset_size": 192,
            "seq_len": 24,
            "diffusion_steps": 4,
            "seed": 7,
            "dependency_probability": 0.8,
            "min_dependency_span": 2,
            "max_dependency_span": 5,
            "allowed_modes": ("factorized", "coupled-local", "micro-sequential"),
            "max_coupled_span_len": 4,
            "log_examples": 3,
        },
        "budget": {
            "max_coupled_groups_per_step": 2,
            "max_micro_seq_groups_per_step": 1,
            "max_non_factorized_fraction": 0.20,
            "max_coupled_tokens_per_step": 4,
            "max_micro_seq_tokens_per_step": 2,
        },
        "plan_block": "Review Loop: Matched-Budget Ablations",
        "success_hint": "Same global budget as the best span-4 run, but without the heuristic router.",
    },
    "three_mode_span4": {
        "description": "Full ADRD with coupled-local spans capped at length 4.",
        "strategy": "adrd",
        "config": {
            "dataset_size": 192,
            "seq_len": 24,
            "diffusion_steps": 4,
            "seed": 7,
            "dependency_probability": 0.8,
            "min_dependency_span": 2,
            "max_dependency_span": 5,
            "allowed_modes": ("factorized", "coupled-local", "micro-sequential"),
            "max_coupled_span_len": 4,
            "log_examples": 3,
        },
        "budget": {
            "max_coupled_groups_per_step": 2,
            "max_micro_seq_groups_per_step": 1,
            "max_non_factorized_fraction": 0.20,
            "max_coupled_tokens_per_step": 4,
            "max_micro_seq_tokens_per_step": 2,
        },
        "plan_block": "Block 2: Add Coupled-Local Mode",
        "success_hint": "Should outperform the two-mode run at matched diffusion steps.",
    },
    "long_context_factorized": {
        "description": "Longer-context factorized baseline for dependency-heavy spans.",
        "strategy": "factorized",
        "config": {
            "dataset_size": 192,
            "seq_len": 40,
            "diffusion_steps": 4,
            "seed": 11,
            "dependency_probability": 0.9,
            "min_dependency_span": 3,
            "max_dependency_span": 7,
            "log_examples": 3,
        },
        "budget": {},
        "plan_block": "Review Loop: Stress Tests",
        "success_hint": "Reference point for the long-context stress setting.",
    },
    "long_context_span4": {
        "description": "Longer-context ADRD with coupled-local spans capped at length 4.",
        "strategy": "adrd",
        "config": {
            "dataset_size": 192,
            "seq_len": 40,
            "diffusion_steps": 4,
            "seed": 11,
            "dependency_probability": 0.9,
            "min_dependency_span": 3,
            "max_dependency_span": 7,
            "allowed_modes": ("factorized", "coupled-local", "micro-sequential"),
            "max_coupled_span_len": 4,
            "log_examples": 3,
        },
        "budget": {
            "max_coupled_groups_per_step": 2,
            "max_micro_seq_groups_per_step": 1,
            "max_non_factorized_fraction": 0.15,
            "max_coupled_tokens_per_step": 4,
            "max_micro_seq_tokens_per_step": 2,
        },
        "plan_block": "Review Loop: Stress Tests",
        "success_hint": "Checks whether ADRD keeps its edge on longer, denser dependency spans.",
    },
    "three_mode_span8": {
        "description": "Full ADRD with coupled-local spans capped at length 8.",
        "strategy": "adrd",
        "config": {
            "dataset_size": 192,
            "seq_len": 24,
            "diffusion_steps": 4,
            "seed": 7,
            "dependency_probability": 0.8,
            "min_dependency_span": 2,
            "max_dependency_span": 6,
            "allowed_modes": ("factorized", "coupled-local", "micro-sequential"),
            "max_coupled_span_len": 8,
            "log_examples": 3,
        },
        "budget": {
            "max_coupled_groups_per_step": 2,
            "max_micro_seq_groups_per_step": 1,
            "max_non_factorized_fraction": 0.20,
            "max_coupled_tokens_per_step": 6,
            "max_micro_seq_tokens_per_step": 2,
        },
        "plan_block": "Block 2: Add Coupled-Local Mode",
        "success_hint": "Optional wider-span coupled-local variant for follow-up runs.",
    },
}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run plan-aligned ADRD synthetic experiments.")
    parser.add_argument(
        "--strategy",
        choices=[
            "factorized",
            "coupled-local",
            "micro-sequential",
            "adrd",
            "budgeted-coupled-local",
            "budgeted-micro-sequential",
            "random-budgeted",
        ],
        default=None,
    )
    parser.add_argument("--preset", choices=["suite", "review_suite", *PRESETS.keys()], default=None)
    parser.add_argument("--dataset-size", type=int, default=128)
    parser.add_argument("--seq-len", type=int, default=24)
    parser.add_argument("--diffusion-steps", type=int, default=4)
    parser.add_argument("--seed", type=int, default=7)
    parser.add_argument("--dependency-probability", type=float, default=0.75)
    parser.add_argument("--min-dependency-span", type=int, default=2)
    parser.add_argument("--max-dependency-span", type=int, default=5)
    parser.add_argument(
        "--allowed-modes",
        nargs="+",
        choices=["factorized", "coupled-local", "micro-sequential"],
        default=None,
    )
    parser.add_argument("--max-coupled-span-len", type=int, default=None)
    parser.add_argument("--max-coupled-groups-per-step", type=int, default=2)
    parser.add_argument("--max-micro-seq-groups-per-step", type=int, default=1)
    parser.add_argument("--max-non-factorized-fraction", type=float, default=0.5)
    parser.add_argument("--max-coupled-tokens-per-step", type=int, default=None)
    parser.add_argument("--max-micro-seq-tokens-per-step", type=int, default=None)
    parser.add_argument("--log-examples", type=int, default=5)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--csv-output", type=Path)
    parser.add_argument("--results-dir", type=Path)
    return parser


def _top_error_positions(metrics: DecodeMetrics, limit: int = 5) -> list[dict[str, float]]:
    pairs = sorted(
        ((int(position), rate) for position, rate in metrics.position_error_rates.items()),
        key=lambda item: item[1],
        reverse=True,
    )
    return [
        {"position": position, "error_rate": round(rate, 4)}
        for position, rate in pairs[:limit]
    ]


def _build_config(config_overrides: dict[str, Any], budget_overrides: dict[str, Any]) -> ExperimentConfig:
    budget = BudgetConfig(**budget_overrides)
    return ExperimentConfig(budget=budget, **config_overrides)


def _build_single_run_config(args: argparse.Namespace) -> ExperimentConfig:
    allowed_modes = tuple(args.allowed_modes) if args.allowed_modes else ("factorized", "coupled-local", "micro-sequential")
    budget = BudgetConfig(
        max_coupled_groups_per_step=args.max_coupled_groups_per_step,
        max_micro_seq_groups_per_step=args.max_micro_seq_groups_per_step,
        max_non_factorized_fraction=args.max_non_factorized_fraction,
        max_coupled_tokens_per_step=args.max_coupled_tokens_per_step,
        max_micro_seq_tokens_per_step=args.max_micro_seq_tokens_per_step,
    )
    return ExperimentConfig(
        dataset_size=args.dataset_size,
        seq_len=args.seq_len,
        diffusion_steps=args.diffusion_steps,
        seed=args.seed,
        dependency_probability=args.dependency_probability,
        min_dependency_span=args.min_dependency_span,
        max_dependency_span=args.max_dependency_span,
        allowed_modes=allowed_modes,
        max_coupled_span_len=args.max_coupled_span_len,
        log_examples=args.log_examples,
        budget=budget,
    )


def _result_payload(name: str, description: str, strategy: str, config: ExperimentConfig, metrics: DecodeMetrics) -> dict[str, Any]:
    return {
        "run_id": name,
        "description": description,
        "strategy": strategy,
        "config": asdict(config),
        "metrics": {
            "token_accuracy": round(metrics.token_accuracy, 4),
            "exact_match": round(metrics.exact_match, 4),
            "dependency_group_accuracy": round(metrics.dependency_group_accuracy, 4),
            "dependency_accuracy": round(metrics.dependency_accuracy, 4),
            "non_dependency_accuracy": round(metrics.non_dependency_accuracy, 4),
            "average_expensive_token_fraction": round(metrics.average_expensive_token_fraction, 4),
            "mean_token_confidence": round(metrics.mean_token_confidence, 4),
            "mean_error_confidence": round(metrics.mean_error_confidence, 4),
            "dependency_group_accuracy_by_kind": metrics.dependency_group_accuracy_by_kind,
            "mode_group_counts": metrics.mode_group_counts,
            "mode_token_counts": metrics.mode_token_counts,
            "average_span_size_by_mode": metrics.average_span_size_by_mode,
            "top_error_positions": _top_error_positions(metrics),
        },
        "logged_examples": metrics.logged_examples,
    }


def _write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def _write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    if not rows:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def _run_named_experiment(name: str) -> dict[str, Any]:
    preset = PRESETS[name]
    config = _build_config(preset["config"], preset["budget"])
    dataset = make_dataset(config)
    metrics = evaluate(config, dataset, preset["strategy"], label=name)
    return _result_payload(name, preset["description"], preset["strategy"], config, metrics)


def _summarize_suite(results: list[dict[str, Any]]) -> dict[str, Any]:
    factorized = next(item for item in results if item["run_id"] == "factorized_logging")
    two_mode = next(item for item in results if item["run_id"] == "two_mode_budget10")
    three_mode = next(item for item in results if item["run_id"] == "three_mode_span4")
    return {
        "suite": "initial_plan_runs",
        "runs": results,
        "summary": {
            "baseline_token_accuracy": factorized["metrics"]["token_accuracy"],
            "two_mode_token_accuracy": two_mode["metrics"]["token_accuracy"],
            "three_mode_token_accuracy": three_mode["metrics"]["token_accuracy"],
            "baseline_exact_match": factorized["metrics"]["exact_match"],
            "two_mode_exact_match": two_mode["metrics"]["exact_match"],
            "three_mode_exact_match": three_mode["metrics"]["exact_match"],
            "two_mode_improves_over_baseline": two_mode["metrics"]["token_accuracy"] > factorized["metrics"]["token_accuracy"],
            "three_mode_improves_over_two_mode": three_mode["metrics"]["token_accuracy"] > two_mode["metrics"]["token_accuracy"],
            "two_mode_budget_fraction": two_mode["metrics"]["average_expensive_token_fraction"],
            "three_mode_budget_fraction": three_mode["metrics"]["average_expensive_token_fraction"],
        },
    }


def _summarize_review_suite(results: list[dict[str, Any]]) -> dict[str, Any]:
    by_id = {item["run_id"]: item for item in results}
    factorized = by_id["factorized_logging"]
    matched = by_id["three_mode_budget10"]
    full = by_id["three_mode_span4"]
    long_factorized = by_id["long_context_factorized"]
    long_full = by_id["long_context_span4"]
    return {
        "suite": "review_suite",
        "runs": results,
        "summary": {
            "best_token_accuracy_run": max(results, key=lambda item: item["metrics"]["token_accuracy"])["run_id"],
            "best_dependency_accuracy_run": max(results, key=lambda item: item["metrics"]["dependency_accuracy"])["run_id"],
            "budget05_token_accuracy": by_id["three_mode_budget05"]["metrics"]["token_accuracy"],
            "budget10_token_accuracy": matched["metrics"]["token_accuracy"],
            "budget20_token_accuracy": full["metrics"]["token_accuracy"],
            "budget05_expensive_fraction": by_id["three_mode_budget05"]["metrics"]["average_expensive_token_fraction"],
            "budget10_expensive_fraction": matched["metrics"]["average_expensive_token_fraction"],
            "budget20_expensive_fraction": full["metrics"]["average_expensive_token_fraction"],
            "heuristic10_vs_random_token_gain": round(
                matched["metrics"]["token_accuracy"] - by_id["random_budget10"]["metrics"]["token_accuracy"],
                4,
            ),
            "heuristic10_vs_coupled_budget10_token_gain": round(
                matched["metrics"]["token_accuracy"] - by_id["budgeted_coupled_budget10"]["metrics"]["token_accuracy"],
                4,
            ),
            "heuristic10_vs_micro_budget10_token_gain": round(
                matched["metrics"]["token_accuracy"] - by_id["budgeted_micro_budget10"]["metrics"]["token_accuracy"],
                4,
            ),
            "dependency_group_gain_over_factorized": round(
                matched["metrics"]["dependency_group_accuracy"] - factorized["metrics"]["dependency_group_accuracy"],
                4,
            ),
            "span4_vs_random_token_gain": round(
                full["metrics"]["token_accuracy"] - by_id["random_span4"]["metrics"]["token_accuracy"],
                4,
            ),
            "span4_vs_coupled_token_gain": round(
                full["metrics"]["token_accuracy"] - by_id["budgeted_coupled_span4"]["metrics"]["token_accuracy"],
                4,
            ),
            "span4_vs_micro_token_gain": round(
                full["metrics"]["token_accuracy"] - by_id["budgeted_micro_span4"]["metrics"]["token_accuracy"],
                4,
            ),
            "long_context_token_gain": round(
                long_full["metrics"]["token_accuracy"] - long_factorized["metrics"]["token_accuracy"],
                4,
            ),
            "long_context_dependency_gain": round(
                long_full["metrics"]["dependency_accuracy"] - long_factorized["metrics"]["dependency_accuracy"],
                4,
            ),
        },
    }


def main() -> int:
    args = build_parser().parse_args()

    if args.preset == "suite":
        results = [_run_named_experiment(name) for name in PRESET_ORDER]
        payload = _summarize_suite(results)
        if args.results_dir:
            args.results_dir.mkdir(parents=True, exist_ok=True)
            for item in results:
                _write_json(args.results_dir / f"{item['run_id']}.json", item)
            summary_rows = [
                {
                    "run_id": item["run_id"],
                    "strategy": item["strategy"],
                    "token_accuracy": item["metrics"]["token_accuracy"],
                    "exact_match": item["metrics"]["exact_match"],
                    "dependency_accuracy": item["metrics"]["dependency_accuracy"],
                    "non_dependency_accuracy": item["metrics"]["non_dependency_accuracy"],
                    "average_expensive_token_fraction": item["metrics"]["average_expensive_token_fraction"],
                }
                for item in results
            ]
            _write_csv(args.results_dir / "initial_plan_runs.csv", summary_rows)
            _write_json(args.results_dir / "initial_plan_runs.json", payload)
        if args.output:
            _write_json(args.output, payload)
        if args.csv_output:
            _write_csv(
                args.csv_output,
                [
                    {
                        "run_id": item["run_id"],
                        "strategy": item["strategy"],
                        "token_accuracy": item["metrics"]["token_accuracy"],
                        "exact_match": item["metrics"]["exact_match"],
                        "dependency_accuracy": item["metrics"]["dependency_accuracy"],
                        "non_dependency_accuracy": item["metrics"]["non_dependency_accuracy"],
                        "average_expensive_token_fraction": item["metrics"]["average_expensive_token_fraction"],
                    }
                    for item in results
                ],
            )
        print(json.dumps(payload, indent=2))
        return 0

    if args.preset == "review_suite":
        results = [_run_named_experiment(name) for name in REVIEW_SUITE_ORDER]
        payload = _summarize_review_suite(results)
        if args.results_dir:
            args.results_dir.mkdir(parents=True, exist_ok=True)
            for item in results:
                _write_json(args.results_dir / f"{item['run_id']}.json", item)
            _write_csv(
                args.results_dir / "review_suite.csv",
                [
                    {
                        "run_id": item["run_id"],
                        "strategy": item["strategy"],
                        "token_accuracy": item["metrics"]["token_accuracy"],
                        "dependency_accuracy": item["metrics"]["dependency_accuracy"],
                        "dependency_group_accuracy": item["metrics"]["dependency_group_accuracy"],
                        "non_dependency_accuracy": item["metrics"]["non_dependency_accuracy"],
                        "average_expensive_token_fraction": item["metrics"]["average_expensive_token_fraction"],
                    }
                    for item in results
                ],
            )
            _write_json(args.results_dir / "review_suite.json", payload)
        if args.output:
            _write_json(args.output, payload)
        if args.csv_output:
            _write_csv(
                args.csv_output,
                [
                    {
                        "run_id": item["run_id"],
                        "strategy": item["strategy"],
                        "token_accuracy": item["metrics"]["token_accuracy"],
                        "dependency_accuracy": item["metrics"]["dependency_accuracy"],
                        "dependency_group_accuracy": item["metrics"]["dependency_group_accuracy"],
                        "non_dependency_accuracy": item["metrics"]["non_dependency_accuracy"],
                        "average_expensive_token_fraction": item["metrics"]["average_expensive_token_fraction"],
                    }
                    for item in results
                ],
            )
        print(json.dumps(payload, indent=2))
        return 0

    if args.preset:
        payload = _run_named_experiment(args.preset)
        if args.results_dir:
            _write_json(args.results_dir / f"{args.preset}.json", payload)
        if args.output:
            _write_json(args.output, payload)
        print(json.dumps(payload, indent=2))
        return 0

    strategy = args.strategy or "adrd"
    config = _build_single_run_config(args)
    dataset = make_dataset(config)
    metrics = evaluate(config, dataset, strategy, label=strategy)
    payload = _result_payload("adhoc", "Ad hoc ADRD run.", strategy, config, metrics)
    if args.output:
        _write_json(args.output, payload)
    if args.csv_output:
        _write_csv(
            args.csv_output,
            [
                {
                    "run_id": payload["run_id"],
                    "strategy": payload["strategy"],
                    "token_accuracy": payload["metrics"]["token_accuracy"],
                    "exact_match": payload["metrics"]["exact_match"],
                    "dependency_accuracy": payload["metrics"]["dependency_accuracy"],
                    "non_dependency_accuracy": payload["metrics"]["non_dependency_accuracy"],
                    "average_expensive_token_fraction": payload["metrics"]["average_expensive_token_fraction"],
                }
            ],
        )
    print(json.dumps(payload, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
