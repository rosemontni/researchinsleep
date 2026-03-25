from __future__ import annotations

from dataclasses import dataclass, field
from typing import Literal


Mode = Literal["factorized", "coupled-local", "micro-sequential"]


@dataclass(slots=True)
class BudgetConfig:
    max_coupled_groups_per_step: int = 2
    max_micro_seq_groups_per_step: int = 1
    max_non_factorized_fraction: float = 0.5
    max_coupled_tokens_per_step: int | None = None
    max_micro_seq_tokens_per_step: int | None = None


@dataclass(slots=True)
class ExperimentConfig:
    dataset_size: int = 128
    seq_len: int = 24
    vocab_size: int = 10
    diffusion_steps: int = 4
    seed: int = 7
    dependency_probability: float = 0.75
    min_dependency_span: int = 2
    max_dependency_span: int = 5
    allowed_modes: tuple[Mode, ...] = ("factorized", "coupled-local", "micro-sequential")
    max_coupled_span_len: int | None = None
    log_examples: int = 5
    budget: BudgetConfig = field(default_factory=BudgetConfig)
