from __future__ import annotations

from caesc import Plant, Transition


def precursor_component(i: int) -> Plant:
    p = f"c{i}_"
    labels = {
        0: "start",
        1: "assessed",
        2: "binding_secured",
        3: "unsecured_commitment",
        4: "binding_invalidated",
        5: "complete",
        6: "human_review",
        7: "violation",
    }
    transitions = (
        Transition(0, p + "assess", 1, True),
        Transition(1, p + "bind", 2, True),
        Transition(1, p + "unsecured_prepare", 3, True),
        Transition(1, p + "review", 6, True),
        Transition(2, p + "protected_action", 5, True),
        Transition(3, p + "protected_action", 5, True),
        Transition(3, p + "evidence_expire", 4, False),
        Transition(4, p + "protected_action", 7, True),
    )
    return Plant(
        f"precursor_{i}",
        8,
        0,
        frozenset({5, 6}),
        frozenset({7}),
        transitions,
        labels,
    )


def authority_component(i: int) -> Plant:
    p = f"a{i}_"
    labels = {
        0: "start",
        1: "ready",
        2: "authority_claimed",
        3: "complete",
        4: "human_review",
        5: "authority_revoked",
        6: "violation",
    }
    transitions = (
        Transition(0, p + "assess", 1, True),
        Transition(1, p + "claim_authority", 2, True),
        Transition(1, p + "review", 4, True),
        Transition(2, p + "protected_action", 3, True),
        Transition(2, p + "revoke", 5, False),
        Transition(5, p + "review_after_revoke", 4, True),
        Transition(5, p + "protected_action", 6, True),
    )
    return Plant(
        f"authority_{i}",
        7,
        0,
        frozenset({3, 4}),
        frozenset({6}),
        transitions,
        labels,
    )


def at_most_one_authority_claimed(state):
    return sum(1 for s in state if s == 2) > 1
