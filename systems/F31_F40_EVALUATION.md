# F31-F40 Evaluation Framework

The AI Engineering batch is evaluated as engineering decision support, not autonomous production control.

## Common release criteria

- Required evidence is either supplied or explicitly marked missing.
- No agent silently converts assumptions into facts.
- Specialized roles produce traceable state entries.
- Human approval is required before consequential deployment or release.
- Tests cover registration, missing evidence, and gate behavior.
- Production implementations add authentication, authorization, audit logs, provenance, model/version tracking, secrets management, and organization-specific controls.

## System-specific evaluation focus

| ID | Evaluation focus |
|---|---|
| F31 | model quality, generalization, leakage, reproducibility, risk |
| F32 | deployment safety, rollback readiness, observability, release integrity |
| F33 | schema correctness, data quality, lineage, freshness, reliability |
| F34 | task success, robustness, regression tests, injection resistance, version traceability |
| F35 | retrieval recall/precision, grounding, citation correctness, unsupported-answer rate |
| F36 | routing accuracy, task completion, state consistency, conflict resolution, gate enforcement |
| F37 | evaluation validity, judge reliability, bias coverage, safety coverage, reproducibility |
| F38 | benchmark validity, dataset integrity, metric correctness, repeatability, contamination controls |
| F39 | requirement quality, user-value evidence, prioritization rationale, AI risk, launch readiness |
| F40 | availability, latency, capacity, security, cost, failure isolation, recovery |

## Red-team expectations

Every system should eventually be tested against missing data, conflicting evidence, malformed inputs, untrusted embedded instructions, stale state, partial tool failure, and attempts to bypass the human gate.
