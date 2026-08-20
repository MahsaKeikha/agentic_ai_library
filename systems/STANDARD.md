# Unified System Engineering Standard

Every system under `systems/` should follow the same minimum engineering contract.

## Required artifacts

1. `README.md` with scope, workflow, human gate, limitations, and quick start.
2. `manifest.json` with stable ID, name, category, agents, capabilities, risks, and status.
3. `run.py` with a deterministic offline path.
4. `examples/` with at least one structured example input.
5. `tests/` with checks for required outputs, human control, and evidence discipline.
6. `EVALUATION.md` with quality, safety, grounding, and release criteria.

## Behavioral requirements

- Do not invent missing material facts.
- Separate evidence, assumptions, hypotheses, risks, and recommendations.
- Use a human approval gate before consequential external actions.
- Sensitive-domain systems must state their professional limitations.
- Offline examples must run without external APIs.
- Stable IDs must not be renumbered after release.

## Recommended production additions

Production deployments should add authentication, authorization, audit logging, provenance, model/version tracking, secrets management, observability, cost controls, evaluation datasets, and organization-specific policies.
