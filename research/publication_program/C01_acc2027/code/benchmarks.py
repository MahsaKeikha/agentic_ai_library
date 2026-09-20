"""Synthetic Atlas-derived benchmark models for AESC Paper 1."""
from __future__ import annotations

import random
from typing import List, Tuple

from aesc import Plant, Transition


def _domain_plant(name, invalidation_event, binding_event, risky_precursor, protected_event) -> Plant:
    labels = {
        0: "start", 1: "assessed", 2: "binding_secured",
        3: "unsecured_commitment", 4: "binding_invalidated",
        5: "complete", 6: "human_review", 7: "protected_action_violation",
    }
    transitions = (
        Transition(0, "assess", 1, True),
        Transition(1, binding_event, 2, True),
        Transition(1, risky_precursor, 3, True),
        Transition(1, "request_human_review", 6, True),
        Transition(2, protected_event, 5, True, protected=True),
        Transition(3, protected_event, 5, True, protected=True),
        Transition(3, invalidation_event, 4, False),
        Transition(4, protected_event, 7, True, protected=True),
        Transition(1, "refresh_context", 1, True),
        Transition(2, "verify_binding", 2, True),
    )
    return Plant(
        name=name, n_states=8, initial=0,
        marked=frozenset({5, 6}), forbidden=frozenset({7}),
        transitions=transitions, labels=labels,
    )


def atlas_case_studies() -> List[Tuple[Plant, float]]:
    return [
        (_domain_plant("software_release","approval_revoked","bind_release_token","prepare_unbound_release","deploy_production"),0.22),
        (_domain_plant("industrial_digital_twin","twin_snapshot_stale","pin_twin_snapshot","reserve_unpinned_actuation","write_actuator"),0.30),
        (_domain_plant("agewell_support","consent_scope_changed","bind_consent_epoch","prepare_unbound_support","dispatch_support_action"),0.18),
        (_domain_plant("smart_city","evidence_feed_stale","pin_incident_evidence","prepare_unbound_intervention","execute_city_intervention"),0.27),
    ]


def random_feasible_plant(
    n_states: int, seed: int, out_degree: int = 5,
    forbidden_fraction: float = 0.05, marked_fraction: float = 0.04,
    uncontrollable_fraction: float = 0.12,
) -> Plant:
    """Generate a seeded random plant with an explicit safe backbone."""
    rng = random.Random(seed)
    marked_count = max(1, int(n_states * marked_fraction))
    marked = set(rng.sample(range(1, n_states), marked_count))
    forbidden_candidates = [s for s in range(1, n_states) if s not in marked]
    forbidden_count = max(1, int(n_states * forbidden_fraction))
    forbidden = set(rng.sample(forbidden_candidates, forbidden_count))

    transitions = []
    target = min(marked)
    mids = [s for s in range(1, n_states) if s not in marked and s not in forbidden]
    rng.shuffle(mids)

    current = 0
    for nxt in mids[: min(6, len(mids))]:
        transitions.append(Transition(current, f"backbone_{current}_{nxt}", nxt, True))
        current = nxt
    transitions.append(Transition(current, f"backbone_complete_{target}", target, True))

    for state in range(n_states):
        for edge_idx in range(out_degree):
            dst = rng.randrange(n_states)
            controllable = rng.random() > uncontrollable_fraction
            protected = controllable and rng.random() < 0.18
            transitions.append(
                Transition(state, f"e{state}_{edge_idx}_{dst}", dst, controllable, protected=protected)
            )

    return Plant(
        name=f"random_{n_states}_{seed}", n_states=n_states, initial=0,
        marked=frozenset(marked), forbidden=frozenset(forbidden),
        transitions=tuple(transitions), labels={state: str(state) for state in range(n_states)},
    )
