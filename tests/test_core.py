import sys
import unittest
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from adrd.config import BudgetConfig, ExperimentConfig
from adrd.core import BudgetController, ModeRouter, ScoredGroup, evaluate
from adrd.synthetic import DependencyGroup, make_dataset


class CoreTests(unittest.TestCase):
    def test_router_respects_token_budget(self) -> None:
        config = ExperimentConfig(
            seq_len=24,
            allowed_modes=("factorized", "micro-sequential"),
            budget=BudgetConfig(
                max_coupled_groups_per_step=0,
                max_micro_seq_groups_per_step=2,
                max_non_factorized_fraction=0.10,
                max_micro_seq_tokens_per_step=2,
            ),
        )
        router = ModeRouter(config, BudgetController(config.budget))
        candidates = [
            ScoredGroup(DependencyGroup((0, 1, 2), "progression"), 0.9, 0.2, (0, 1, 2)),
            ScoredGroup(DependencyGroup((3, 4), "copy"), 0.85, 0.3, (3, 4)),
        ]
        routed = router.route(candidates, seq_len=config.seq_len)
        expensive_tokens = sum(len(item.unresolved_positions) for item in routed if item.mode != "factorized")
        self.assertLessEqual(expensive_tokens, 2)

    def test_coupled_local_respects_span_cap(self) -> None:
        config = ExperimentConfig(max_coupled_span_len=3)
        router = ModeRouter(config, BudgetController(config.budget))
        candidates = [
            ScoredGroup(DependencyGroup((0, 1, 2, 3), "progression"), 0.8, 0.55, (0, 1, 2, 3)),
        ]
        routed = router.route(candidates, seq_len=config.seq_len)
        self.assertNotEqual(routed[0].mode, "coupled-local")

    def test_adrd_uses_non_factorized_modes(self) -> None:
        config = ExperimentConfig(dataset_size=32, seed=13)
        metrics = evaluate(config, make_dataset(config), "adrd", label="adrd")
        self.assertTrue(metrics.mode_token_counts["coupled-local"] > 0 or metrics.mode_token_counts["micro-sequential"] > 0)

    def test_progression_groups_can_route_to_micro_sequential(self) -> None:
        config = ExperimentConfig(
            allowed_modes=("factorized", "coupled-local", "micro-sequential"),
            budget=BudgetConfig(
                max_coupled_groups_per_step=2,
                max_micro_seq_groups_per_step=2,
                max_non_factorized_fraction=0.25,
                max_micro_seq_tokens_per_step=3,
            ),
        )
        router = ModeRouter(config, BudgetController(config.budget))
        candidates = [
            ScoredGroup(DependencyGroup((0, 1, 2), "progression"), 0.82, 0.45, (0, 1, 2)),
        ]
        routed = router.route(candidates, seq_len=config.seq_len)
        self.assertEqual(routed[0].mode, "micro-sequential")

    def test_random_budgeted_routing_respects_budget(self) -> None:
        config = ExperimentConfig(
            allowed_modes=("factorized", "coupled-local", "micro-sequential"),
            budget=BudgetConfig(
                max_coupled_groups_per_step=1,
                max_micro_seq_groups_per_step=1,
                max_non_factorized_fraction=0.10,
                max_coupled_tokens_per_step=2,
                max_micro_seq_tokens_per_step=2,
            ),
        )
        dataset = make_dataset(config)
        metrics = evaluate(config, dataset, "random-budgeted", label="random-budgeted")
        expensive_tokens = metrics.mode_token_counts["coupled-local"] + metrics.mode_token_counts["micro-sequential"]
        self.assertLessEqual(expensive_tokens, config.dataset_size * int(config.seq_len * config.budget.max_non_factorized_fraction))

    def test_adrd_improves_exact_match_over_factorized_on_synthetic_task(self) -> None:
        config = ExperimentConfig(dataset_size=48, seed=9)
        dataset = make_dataset(config)
        factorized = evaluate(config, dataset, "factorized", label="factorized")
        adrd = evaluate(config, dataset, "adrd", label="adrd")
        self.assertGreaterEqual(adrd.exact_match, factorized.exact_match)

    def test_dependency_group_accuracy_tracks_group_recovery(self) -> None:
        config = ExperimentConfig(dataset_size=48, seed=9)
        dataset = make_dataset(config)
        factorized = evaluate(config, dataset, "factorized", label="factorized")
        adrd = evaluate(config, dataset, "adrd", label="adrd")
        self.assertGreaterEqual(adrd.dependency_group_accuracy, factorized.dependency_group_accuracy)

    def test_adrd_beats_fixed_budget10_baselines_on_token_accuracy(self) -> None:
        config = ExperimentConfig(
            dataset_size=192,
            seq_len=24,
            seed=7,
            dependency_probability=0.8,
            min_dependency_span=2,
            max_dependency_span=5,
            allowed_modes=("factorized", "coupled-local", "micro-sequential"),
            max_coupled_span_len=4,
            budget=BudgetConfig(
                max_coupled_groups_per_step=1,
                max_micro_seq_groups_per_step=1,
                max_non_factorized_fraction=0.10,
                max_coupled_tokens_per_step=2,
                max_micro_seq_tokens_per_step=2,
            ),
        )
        dataset = make_dataset(config)
        adrd = evaluate(config, dataset, "adrd", label="three_mode_budget10")
        coupled = evaluate(config, dataset, "budgeted-coupled-local", label="budgeted_coupled_budget10")
        micro = evaluate(config, dataset, "budgeted-micro-sequential", label="budgeted_micro_budget10")
        self.assertGreater(adrd.token_accuracy, coupled.token_accuracy)
        self.assertGreater(adrd.token_accuracy, micro.token_accuracy)

    def test_adrd_beats_span4_baselines_after_router_redesign(self) -> None:
        config = ExperimentConfig(
            dataset_size=192,
            seq_len=24,
            seed=7,
            dependency_probability=0.8,
            min_dependency_span=2,
            max_dependency_span=5,
            allowed_modes=("factorized", "coupled-local", "micro-sequential"),
            max_coupled_span_len=4,
            budget=BudgetConfig(
                max_coupled_groups_per_step=2,
                max_micro_seq_groups_per_step=1,
                max_non_factorized_fraction=0.20,
                max_coupled_tokens_per_step=4,
                max_micro_seq_tokens_per_step=2,
            ),
        )
        dataset = make_dataset(config)
        adrd = evaluate(config, dataset, "adrd", label="three_mode_span4")
        coupled = evaluate(config, dataset, "budgeted-coupled-local", label="budgeted_coupled_span4")
        random_budgeted = evaluate(config, dataset, "random-budgeted", label="random_span4")
        self.assertGreater(adrd.token_accuracy, coupled.token_accuracy)
        self.assertGreater(adrd.token_accuracy, random_budgeted.token_accuracy)


if __name__ == "__main__":
    unittest.main()
