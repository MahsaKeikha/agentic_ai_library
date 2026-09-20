import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "code"))

from risk_calibrated_oversight import AgentAction, Episode, calibrate_selective_oversight


def safe_episodes(n=200):
    return [
        Episode((AgentAction(0.1, False), AgentAction(0.3, False)))
        for _ in range(n)
    ]


def test_safe_data_permits_autonomy_when_certificate_allows_it():
    policy = calibrate_selective_oversight(
        safe_episodes(1000),
        alpha=0.10,
        delta=0.05,
        thresholds=(-1.0, 0.2, 0.5, 1.0),
    )
    assert policy.threshold == 1.0
    assert policy.certificate.autonomy_coverage == 1.0
    assert policy.certificate.episode_failures == 0


def test_high_risk_low_score_forces_conservative_policy():
    episodes = [
        Episode((AgentAction(0.1, i % 5 == 0), AgentAction(0.8, False)))
        for i in range(1000)
    ]
    policy = calibrate_selective_oversight(
        episodes,
        alpha=0.05,
        delta=0.05,
        thresholds=(-1.0, 0.05, 0.2, 1.0),
    )
    assert policy.threshold == 0.05
    assert policy.certificate.autonomy_coverage == 0.0


def test_hard_block_is_never_acted_autonomously():
    episodes = [
        Episode((AgentAction(0.0, True, hard_block=True),))
        for _ in range(500)
    ]
    policy = calibrate_selective_oversight(
        episodes,
        alpha=0.05,
        thresholds=(-1.0, 1.0),
    )
    action = episodes[0].actions[0]
    assert policy.decision(action, human_available=True) == "ASK"
    assert policy.decision(action, human_available=False) == "ABSTAIN"
    assert policy.certificate.autonomy_coverage == 0.0


def test_review_when_above_threshold():
    policy = calibrate_selective_oversight(
        safe_episodes(1000),
        alpha=0.10,
        thresholds=(-1.0, 0.2),
    )
    action = AgentAction(0.9, False)
    assert policy.decision(action, human_available=True) == "ASK"
    assert policy.decision(action, human_available=False) == "ABSTAIN"
