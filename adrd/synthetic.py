from __future__ import annotations

import random
from dataclasses import dataclass
from typing import Iterable

from adrd.config import ExperimentConfig


MASK_TOKEN = -1


@dataclass(slots=True)
class DependencyGroup:
    positions: tuple[int, ...]
    kind: str


@dataclass(slots=True)
class SyntheticExample:
    tokens: list[int]
    dependency_groups: list[DependencyGroup]


def _sample_positions(length: int, rng: random.Random, config: ExperimentConfig) -> tuple[int, ...]:
    max_span = min(config.max_dependency_span, length)
    min_span = min(config.min_dependency_span, max_span)
    span = rng.randint(min_span, max_span)
    start = rng.randint(0, length - span)
    return tuple(range(start, start + span))


def _make_copy_group(tokens: list[int], rng: random.Random, config: ExperimentConfig) -> DependencyGroup:
    positions = _sample_positions(len(tokens), rng, config)
    shared = rng.randint(0, 9)
    for idx in positions:
        tokens[idx] = shared
    return DependencyGroup(positions=positions, kind="copy")


def _make_progression_group(tokens: list[int], rng: random.Random, config: ExperimentConfig) -> DependencyGroup:
    positions = _sample_positions(len(tokens), rng, config)
    base = rng.randint(0, config.vocab_size - 1)
    step = rng.randint(1, 3)
    for offset, idx in enumerate(positions):
        tokens[idx] = (base + offset * step) % config.vocab_size
    return DependencyGroup(positions=positions, kind="progression")


def make_example(rng: random.Random, config: ExperimentConfig) -> SyntheticExample:
    tokens = [rng.randint(0, config.vocab_size - 1) for _ in range(config.seq_len)]
    dependency_groups: list[DependencyGroup] = []
    if rng.random() < config.dependency_probability:
        dependency_groups.append(_make_copy_group(tokens, rng, config))
    if rng.random() < config.dependency_probability:
        dependency_groups.append(_make_progression_group(tokens, rng, config))
    return SyntheticExample(tokens=tokens, dependency_groups=dependency_groups)


def make_dataset(config: ExperimentConfig) -> list[SyntheticExample]:
    rng = random.Random(config.seed)
    return [make_example(rng, config) for _ in range(config.dataset_size)]


def unresolved_positions(example: SyntheticExample, state: list[int]) -> Iterable[int]:
    for idx, value in enumerate(state):
        if value == MASK_TOKEN:
            yield idx
