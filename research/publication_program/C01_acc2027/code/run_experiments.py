"""Reproduce Paper 1 synthetic experiments.

Usage:
    python run_experiments.py --runs 100000 --seed 20260919 --out ../results
"""
from __future__ import annotations

import argparse
import csv
import random
import statistics
import time
from collections import Counter, defaultdict
from pathlib import Path

from aesc import Plant, all_transition_ids, pointwise_gate_transition_ids, synthesize_supervisor
from benchmarks import atlas_case_studies, random_feasible_plant

CONTROLLERS = ("unconstrained", "pointwise_gate", "aesc")


def _enabled_ids(plant: Plant, controller: str):
    if controller == "unconstrained":
        return all_transition_ids(plant)
    if controller == "pointwise_gate":
        return pointwise_gate_transition_ids(plant)
    if controller == "aesc":
        return synthesize_supervisor(plant).enabled_transition_ids
    raise ValueError(controller)


def simulate_case(plant, controller, runs, seed, invalidation_probability):
    rng = random.Random(seed)
    enabled = set(_enabled_ids(plant, controller))
    outgoing = defaultdict(list)
    for idx, tr in enumerate(plant.transitions):
        outgoing[tr.src].append((idx, tr))

    counts = Counter()
    step_counts = []
    for _ in range(runs):
        state = plant.initial
        steps = 0
        for _ in range(20):
            steps += 1
            if state in plant.marked:
                counts["complete" if state == 5 else "human_review"] += 1
                break
            if state in plant.forbidden:
                counts["violation"] += 1
                break

            uncontrollable = [
                (idx, tr) for idx, tr in outgoing[state]
                if (not tr.controllable) and idx in enabled
            ]
            if uncontrollable and rng.random() < invalidation_probability:
                state = uncontrollable[0][1].dst
                continue

            candidates = [
                (idx, tr) for idx, tr in outgoing[state]
                if tr.controllable and idx in enabled and tr.dst != state
            ]
            if not candidates:
                counts["deadlock"] += 1
                break

            weights = []
            for _, tr in candidates:
                if tr.src == 1:
                    if "unbound" in tr.event or "unpinned" in tr.event:
                        weight = 0.35
                    elif "review" in tr.event:
                        weight = 0.10
                    else:
                        weight = 0.55
                else:
                    weight = 1.0
                weights.append(weight)

            draw = rng.random() * sum(weights)
            cumulative = 0.0
            for (_, tr), weight in zip(candidates, weights):
                cumulative += weight
                if draw <= cumulative:
                    state = tr.dst
                    break
        else:
            counts["timeout"] += 1
        step_counts.append(steps)

    return {
        "complete": counts["complete"] / runs,
        "human_review": counts["human_review"] / runs,
        "violation": counts["violation"] / runs,
        "deadlock": counts["deadlock"] / runs,
        "timeout": counts["timeout"] / runs,
        "mean_steps": statistics.mean(step_counts),
    }


def run_case_studies(runs: int, seed: int):
    rows = []
    for case_index, (plant, invalidation_probability) in enumerate(atlas_case_studies()):
        supervisor = synthesize_supervisor(plant)
        for controller_index, controller in enumerate(CONTROLLERS):
            metrics = simulate_case(
                plant, controller, runs,
                seed + 1000 * case_index + 17 * controller_index,
                invalidation_probability,
            )
            rows.append({
                "case": plant.name,
                "controller": controller,
                "runs": runs,
                "seed": seed + 1000 * case_index + 17 * controller_index,
                "invalidation_probability": invalidation_probability,
                "winning_states": len(supervisor.winning_states),
                "total_states": plant.n_states,
                **metrics,
            })
    return rows


def run_scaling(seed: int, replicates: int = 30):
    sizes = [25, 50, 100, 250, 500, 1000, 2000]
    rows = []
    for n_states in sizes:
        timings, state_retention, transition_retention, iterations = [], [], [], []
        attempts = accepted = 0
        while accepted < replicates and attempts < replicates * 50:
            attempts += 1
            trial_seed = seed + n_states * 1000 + attempts
            plant = random_feasible_plant(n_states, trial_seed)
            start = time.perf_counter()
            supervisor = synthesize_supervisor(plant)
            elapsed_ms = (time.perf_counter() - start) * 1000.0
            if plant.initial not in supervisor.winning_states:
                continue
            accepted += 1
            timings.append(elapsed_ms)
            state_retention.append(len(supervisor.winning_states) / plant.n_states)
            transition_retention.append(len(supervisor.enabled_transition_ids) / len(plant.transitions))
            iterations.append(supervisor.fixpoint_iterations)
        rows.append({
            "states": n_states,
            "replicates": accepted,
            "median_synthesis_ms": statistics.median(timings),
            "median_state_retention": statistics.median(state_retention),
            "median_transition_retention": statistics.median(transition_retention),
            "median_fixpoint_iterations": statistics.median(iterations),
        })
    return rows


def write_csv(path: Path, rows):
    rows = list(rows)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--runs", type=int, default=100000)
    parser.add_argument("--seed", type=int, default=20260919)
    parser.add_argument("--replicates", type=int, default=30)
    parser.add_argument("--out", type=Path, default=Path("../results"))
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    write_csv(args.out / "case_study_summary.csv", run_case_studies(args.runs, args.seed))
    write_csv(args.out / "scaling_summary.csv", run_scaling(args.seed, args.replicates))
    print("Wrote case-study and scaling results.")


if __name__ == "__main__":
    main()
