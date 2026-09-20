"""Independent exhaustive verification for the AESC fixed-point implementation."""
from __future__ import annotations

import argparse
import csv
import itertools
import random
from pathlib import Path
from typing import Set

from aesc import Plant, Transition, synthesize_supervisor


def _is_closed_and_nonblocking(plant: Plant, subset: Set[int]) -> bool:
    if not subset or subset & set(plant.forbidden):
        return False
    outgoing = {s: [] for s in range(plant.n_states)}
    reverse = {s: [] for s in range(plant.n_states)}
    for tr in plant.transitions:
        outgoing[tr.src].append(tr)
        reverse[tr.dst].append(tr)
    for state in subset:
        for tr in outgoing[state]:
            if not tr.controllable and tr.dst not in subset:
                return False
    coreach = set(plant.marked) & subset
    frontier = list(coreach)
    while frontier:
        dst = frontier.pop()
        for tr in reverse[dst]:
            if tr.src in subset and tr.dst in subset and tr.src not in coreach:
                coreach.add(tr.src)
                frontier.append(tr.src)
    return coreach == subset


def brute_force_winning_states(plant: Plant) -> frozenset[int]:
    safe_states = sorted(set(range(plant.n_states)) - set(plant.forbidden))
    winning_union: Set[int] = set()
    for r in range(1, len(safe_states) + 1):
        for combo in itertools.combinations(safe_states, r):
            subset = set(combo)
            if _is_closed_and_nonblocking(plant, subset):
                winning_union.update(subset)
    return frozenset(winning_union)


def random_small_plant(n_states: int, seed: int) -> Plant:
    rng = random.Random(seed)
    states = list(range(n_states))
    marked = frozenset(rng.sample(states, rng.randint(1, max(1, min(2, n_states)))))
    forbidden_candidates = [s for s in states if s not in marked]
    forbidden = frozenset(rng.sample(
        forbidden_candidates,
        rng.randint(0, min(2, len(forbidden_candidates)))
    ))
    transitions = []
    tid = 0
    for src in states:
        for _ in range(rng.randint(1, min(3, n_states))):
            dst = rng.randrange(n_states)
            transitions.append(Transition(
                src=src, event=f"e{tid}", dst=dst,
                controllable=(rng.random() >= 0.30), protected=False,
            ))
            tid += 1
    return Plant(
        name=f"oracle_{n_states}_{seed}", n_states=n_states, initial=0,
        marked=marked, forbidden=forbidden, transitions=tuple(transitions),
        labels={s: str(s) for s in states},
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--plants", type=int, default=5000)
    parser.add_argument("--seed", type=int, default=20260919)
    parser.add_argument("--out", type=Path, default=Path("../results/exhaustive_oracle_summary.csv"))
    args = parser.parse_args()

    rng = random.Random(args.seed)
    mismatches = []
    counts = {n: 0 for n in range(3, 9)}
    for idx in range(args.plants):
        n = rng.randint(3, 8)
        counts[n] += 1
        plant = random_small_plant(n, args.seed + idx * 7919 + n)
        expected = brute_force_winning_states(plant)
        actual = synthesize_supervisor(plant).winning_states
        if expected != actual:
            mismatches.append((plant.name, sorted(expected), sorted(actual)))
            if len(mismatches) >= 10:
                break

    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["seed","requested_plants","checked_plants","mismatches","states_3","states_4","states_5","states_6","states_7","states_8"])
        checked = sum(counts.values()) if not mismatches else idx + 1
        writer.writerow([args.seed,args.plants,checked,len(mismatches),*(counts[n] for n in range(3,9))])

    if mismatches:
        for mismatch in mismatches:
            print("MISMATCH", mismatch)
        raise SystemExit(1)
    print(f"Exhaustive oracle verification passed for {args.plants} random plants (3-8 states).")


if __name__ == "__main__":
    main()
