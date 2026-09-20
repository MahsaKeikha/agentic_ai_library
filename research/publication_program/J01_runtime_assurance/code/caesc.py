from __future__ import annotations

from collections import defaultdict, deque
from dataclasses import dataclass
from time import perf_counter
from typing import Callable, Dict, FrozenSet, List, Mapping, Sequence, Set, Tuple


@dataclass(frozen=True)
class Transition:
    src: int
    event: str
    dst: int
    controllable: bool


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
    iterations: int


@dataclass(frozen=True)
class ProductModel:
    plant: Plant
    tuples: Tuple[Tuple[int, ...], ...]


def synthesize(plant: Plant) -> Supervisor:
    outgoing: Dict[int, List[Tuple[int, Transition]]] = defaultdict(list)
    incoming: Dict[int, List[Tuple[int, Transition]]] = defaultdict(list)
    for idx, tr in enumerate(plant.transitions):
        outgoing[tr.src].append((idx, tr))
        incoming[tr.dst].append((idx, tr))

    winning: Set[int] = set(range(plant.n_states)) - set(plant.forbidden)
    iterations = 0
    changed = True
    while changed:
        iterations += 1
        changed = False
        uc_bad = {
            s for s in winning
            if any((not tr.controllable) and tr.dst not in winning for _, tr in outgoing[s])
        }
        if uc_bad:
            winning.difference_update(uc_bad)
            changed = True

        coreach = set(plant.marked).intersection(winning)
        queue = deque(coreach)
        while queue:
            dst = queue.popleft()
            for _, tr in incoming[dst]:
                if tr.src in winning and tr.dst in winning and tr.src not in coreach:
                    coreach.add(tr.src)
                    queue.append(tr.src)

        if coreach != winning:
            winning.intersection_update(coreach)
            changed = True

    enabled = frozenset(
        idx for idx, tr in enumerate(plant.transitions)
        if tr.src in winning and tr.dst in winning
    )
    return Supervisor(frozenset(winning), enabled, iterations)


def local_viability_sets(components: Sequence[Plant]) -> Tuple[FrozenSet[int], ...]:
    return tuple(synthesize(c).winning_states for c in components)


def _indices(component: Plant):
    alphabet = set()
    by_state: Dict[int, Dict[str, List[Transition]]] = defaultdict(lambda: defaultdict(list))
    ctrl: Dict[str, bool] = {}
    for tr in component.transitions:
        alphabet.add(tr.event)
        by_state[tr.src][tr.event].append(tr)
        if tr.event in ctrl and ctrl[tr.event] != tr.controllable:
            raise ValueError(f"inconsistent controllability for event {tr.event}")
        ctrl[tr.event] = tr.controllable
    return alphabet, by_state, ctrl


def compose_reachable(
    components: Sequence[Plant],
    coupling_forbidden: Callable[[Tuple[int, ...]], bool] | None = None,
    local_allowed: Sequence[Set[int] | FrozenSet[int]] | None = None,
) -> ProductModel:
    if not components:
        raise ValueError("at least one component is required")
    coupling_forbidden = coupling_forbidden or (lambda _: False)

    alphabets = []
    by_state = []
    global_ctrl: Dict[str, bool] = {}
    for component in components:
        alphabet, indexed, ctrl = _indices(component)
        alphabets.append(alphabet)
        by_state.append(indexed)
        for event, controllable in ctrl.items():
            if event in global_ctrl and global_ctrl[event] != controllable:
                raise ValueError(f"shared event {event} has inconsistent controllability")
            global_ctrl[event] = controllable

    initial = tuple(c.initial for c in components)
    ids = {initial: 0}
    tuples = [initial]
    transitions = []
    queue = deque([initial])

    while queue:
        state = queue.popleft()
        state_id = ids[state]
        events = set().union(*(by_state[i][state[i]].keys() for i in range(len(components))))
        for event in sorted(events):
            participants = [i for i, alphabet in enumerate(alphabets) if event in alphabet]
            choices = []
            valid = True
            for i in participants:
                enabled = by_state[i][state[i]].get(event, [])
                if len(enabled) != 1:
                    valid = False
                    break
                choices.append((i, enabled[0]))
            if not valid:
                continue

            nxt = list(state)
            for i, tr in choices:
                nxt[i] = tr.dst
            nxt = tuple(nxt)

            if local_allowed is not None and any(
                nxt[i] not in local_allowed[i] for i in range(len(components))
            ):
                continue

            if nxt not in ids:
                ids[nxt] = len(tuples)
                tuples.append(nxt)
                queue.append(nxt)
            transitions.append(Transition(state_id, event, ids[nxt], global_ctrl[event]))

    forbidden = set()
    marked = set()
    labels = {}
    for idx, state in enumerate(tuples):
        labels[idx] = "|".join(str(x) for x in state)
        local_forbidden = any(
            state[i] in components[i].forbidden for i in range(len(components))
        )
        if local_forbidden or coupling_forbidden(state):
            forbidden.add(idx)
        if all(state[i] in components[i].marked for i in range(len(components))):
            marked.add(idx)

    return ProductModel(
        Plant(
            name=" || ".join(c.name for c in components),
            n_states=len(tuples),
            initial=0,
            marked=frozenset(marked),
            forbidden=frozenset(forbidden),
            transitions=tuple(transitions),
            labels=labels,
        ),
        tuple(tuples),
    )


def compositional_synthesize(
    components: Sequence[Plant],
    coupling_forbidden: Callable[[Tuple[int, ...]], bool] | None = None,
):
    local_sets = local_viability_sets(components)
    product_model = compose_reachable(
        components,
        coupling_forbidden=coupling_forbidden,
        local_allowed=local_sets,
    )
    supervisor = synthesize(product_model.plant)
    return local_sets, product_model, supervisor


def monolithic_synthesize(
    components: Sequence[Plant],
    coupling_forbidden: Callable[[Tuple[int, ...]], bool] | None = None,
):
    product_model = compose_reachable(components, coupling_forbidden=coupling_forbidden)
    supervisor = synthesize(product_model.plant)
    return product_model, supervisor


def winning_tuples(model: ProductModel, supervisor: Supervisor) -> FrozenSet[Tuple[int, ...]]:
    return frozenset(model.tuples[i] for i in supervisor.winning_states)


def benchmark_synthesis(components, coupling_forbidden=None):
    t0 = perf_counter()
    mono_model, mono_sup = monolithic_synthesize(components, coupling_forbidden)
    t1 = perf_counter()
    local_sets, comp_model, comp_sup = compositional_synthesize(
        components, coupling_forbidden
    )
    t2 = perf_counter()
    return {
        "components": len(components),
        "monolithic_states": mono_model.plant.n_states,
        "pruned_states": comp_model.plant.n_states,
        "monolithic_transitions": len(mono_model.plant.transitions),
        "pruned_transitions": len(comp_model.plant.transitions),
        "monolithic_winning": len(mono_sup.winning_states),
        "compositional_winning": len(comp_sup.winning_states),
        "monolithic_ms": (t1 - t0) * 1000.0,
        "compositional_ms": (t2 - t1) * 1000.0,
        "equivalent": winning_tuples(mono_model, mono_sup)
        == winning_tuples(comp_model, comp_sup),
        "local_sizes": ";".join(str(len(s)) for s in local_sets),
    }
