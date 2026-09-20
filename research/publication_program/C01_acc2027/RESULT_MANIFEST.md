# C01 verified result manifest

Updated: 2026-09-19

## Paper

**Supervisory Control of Protected Actions in Tool-Using Multi-Agent AI**

## Verification status

- Four synthetic Atlas-derived workflow abstractions.
- Three controller conditions per abstraction.
- 100,000 seeded rollouts per controller/case.
- 1,200,000 total case-study rollouts.
- Seven scaling sizes from 25 to 2,000 states.
- Thirty feasible seeded random plants per scaling size.
- Independent brute-force oracle: 5,000 random automata with 3 to 8 states and **zero winning-set mismatches**.
- Regression suite: **4 passed, 0 failed**.

## Recorded case-study outcomes

| Case | Unconstrained violation | Pointwise deadlock | AESC violation | AESC deadlock | AESC complete | AESC review |
|---|---:|---:|---:|---:|---:|---:|
| Software release | 7.624% | 7.757% | 0 | 0 | 84.495% | 15.505% |
| Industrial digital twin | 10.386% | 10.527% | 0 | 0 | 84.776% | 15.224% |
| AgeWell support | 6.283% | 6.260% | 0 | 0 | 84.743% | 15.257% |
| Smart city | 9.544% | 9.487% | 0 | 0 | 84.596% | 15.404% |

The AESC zeroes are expected for rollouts restricted to the synthesized safe/nonblocking winning set. They are model-level implementation checks, not empirical real-world safety estimates.

## Recorded scaling outcome

The recorded reference run produced median synthesis time of 0.066 ms at 25 states and 21.904 ms at 2,000 states. At 2,000 states, the median winning set retained 88.875% of plant states and 79.989% of transitions, with a median of eight fixed-point iterations.

Wall-clock timing is environment-dependent and may vary slightly when rerun.

## Exact commands

    cd code
    python run_experiments.py --runs 100000 --seed 20260919 --replicates 30 --out ../results
    python verify_synthesis.py --plants 5000 --seed 20260919 --out ../results/exhaustive_oracle_summary.csv
    cd ..
    python -m pytest -q tests

## Scientific claim boundary

The benchmark is synthetic and validates a finite-state implementation against its modeled semantics. It is not evidence of real-world safety, empirical invalidation frequency, clinical efficacy, infrastructure reliability, security certification, or production readiness. Correctness is conditional on the task automaton, controllability classification, observation assumptions, and policy predicates accurately representing the system being controlled.

The separately sealed submission artifact records SHA-256 checksums for the exact manuscript, source, result, and figure snapshots used to compile the current five-page PDF.
