"""Reproduce Paper 1 synthetic experiments."""
from __future__ import annotations

import argparse
import csv
import random
import statistics
import time
from collections import Counter, defaultdict
from pathlib import Path

from aesc import (
    Plant,
    all_transition_ids,
    pointwise_gate_transition_ids,
    precursor_vulnerability,
    synthesize_supervisor,
)
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
        vulnerability = precursor_vulnerability(plant)
        for controller_index, controller in enumerate(CONTROLLERS):
            metrics = simulate_case(
                plant,
                controller,
                runs,
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
                "pointwise_reachable_states": len(vulnerability["reachable_pointwise"]),
                "precursor_vulnerable_states": len(vulnerability["vulnerable_states"]),
                "suppressed_precursor_transitions": len(vulnerability["precursor_transition_ids"]),
                **metrics,
            })
    return rows


def run_scaling(seed: int, replicates: int = 30):
    sizes = [25, 50, 100, 250, 500, 1000, 2000]
    rows = []
    for n_states in sizes:
        timings, state_retention, transition_retention, iterations = [], [], [], []
        vulnerability_state_fraction = []
        attempts = accepted = 0
        while accepted < replicates and attempts < replicates * 100:
            attempts += 1
            trial_seed = seed + n_states * 1000 + attempts
            plant = random_feasible_plant(n_states, trial_seed)
            start = time.perf_counter()
            supervisor = synthesize_supervisor(plant)
            elapsed_ms = (time.perf_counter() - start) * 1000.0
            if plant.initial not in supervisor.winning_states:
                continue
            accepted += 1
            vuln = precursor_vulnerability(plant)
            timings.append(elapsed_ms)
            state_retention.append(len(supervisor.winning_states) / plant.n_states)
            transition_retention.append(len(supervisor.enabled_transition_ids) / len(plant.transitions))
            iterations.append(supervisor.fixpoint_iterations)
            vulnerability_state_fraction.append(len(vuln["vulnerable_states"]) / plant.n_states)
        rows.append({
            "states": n_states,
            "replicates": accepted,
            "median_synthesis_ms": statistics.median(timings),
            "median_state_retention": statistics.median(state_retention),
            "median_transition_retention": statistics.median(transition_retention),
            "median_fixpoint_iterations": statistics.median(iterations),
            "median_precursor_vulnerability_fraction": statistics.median(vulnerability_state_fraction),
        })
    return rows


def run_vulnerability_survey(seed: int, plants_per_size: int = 100):
    sizes = [25, 50, 100, 250, 500]
    rows = []
    for n_states in sizes:
        accepted = 0
        attempts = 0
        vulnerable_count = 0
        fractions = []
        precursor_counts = []
        while accepted < plants_per_size and attempts < plants_per_size * 200:
            attempts += 1
            plant = random_feasible_plant(n_states, seed + 3100000 + n_states * 1000 + attempts)
            supervisor = synthesize_supervisor(plant)
            if plant.initial not in supervisor.winning_states:
                continue
            accepted += 1
            vuln = precursor_vulnerability(plant)
            v = len(vuln["vulnerable_states"])
            p = len(vuln["precursor_transition_ids"])
            if v > 0:
                vulnerable_count += 1
            fractions.append(v / n_states)
            precursor_counts.append(p)
        rows.append({
            "states": n_states,
            "plants": accepted,
            "plants_with_pointwise_vulnerability": vulnerable_count,
            "vulnerability_prevalence": vulnerable_count / accepted if accepted else 0.0,
            "median_vulnerable_state_fraction": statistics.median(fractions),
            "median_suppressed_precursor_transitions": statistics.median(precursor_counts),
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
    parser.add_argument("--survey-plants", type=int, default=100)
    parser.add_argument("--out", type=Path, default=Path("../results"))
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    write_csv(args.out / "case_study_summary.csv", run_case_studies(args.runs, args.seed))
    write_csv(args.out / "scaling_summary.csv", run_scaling(args.seed, args.replicates))
    write_csv(args.out / "vulnerability_survey.csv", run_vulnerability_survey(args.seed, args.survey_plants))
    print("Wrote case study, scaling, and vulnerability results.")


if __name__ == "__main__":
    main()
