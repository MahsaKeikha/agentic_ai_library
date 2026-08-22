# F01-F170 Gold Standard Audit Scorecard

Use this scorecard to evaluate every standalone repository consistently. The score is diagnostic only. Gold Standard promotion still requires every mandatory acceptance gate to pass.

## Scoring

Each category is scored 0-5.

- 0: absent
- 1: placeholder
- 2: partial draft
- 3: meaningful implementation
- 4: verified and well-tested
- 5: exemplary reference quality

Maximum score: 100.

## Categories

| Category | Weight | Gold Standard expectation |
|---|---:|---|
| Agent specialization | 5 | Distinct responsibilities, contracts, failure modes, and domain reasoning |
| Orchestration | 5 | Explicit routing, state transitions, retries, conflicts, approvals, termination |
| State and schemas | 5 | Structured facts, assumptions, provenance, uncertainty, blockers, approvals |
| Domain tools | 5 | Real calculations, validation, adapters, retrieval, scoring, or transformations |
| Skills/prompts | 5 | Reusable domain methods with clear inputs, outputs, and limits |
| Memory | 5 | Purposeful retention, stale-data handling, privacy boundaries |
| Observability | 5 | Inspectable traces for agents, tools, state changes, failures, approvals |
| Evidence discipline | 5 | Provenance, conflicts, missing evidence, stale evidence, uncertainty |
| Safety/governance | 5 | Domain-specific scope, gates, escalation, prohibited actions |
| Human authority | 5 | Consequential actions cannot bypass explicit authorization |
| Unit testing | 5 | Behavioral agent/tool tests rather than status-only checks |
| Integration testing | 5 | Orchestrator and state transitions exercised end to end |
| Failure/adversarial testing | 5 | Tool failures, malformed input, conflicts, red-team scenarios |
| Evaluation | 5 | Metrics, methodology, fixtures, reproducible results |
| Benchmarks | 5 | Normal and difficult benchmark cases with interpretation |
| Reproducibility | 5 | Fresh clone, install, offline core run, deterministic examples |
| CI/engineering hygiene | 5 | Green CI, supported versions, package metadata, no secrets |
| Documentation | 5 | README plus architecture, agents, evaluation, safety, extending |
| Open-source governance | 5 | LICENSE, CITATION, CONTRIBUTING, SECURITY, CHANGELOG, templates |
| Teaching/reference value | 5 | Clear enough to learn from, extend, compare, and cite |

## Score interpretation

- 0-34: L0 Scaffold
- 35-59: L1 Reference Draft
- 60-84: L2 candidate, but only Verified Reference if all mandatory gates pass
- 85-100: L3 candidate, but Gold Standard only if all mandatory gates pass

A high numerical score cannot override a mandatory blocker such as failing CI, unsafe consequential execution, broken reproducibility, missing critical evidence controls, or placeholder logic in the critical path.

## Mandatory blockers

Any one of the following blocks L3 promotion:

- placeholder/pass-through critical agent;
- critical tool returning hard-coded or echoed output;
- failing required tests;
- failing required CI;
- no reproducible end-to-end run;
- no domain-specific safety model;
- consequential external action without approval gate;
- misleading capability claim;
- missing required provenance/evidence controls for evidence-dependent systems;
- secrets or credentials in repository;
- missing LICENSE or citation metadata;
- required links broken;
- unresolved high-severity security issue.

## Audit record format

For each repository record:

```text
ID:
Repository:
Domain:
Current maturity:
Target maturity: L3 Gold Standard
Score: /100
Mandatory blockers:
Top strengths:
Top gaps:
Required remediation:
Tests executed:
CI status:
Benchmark status:
Reviewer notes:
Promotion decision:
```

## Review philosophy

The audit should reward working depth, not cosmetic uniformity. A legacy repository with meaningful orchestration and real domain logic may score higher than a modern repository containing every expected folder but only placeholder functions.

The objective is to preserve strong existing implementations, modernize their quality layers, and deepen thin repositories until every F01-F170 system earns Gold Standard status on evidence rather than appearance.
