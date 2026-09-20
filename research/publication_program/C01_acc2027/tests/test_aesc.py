import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "code"))

from aesc import pointwise_gate_transition_ids, synthesize_supervisor
from benchmarks import atlas_case_studies


def test_aesc_removes_risky_precursor_and_invalidated_state():
    for plant, _ in atlas_case_studies():
        supervisor = synthesize_supervisor(plant)
        labels = {plant.labels[state] for state in supervisor.winning_states}
        assert "unsecured_commitment" not in labels
        assert "binding_invalidated" not in labels
        assert "protected_action_violation" not in labels
        assert plant.initial in supervisor.winning_states


def test_aesc_preserves_secure_completion_and_human_review():
    for plant, _ in atlas_case_studies():
        supervisor = synthesize_supervisor(plant)
        labels = {plant.labels[state] for state in supervisor.winning_states}
        assert "binding_secured" in labels
        assert "complete" in labels
        assert "human_review" in labels


def test_pointwise_gate_does_not_remove_risky_precursor():
    for plant, _ in atlas_case_studies():
        enabled = pointwise_gate_transition_ids(plant)
        events = {plant.transitions[idx].event for idx in enabled}
        assert any("unbound" in event or "unpinned" in event for event in events)


def test_against_bruteforce_oracle():
    from verify_synthesis import brute_force_winning_states, random_small_plant
    for idx in range(100):
        n = 3 + (idx % 6)
        plant = random_small_plant(n, 700001 + idx * 101)
        assert synthesize_supervisor(plant).winning_states == brute_force_winning_states(plant)
