import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "code"))

from caesc import compositional_synthesize, monolithic_synthesize, winning_tuples
from journal_benchmarks import (
    authority_component,
    at_most_one_authority_claimed,
    precursor_component,
)


def test_local_viability_pruning_is_exact_for_precursor_networks():
    for n in range(2, 5):
        components = [precursor_component(i) for i in range(n)]
        mono, mono_sup = monolithic_synthesize(components)
        _, comp, comp_sup = compositional_synthesize(components)
        assert winning_tuples(mono, mono_sup) == winning_tuples(comp, comp_sup)
        assert comp.plant.n_states < mono.plant.n_states


def test_coupling_requires_global_coordination():
    components = [authority_component(0), authority_component(1)]
    mono, mono_sup = monolithic_synthesize(components, at_most_one_authority_claimed)
    tuples = winning_tuples(mono, mono_sup)
    assert (2, 2) not in tuples
    assert (2, 1) in tuples or (1, 2) in tuples


def test_compositional_and_monolithic_match_with_coupling():
    for n in range(2, 5):
        components = [authority_component(i) for i in range(n)]
        mono, mono_sup = monolithic_synthesize(components, at_most_one_authority_claimed)
        _, comp, comp_sup = compositional_synthesize(
            components, at_most_one_authority_claimed
        )
        assert winning_tuples(mono, mono_sup) == winning_tuples(comp, comp_sup)


def test_revoked_authority_never_reaches_violation_under_supervisor():
    components = [authority_component(0), authority_component(1)]
    _, model, supervisor = compositional_synthesize(
        components, at_most_one_authority_claimed
    )
    for idx in supervisor.winning_states:
        state = model.tuples[idx]
        assert all(x != 6 for x in state)
