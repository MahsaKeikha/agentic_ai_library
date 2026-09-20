"""Authority-Evidence Supervisory Control (AESC).

Finite-state reference implementation for the Paper 1 reproducibility package.

The implementation computes the largest state subset that is:
1) outside modeled forbidden states,
2) closed under uncontrollable transitions, and
3) nonblocking with respect to accepted marked states.

The returned supervisor disables controllable transitions whose destination lies
outside the winning set. It does not disable uncontrollable events.

This is a research reference implementation, not a production authorization
engine.
"""
from __future__ import annotations

from collections import defaultdict, deque
from dataclasses import dataclass
from typing import Dict, FrozenSet, Iterable, List, Mapping, Set, Tuple


@dataclass(frozen=True)
class Transition:
    src: int
    event: str
    dst: int
    controllable: bool
    protected: bool = False


@dataclass(frozen=True)
class Plant:
    name: str
    n_states: int
    initial: int
    marked: FrozenSet[int]
    forbidden: FrozenSet[int]
    transitions: Tuple[Transition, ...]
    labels: Mapping[int, str]


@dataclass(frozen=True)
class Supervisor:
    winning_states: FrozenSet[int]
    enabled_transition_ids: FrozenSet[int]
    fixpoint_iterations: int

    def enables(self, transition_id: int) -> bool:
        return transition_id in self.enabled_transition_ids


def synthesize_supervisor(plant: Plant) -> Supervisor:
    """Compute the maximal safe, uncontrollable-closed, nonblocking state set."""
    outgoing: Dict[int, List[Tuple[int, Transition]]] = defaultdict(list)
    incoming: Dict[int, List[Tuple[int, Transition]]] = defaultdict(list)
    for idx, tr in enumerate(plant.transitions):
        outgoing[tr.src].append((idx, tr))
        incoming[tr.dst].append((idx, tr))

    winning: Set[int] = set(range(plant.n_states)) - set(plant.forbidden)
    changed = True
    iterations = 0

    while changed:
        iterations += 1
        changed = False

        uncontrollable_bad = {
            state
            for state in winning
            if any((not tr.controllable) and tr.dst not in winning for _, tr in outgoing[state])
        }
        if uncontrollable_bad:
            winning.difference_update(uncontrollable_bad)
            changed = True

        coreachable = set(plant.marked).intersection(winning)
        queue = deque(coreachable)
        while queue:
            dst = queue.popleft()
            for _, tr in incoming[dst]:
                if tr.src in winning and tr.dst in winning and tr.src not in coreachable:
                    coreachable.add(tr.src)
                    queue.append(tr.src)

        if coreachable != winning:
            winning.intersection_update(coreachable)
            changed = True

    enabled = {
        idx for idx, tr in enumerate(plant.transitions)
        if tr.src in winning and tr.dst in winning
    }

    return Supervisor(
        winning_states=frozenset(winning),
        enabled_transition_ids=frozenset(enabled),
        fixpoint_iterations=iterations,
    )


def reachable_states(plant: Plant, enabled_transition_ids: Iterable[int]) -> FrozenSet[int]:
    enabled = set(enabled_transition_ids)
    outgoing: Dict[int, List[Tuple[int, Transition]]] = defaultdict(list)
    for idx, tr in enumerate(plant.transitions):
        if idx in enabled:
            outgoing[tr.src].append((idx, tr))

    seen = {plant.initial}
    queue = deque([plant.initial])
    while queue:
        src = queue.popleft()
        for _, tr in outgoing[src]:
            if tr.dst not in seen:
                seen.add(tr.dst)
                queue.append(tr.dst)
    return frozenset(seen)


def pointwise_gate_transition_ids(plant: Plant) -> FrozenSet[int]:
    """Immediate-only baseline; blocks only controllable transitions directly into forbidden states."""
    return frozenset(
        idx for idx, tr in enumerate(plant.transitions)
        if (not tr.controllable) or tr.dst not in plant.forbidden
    )


def all_transition_ids(plant: Plant) -> FrozenSet[int]:
    return frozenset(range(len(plant.transitions)))
