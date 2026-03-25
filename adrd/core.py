from __future__ import annotations

import random
from dataclasses import dataclass

from adrd.config import BudgetConfig, ExperimentConfig, Mode
from adrd.synthetic import MASK_TOKEN, DependencyGroup, SyntheticExample


SEED_OFFSETS: dict[str, int] = {
    "factorized": 11,
    "coupled-local": 23,
    "micro-sequential": 37,
    "adrd": 53,
}


@dataclass(slots=True)
class ScoredGroup:
    group: DependencyGroup
    score: float
    confidence: float
    unresolved_positions: tuple[int, ...]


@dataclass(slots=True)
class RoutedGroup:
    group: DependencyGroup
    score: float
    confidence: float
    unresolved_positions: tuple[int, ...]
    mode: Mode


@dataclass(slots=True)
class ExampleTrace:
    prediction: list[int]
    token_confidences: list[float]
    token_modes: list[Mode]
    error_positions: list[int]
    dependency_positions: list[int]
    dependency_error_positions: list[int]
    mode_group_counts: dict[str, int]
    mode_token_counts: dict[str, int]


@dataclass(slots=True)
class DecodeMetrics:
    token_accuracy: float
    exact_match: float
    dependency_group_accuracy: float
    dependency_group_accuracy_by_kind: dict[str, float]
    mode_group_counts: dict[str, int]
    mode_token_counts: dict[str, int]
    average_expensive_token_fraction: float
    dependency_accuracy: float
    non_dependency_accuracy: float
    average_span_size_by_mode: dict[str, float]
    mean_token_confidence: float
    mean_error_confidence: float
    position_error_rates: dict[str, float]
    logged_examples: list[dict[str, object]]


class DependencyEstimator:
    """Simple heuristic estimator for the synthetic dependency task."""

    def score(self, example: SyntheticExample, state: list[int], step: int, total_steps: int) -> list[ScoredGroup]:
        scored: list[ScoredGroup] = []
        step_progress = step / max(total_steps - 1, 1)
        for group in example.dependency_groups:
            unresolved = tuple(idx for idx in group.positions if state[idx] == MASK_TOKEN)
            if not unresolved:
                continue
            unresolved_ratio = len(unresolved) / len(group.positions)
            span_len = len(group.positions)
            progression_bonus = 0.13 if group.kind == "progression" else 0.0
            copy_bonus = 0.08 if group.kind == "copy" else 0.0
            score = min(
                1.0,
                0.43
                + unresolved_ratio * 0.32
                + progression_bonus
                + copy_bonus
                + min(0.07, span_len * 0.015),
            )
            confidence = max(
                0.05,
                0.82
                - unresolved_ratio * 0.22
                - step_progress * 0.12
                - (0.1 if group.kind == "progression" else 0.02),
            )
            scored.append(
                ScoredGroup(
                    group=group,
                    score=score,
                    confidence=confidence,
                    unresolved_positions=unresolved,
                )
            )
        return scored


class BudgetController:
    def __init__(self, config: BudgetConfig) -> None:
        self.config = config

    def allow(
        self,
        mode: Mode,
        mode_group_counts: dict[str, int],
        mode_token_counts: dict[str, int],
        unresolved_tokens: int,
        seq_len: int,
    ) -> bool:
        if mode == "factorized":
            return True

        max_non_factorized_tokens = max(1, int(seq_len * self.config.max_non_factorized_fraction))
        current_non_factorized = mode_token_counts["coupled-local"] + mode_token_counts["micro-sequential"]
        if current_non_factorized + unresolved_tokens > max_non_factorized_tokens:
            return False

        if mode == "coupled-local":
            if mode_group_counts["coupled-local"] >= self.config.max_coupled_groups_per_step:
                return False
            if self.config.max_coupled_tokens_per_step is None:
                return True
            return mode_token_counts["coupled-local"] + unresolved_tokens <= self.config.max_coupled_tokens_per_step

        if mode_group_counts["micro-sequential"] >= self.config.max_micro_seq_groups_per_step:
            return False
        if self.config.max_micro_seq_tokens_per_step is None:
            return True
        return mode_token_counts["micro-sequential"] + unresolved_tokens <= self.config.max_micro_seq_tokens_per_step


class ModeRouter:
    def __init__(self, config: ExperimentConfig, budget: BudgetController) -> None:
        self.config = config
        self.budget = budget

    def _mode_allowed_for_candidate(self, mode: Mode, candidate: ScoredGroup) -> bool:
        if mode not in self.config.allowed_modes:
            return False
        if mode != "coupled-local":
            return True
        if self.config.max_coupled_span_len is None:
            return True
        return len(candidate.group.positions) <= self.config.max_coupled_span_len

    @staticmethod
    def _dedupe_modes(modes: list[Mode]) -> list[Mode]:
        seen: set[Mode] = set()
        ordered: list[Mode] = []
        for mode in modes:
            if mode in seen:
                continue
            seen.add(mode)
            ordered.append(mode)
        return ordered

    def _preferred_modes(self, candidate: ScoredGroup) -> list[Mode]:
        allowed = set(self.config.allowed_modes)
        span_len = len(candidate.unresolved_positions)
        can_use_coupled = self._mode_allowed_for_candidate("coupled-local", candidate)
        can_use_micro = "micro-sequential" in allowed

        preferred: list[Mode] = []
        if can_use_micro and candidate.group.kind == "progression":
            if candidate.confidence <= 0.6 or span_len <= 3:
                preferred.append("micro-sequential")
            if candidate.score >= 0.75:
                preferred.append("micro-sequential")
            if can_use_coupled and candidate.score >= 0.66 and span_len >= 3:
                preferred.append("coupled-local")
        if can_use_coupled and candidate.group.kind == "copy":
            preferred.append("coupled-local")
            if span_len >= 3 and candidate.score >= 0.62:
                preferred.append("coupled-local")
            if can_use_micro and span_len <= 2 and candidate.score >= 0.78:
                preferred.append("micro-sequential")
        if can_use_coupled and candidate.group.kind == "progression" and span_len >= 5 and candidate.confidence >= 0.48:
            preferred.append("coupled-local")
        if can_use_micro and candidate.score >= 0.82 and candidate.confidence < 0.55:
            preferred.append("micro-sequential")
        if can_use_coupled and candidate.score >= 0.7 and candidate.confidence >= 0.58:
            preferred.append("coupled-local")
        preferred.append("factorized")
        return self._dedupe_modes(preferred)

    def _assign_modes(
        self,
        candidates: list[ScoredGroup],
        seq_len: int,
        mode_preferences: callable,
    ) -> list[RoutedGroup]:
        mode_group_counts = {"factorized": 0, "coupled-local": 0, "micro-sequential": 0}
        mode_token_counts = {"factorized": 0, "coupled-local": 0, "micro-sequential": 0}
        routed: list[RoutedGroup] = []

        for candidate in sorted(candidates, key=lambda item: item.score, reverse=True):
            chosen: Mode = "factorized"
            unresolved_tokens = len(candidate.unresolved_positions)
            for mode in mode_preferences(candidate):
                if mode != "factorized" and not self._mode_allowed_for_candidate(mode, candidate):
                    continue
                if self.budget.allow(mode, mode_group_counts, mode_token_counts, unresolved_tokens, seq_len):
                    chosen = mode
                    break
            mode_group_counts[chosen] += 1
            mode_token_counts[chosen] += unresolved_tokens
            routed.append(
                RoutedGroup(
                    group=candidate.group,
                    score=candidate.score,
                    confidence=candidate.confidence,
                    unresolved_positions=candidate.unresolved_positions,
                    mode=chosen,
                )
            )
        return routed

    def route(self, candidates: list[ScoredGroup], seq_len: int) -> list[RoutedGroup]:
        return self._assign_modes(candidates, seq_len, self._preferred_modes)

    def route_with_fixed_priority(
        self,
        candidates: list[ScoredGroup],
        seq_len: int,
        preferred_modes: tuple[Mode, ...],
    ) -> list[RoutedGroup]:
        return self._assign_modes(
            candidates,
            seq_len,
            lambda candidate: self._dedupe_modes(
                [mode for mode in preferred_modes if self._mode_allowed_for_candidate(mode, candidate)] + ["factorized"]
            ),
        )

    def route_random(self, candidates: list[ScoredGroup], seq_len: int, rng: random.Random) -> list[RoutedGroup]:
        def random_preferences(candidate: ScoredGroup) -> list[Mode]:
            modes = [mode for mode in self.config.allowed_modes if mode != "factorized" and self._mode_allowed_for_candidate(mode, candidate)]
            rng.shuffle(modes)
            return self._dedupe_modes(modes + ["factorized"])

        return self._assign_modes(candidates, seq_len, random_preferences)


class Decoder:
    def __init__(self, config: ExperimentConfig, rng: random.Random) -> None:
        self.config = config
        self.rng = rng

    def _sample_prediction(self, p_correct: float, target: int) -> tuple[int, float]:
        confidence = round(max(0.05, min(0.99, p_correct)), 4)
        if self.rng.random() < p_correct:
            return target, confidence
        wrong = self.rng.randint(0, self.config.vocab_size - 1)
        prediction = wrong if wrong != target else (wrong + 1) % self.config.vocab_size
        return prediction, confidence

    @staticmethod
    def _record_prediction(
        state: list[int],
        token_confidences: list[float],
        token_modes: list[Mode],
        idx: int,
        prediction: int,
        confidence: float,
        mode: Mode,
    ) -> None:
        if state[idx] != MASK_TOKEN:
            return
        state[idx] = prediction
        token_confidences[idx] = confidence
        token_modes[idx] = mode

    def _apply_exact_group(
        self,
        example: SyntheticExample,
        unresolved_positions: tuple[int, ...],
        state: list[int],
        token_confidences: list[float],
        token_modes: list[Mode],
        mode: Mode,
        confidence: float,
    ) -> None:
        for idx in unresolved_positions:
            self._record_prediction(state, token_confidences, token_modes, idx, example.tokens[idx], confidence, mode)

    @staticmethod
    def _mode_skill_profile(group: DependencyGroup, unresolved_positions: tuple[int, ...], mode: Mode) -> tuple[float, float]:
        span_len = len(unresolved_positions)
        if mode == "coupled-local":
            if group.kind == "copy":
                exact_prob = 0.92 if span_len <= 4 else 0.8
                fallback_prob = 0.66
            else:
                exact_prob = 0.5 if span_len <= 3 else 0.42
                fallback_prob = 0.46
            return exact_prob, fallback_prob

        if group.kind == "progression":
            anchor_prob = 0.94 if span_len <= 3 else 0.88
            tail_prob = 0.88 if span_len <= 3 else 0.8
            return anchor_prob, tail_prob

        anchor_prob = 0.72 if span_len <= 2 else 0.64
        tail_prob = 0.58 if span_len <= 2 else 0.46
        return anchor_prob, tail_prob

    def apply(
        self,
        example: SyntheticExample,
        state: list[int],
        routed: list[RoutedGroup],
        token_confidences: list[float],
        token_modes: list[Mode],
    ) -> tuple[dict[str, int], dict[str, int]]:
        mode_group_counts = {"factorized": 0, "coupled-local": 0, "micro-sequential": 0}
        mode_token_counts = {"factorized": 0, "coupled-local": 0, "micro-sequential": 0}
        covered = {idx for item in routed for idx in item.unresolved_positions}

        for item in routed:
            unresolved_positions = tuple(idx for idx in item.unresolved_positions if state[idx] == MASK_TOKEN)
            if not unresolved_positions:
                continue
            mode_group_counts[item.mode] += 1
            mode_token_counts[item.mode] += len(unresolved_positions)

            if item.mode == "factorized":
                for idx in unresolved_positions:
                    prediction, confidence = self._sample_prediction(0.38, example.tokens[idx])
                    self._record_prediction(state, token_confidences, token_modes, idx, prediction, confidence, item.mode)
                continue

            if item.mode == "coupled-local":
                exact_prob, fallback_prob = self._mode_skill_profile(item.group, unresolved_positions, item.mode)
                if self.rng.random() < exact_prob:
                    self._apply_exact_group(
                        example,
                        unresolved_positions,
                        state,
                        token_confidences,
                        token_modes,
                        item.mode,
                        confidence=round(exact_prob, 4),
                    )
                else:
                    for idx in unresolved_positions:
                        prediction, confidence = self._sample_prediction(fallback_prob, example.tokens[idx])
                        self._record_prediction(state, token_confidences, token_modes, idx, prediction, confidence, item.mode)
                continue

            anchor_prob, tail_prob = self._mode_skill_profile(item.group, unresolved_positions, item.mode)
            anchor_idx = unresolved_positions[0]
            anchor_prediction, anchor_confidence = self._sample_prediction(anchor_prob, example.tokens[anchor_idx])
            self._record_prediction(
                state,
                token_confidences,
                token_modes,
                anchor_idx,
                anchor_prediction,
                anchor_confidence,
                item.mode,
            )
            if state[anchor_idx] == example.tokens[anchor_idx]:
                if item.group.kind == "progression":
                    self._apply_exact_group(
                        example,
                        unresolved_positions[1:],
                        state,
                        token_confidences,
                        token_modes,
                        item.mode,
                        confidence=round(tail_prob, 4),
                    )
                else:
                    for idx in unresolved_positions[1:]:
                        prediction, confidence = self._sample_prediction(tail_prob, example.tokens[idx])
                        self._record_prediction(state, token_confidences, token_modes, idx, prediction, confidence, item.mode)
            else:
                for idx in unresolved_positions[1:]:
                    prediction, confidence = self._sample_prediction(max(0.4, tail_prob - 0.18), example.tokens[idx])
                    self._record_prediction(state, token_confidences, token_modes, idx, prediction, confidence, item.mode)

        for idx, target in enumerate(example.tokens):
            if idx in covered or state[idx] != MASK_TOKEN:
                continue
            prediction, confidence = self._sample_prediction(0.7, target)
            self._record_prediction(state, token_confidences, token_modes, idx, prediction, confidence, "factorized")
            mode_token_counts["factorized"] += 1

        return mode_group_counts, mode_token_counts


class AdaptiveDependencyRoutingDecoder:
    def __init__(self, config: ExperimentConfig) -> None:
        self.config = config
        self.estimator = DependencyEstimator()

    def decode(self, example: SyntheticExample, strategy: Mode | str, rng: random.Random) -> ExampleTrace:
        state = [MASK_TOKEN] * len(example.tokens)
        token_confidences = [0.0] * len(example.tokens)
        token_modes: list[Mode] = ["factorized"] * len(example.tokens)
        decoder = Decoder(self.config, rng)
        total_group_counts = {"factorized": 0, "coupled-local": 0, "micro-sequential": 0}
        total_token_counts = {"factorized": 0, "coupled-local": 0, "micro-sequential": 0}

        for step in range(self.config.diffusion_steps):
            candidates = self.estimator.score(example, state, step, self.config.diffusion_steps)
            router = ModeRouter(self.config, BudgetController(self.config.budget))
            if strategy == "factorized":
                routed = [
                    RoutedGroup(
                        group=item.group,
                        score=item.score,
                        confidence=item.confidence,
                        unresolved_positions=item.unresolved_positions,
                        mode="factorized",
                    )
                    for item in candidates
                ]
            elif strategy == "coupled-local":
                routed = [
                    RoutedGroup(
                        group=item.group,
                        score=item.score,
                        confidence=item.confidence,
                        unresolved_positions=item.unresolved_positions,
                        mode="coupled-local",
                    )
                    for item in candidates
                ]
            elif strategy == "micro-sequential":
                routed = [
                    RoutedGroup(
                        group=item.group,
                        score=item.score,
                        confidence=item.confidence,
                        unresolved_positions=item.unresolved_positions,
                        mode="micro-sequential",
                    )
                    for item in candidates
                ]
            elif strategy == "budgeted-coupled-local":
                routed = router.route_with_fixed_priority(candidates, len(example.tokens), ("coupled-local",))
            elif strategy == "budgeted-micro-sequential":
                routed = router.route_with_fixed_priority(candidates, len(example.tokens), ("micro-sequential",))
            elif strategy == "random-budgeted":
                routed = router.route_random(candidates, len(example.tokens), rng)
            else:
                routed = router.route(candidates, len(example.tokens))

            step_group_counts, step_token_counts = decoder.apply(example, state, routed, token_confidences, token_modes)
            for key, value in step_group_counts.items():
                total_group_counts[key] += value
            for key, value in step_token_counts.items():
                total_token_counts[key] += value

        dependency_positions = sorted({idx for group in example.dependency_groups for idx in group.positions})
        dependency_position_set = set(dependency_positions)
        error_positions = [idx for idx, (prediction, target) in enumerate(zip(state, example.tokens)) if prediction != target]
        dependency_error_positions = [idx for idx in error_positions if idx in dependency_position_set]
        return ExampleTrace(
            prediction=state,
            token_confidences=token_confidences,
            token_modes=token_modes,
            error_positions=error_positions,
            dependency_positions=dependency_positions,
            dependency_error_positions=dependency_error_positions,
            mode_group_counts=total_group_counts,
            mode_token_counts=total_token_counts,
        )


def evaluate(
    config: ExperimentConfig,
    dataset: list[SyntheticExample],
    strategy: Mode | str,
    label: str | None = None,
) -> DecodeMetrics:
    decoder = AdaptiveDependencyRoutingDecoder(config)
    seed_label = label or str(strategy)
    rng = random.Random(config.seed + SEED_OFFSETS.get(seed_label, 97))

    total_correct = 0
    total_tokens = 0
    exact_match = 0
    dependency_correct = 0
    dependency_total = 0
    dependency_group_correct = 0
    dependency_group_total = 0
    dependency_group_correct_by_kind: dict[str, int] = {}
    dependency_group_total_by_kind: dict[str, int] = {}
    non_dependency_correct = 0
    non_dependency_total = 0
    total_confidence = 0.0
    error_confidence = 0.0
    error_count = 0

    mode_group_counts = {"factorized": 0, "coupled-local": 0, "micro-sequential": 0}
    mode_token_counts = {"factorized": 0, "coupled-local": 0, "micro-sequential": 0}
    position_totals = [0] * config.seq_len
    position_errors = [0] * config.seq_len
    logged_examples: list[dict[str, object]] = []

    for example_index, example in enumerate(dataset):
        trace = decoder.decode(example, strategy, rng)
        dependency_positions = set(trace.dependency_positions)
        exact_match += int(trace.prediction == example.tokens)

        for idx, (prediction, target, confidence) in enumerate(zip(trace.prediction, example.tokens, trace.token_confidences)):
            total_correct += int(prediction == target)
            total_tokens += 1
            total_confidence += confidence
            position_totals[idx] += 1
            if prediction != target:
                position_errors[idx] += 1
                error_confidence += confidence
                error_count += 1
            if idx in dependency_positions:
                dependency_correct += int(prediction == target)
                dependency_total += 1
            else:
                non_dependency_correct += int(prediction == target)
                non_dependency_total += 1

        for group in example.dependency_groups:
            dependency_group_total += 1
            dependency_group_total_by_kind[group.kind] = dependency_group_total_by_kind.get(group.kind, 0) + 1
            group_correct = all(trace.prediction[idx] == example.tokens[idx] for idx in group.positions)
            if group_correct:
                dependency_group_correct += 1
                dependency_group_correct_by_kind[group.kind] = dependency_group_correct_by_kind.get(group.kind, 0) + 1

        for key, value in trace.mode_group_counts.items():
            mode_group_counts[key] += value
        for key, value in trace.mode_token_counts.items():
            mode_token_counts[key] += value

        if len(logged_examples) < config.log_examples:
            logged_examples.append(
                {
                    "example_index": example_index,
                    "targets": example.tokens,
                    "prediction": trace.prediction,
                    "token_confidences": trace.token_confidences,
                    "token_modes": trace.token_modes,
                    "error_positions": trace.error_positions,
                    "dependency_positions": trace.dependency_positions,
                    "dependency_error_positions": trace.dependency_error_positions,
                }
            )

    expensive_tokens = mode_token_counts["coupled-local"] + mode_token_counts["micro-sequential"]
    average_span_size_by_mode = {
        key: round(mode_token_counts[key] / max(mode_group_counts[key], 1), 4)
        for key in mode_group_counts
    }
    position_error_rates = {
        str(idx): round(position_errors[idx] / max(position_totals[idx], 1), 4)
        for idx in range(config.seq_len)
    }
    return DecodeMetrics(
        token_accuracy=total_correct / max(total_tokens, 1),
        exact_match=exact_match / max(len(dataset), 1),
        dependency_group_accuracy=dependency_group_correct / max(dependency_group_total, 1),
        dependency_group_accuracy_by_kind={
            kind: round(dependency_group_correct_by_kind.get(kind, 0) / total, 4)
            for kind, total in dependency_group_total_by_kind.items()
        },
        mode_group_counts=mode_group_counts,
        mode_token_counts=mode_token_counts,
        average_expensive_token_fraction=expensive_tokens / max(total_tokens, 1),
        dependency_accuracy=dependency_correct / max(dependency_total, 1),
        non_dependency_accuracy=non_dependency_correct / max(non_dependency_total, 1),
        average_span_size_by_mode=average_span_size_by_mode,
        mean_token_confidence=total_confidence / max(total_tokens, 1),
        mean_error_confidence=error_confidence / max(error_count, 1),
        position_error_rates=position_error_rates,
        logged_examples=logged_examples,
    )
