from __future__ import annotations

from dataclasses import dataclass
from math import log, sqrt
from typing import Iterable, Sequence


@dataclass(frozen=True)
class AgentAction:
    risk_score: float
    unsafe_if_autonomous: bool
    hard_block: bool = False

    def __post_init__(self):
        if not 0.0 <= self.risk_score <= 1.0:
            raise ValueError("risk_score must lie in [0,1]")


@dataclass(frozen=True)
class Episode:
    actions: tuple[AgentAction, ...]


@dataclass(frozen=True)
class CalibrationPoint:
    threshold: float
    empirical_episode_risk: float
    risk_upper_bound: float
    autonomy_coverage: float
    review_fraction: float
    episode_failures: int
    episodes: int


@dataclass(frozen=True)
class CalibratedPolicy:
    threshold: float
    alpha: float
    delta: float
    certificate: CalibrationPoint
    candidate_count: int

    def decision(self, action: AgentAction, human_available: bool = True) -> str:
        if action.hard_block:
            return "ASK" if human_available else "ABSTAIN"
        if action.risk_score <= self.threshold:
            return "ACT"
        return "ASK" if human_available else "ABSTAIN"


def fixed_threshold_grid(step: float = 0.01) -> tuple[float, ...]:
    if not 0.0 < step <= 1.0:
        raise ValueError("step must lie in (0,1]")
    n = int(round(1.0 / step))
    vals = [-1.0]
    for i in range(n + 1):
        vals.append(min(1.0, i * step))
    return tuple(dict.fromkeys(vals))


def _evaluate_threshold(
    episodes: Sequence[Episode],
    threshold: float,
    m: int,
    delta: float,
) -> CalibrationPoint:
    n = len(episodes)
    if n == 0:
        raise ValueError("at least one calibration episode is required")

    failures = 0
    total_actions = 0
    autonomous_actions = 0
    review_actions = 0

    for episode in episodes:
        episode_failure = False
        for action in episode.actions:
            total_actions += 1
            autonomous = (not action.hard_block) and action.risk_score <= threshold
            if autonomous:
                autonomous_actions += 1
                if action.unsafe_if_autonomous:
                    episode_failure = True
            else:
                review_actions += 1
        failures += int(episode_failure)

    phat = failures / n
    if threshold < 0.0:
        upper = 0.0
    else:
        radius = sqrt(log(m / delta) / (2.0 * n))
        upper = min(1.0, phat + radius)

    coverage = autonomous_actions / total_actions if total_actions else 0.0
    review = review_actions / total_actions if total_actions else 0.0

    return CalibrationPoint(
        threshold=threshold,
        empirical_episode_risk=phat,
        risk_upper_bound=upper,
        autonomy_coverage=coverage,
        review_fraction=review,
        episode_failures=failures,
        episodes=n,
    )


def calibrate_selective_oversight(
    episodes: Sequence[Episode],
    alpha: float,
    delta: float = 0.05,
    thresholds: Iterable[float] | None = None,
) -> CalibratedPolicy:
    """Choose the highest-coverage threshold with an episode-risk certificate.

    The certificate uses a fixed, prespecified threshold grid and a simultaneous
    Hoeffding bound across that grid. The independent sampling unit is an
    episode. Hard-block actions are never autonomously executed.
    """
    if not 0.0 <= alpha <= 1.0:
        raise ValueError("alpha must lie in [0,1]")
    if not 0.0 < delta < 1.0:
        raise ValueError("delta must lie in (0,1)")

    grid = tuple(fixed_threshold_grid() if thresholds is None else thresholds)
    if not grid:
        raise ValueError("threshold grid cannot be empty")
    if -1.0 not in grid:
        grid = (-1.0,) + grid
    if any(t < -1.0 or t > 1.0 for t in grid):
        raise ValueError("thresholds must lie in [-1,1]")

    points = [_evaluate_threshold(episodes, t, len(grid), delta) for t in grid]
    feasible = [p for p in points if p.risk_upper_bound <= alpha]
    best = max(feasible, key=lambda p: (p.autonomy_coverage, p.threshold))

    return CalibratedPolicy(
        threshold=best.threshold,
        alpha=alpha,
        delta=delta,
        certificate=best,
        candidate_count=len(grid),
    )
