# Reproducibility package

## Paper

**Supervisory Control of Protected Actions in Tool-Using Multi-Agent AI**

This directory contains the finite-state supervisor implementation, four synthetic case abstractions, independent exhaustive verification, and seeded experiment outputs used for Paper 1.

## Quick verification

Run:

    python -m pytest -q tests

Expected result: 4 passed.

## Reproduce experiments

    cd code
    python run_experiments.py --runs 100000 --seed 20260919 --replicates 30 --out ../results
    python verify_synthesis.py --plants 5000 --seed 20260919 --out ../results/exhaustive_oracle_summary.csv

The case-study rollouts are seeded. Scaling wall-clock timing can vary across machines; the result manifest records the values used in the manuscript draft.

## Scientific boundary

All case studies are synthetic finite-state abstractions. The repository does not claim clinical, industrial, municipal, or production deployment validation. AESC guarantees apply only to the modeled discrete-event system and its stated assumptions.

## ACC formatting note

The locally verified PDF is a two-column IEEE conference draft. ACC/PaperPlaza specifies ieeeconf.cls; compile the source with the official class before upload and run the PaperPlaza PDF compliance test.
