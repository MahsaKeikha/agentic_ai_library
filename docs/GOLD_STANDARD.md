# Agentic AI Library Gold Standard v1.0

This document defines the minimum bar for every F01-F170 repository in the Agentic AI Library. A repository is not considered Gold Standard because it contains the right folders. It must demonstrate substantive multi-agent reasoning, reproducible execution, measurable evaluation, domain-specific safety, and open-source engineering quality.

## 1. Purpose

The goal is to make every repository independently useful as a reference implementation that researchers, engineers, educators, reviewers, and organizations can study, run, test, extend, and cite.

## 2. Gold Standard principles

1. **Substantive multi-agent behavior**: agents must perform meaningfully different reasoning tasks. Role names alone do not qualify.
2. **Explicit orchestration**: routing, state transitions, retries, conflicts, approvals, and termination conditions must be visible in code.
3. **Structured state and contracts**: agent inputs and outputs must use documented schemas. Missing evidence, uncertainty, provenance, assumptions, conflicts, and unresolved risks must be representable.
4. **Domain-specific tools and skills**: tools must implement useful domain logic, validation, calculations, adapters, retrieval, transformation, or decision-support operations rather than pass-through placeholders.
5. **Human authority for consequential actions**: systems must distinguish analysis from execution and require explicit authorization for high-impact external actions.
6. **Evaluation before claims**: no repository may claim maturity without passing deterministic tests, adversarial tests, safety tests, and end-to-end examples.
7. **Reproducibility**: a fresh clone must install and run using documented commands. Core examples must work offline unless the repository explicitly documents an external dependency.
8. **Observability**: significant agent decisions, tool calls, state changes, failures, and approvals must be traceable.
9. **Evidence discipline**: systems must preserve provenance and surface missing, weak, stale, or conflicting evidence.
10. **Open reference quality**: documentation, licensing, citation, contribution guidance, security reporting, changelog, CI, and templates are required.

## 3. Required repository structure

Every modernized repository should contain the following unless a documented exception applies:

```text
.github/
  workflows/
  ISSUE_TEMPLATE/
  pull_request_template.md
AGENTS/
SKILLS/
TOOLS/
benchmarks/
config/
docs/
evals/
examples/
memory/
observability/
orchestration/
prompts/
safety/
schemas/
state/
tests/
CHANGELOG.md
CITATION.cff
CONTRIBUTING.md
LICENSE
README.md
SECURITY.md
pyproject.toml
run.py
```

Legacy repositories may preserve their richer existing modules, but the modern interface and quality layers above must be added around them rather than replacing substantive code with scaffolding.

## 4. Multi-agent architecture requirements

Each repository must have at least four specialized agents, with five or more preferred for complex domains. For every agent, documentation must define:

- mission and scope;
- input contract;
- output contract;
- tools and skills it may use;
- evidence expectations;
- failure modes;
- escalation conditions;
- prohibited or out-of-scope actions.

A synthesis, reviewer, gatekeeper, or equivalent final-control role must exist where appropriate.

An agent that only returns fields already present in state without transformation, analysis, validation, challenge, or synthesis is considered a placeholder and fails Gold Standard review.

## 5. Orchestration requirements

The orchestrator must explicitly support the workflow appropriate to the domain, including:

- initialization and validation;
- agent sequencing, routing, or parallelism;
- shared state updates;
- tool invocation boundaries;
- retry and failure policy;
- uncertainty and conflict propagation;
- approval gates;
- final synthesis;
- terminal status and reason.

For non-trivial systems, orchestration should expose a deterministic trace that can be inspected during testing.

## 6. State, memory, and provenance

State must distinguish at least:

- raw inputs;
- derived facts;
- assumptions;
- evidence/provenance;
- agent findings;
- unresolved questions;
- risks/blockers;
- approvals;
- final outputs.

Memory must document what is persisted, why, retention scope, and how stale information is handled. Sensitive systems must minimize stored data and avoid retaining unnecessary personal information.

## 7. Tools and skills

Each repository must include domain-relevant tools and skills with typed or otherwise explicit contracts. Tools must include validation and failure handling.

Examples of acceptable tool behavior include calculations, ranking, parsing, simulation, policy checks, data transformations, evidence reconciliation, schema validation, retrieval adapters, or domain-specific scoring.

Examples of unacceptable Gold Standard tools include functions that merely echo input, return hard-coded success, or wrap a dictionary without performing the documented operation.

## 8. Safety and governance

Every repository must include a domain-specific safety model. At minimum it must define:

- allowed scope;
- prohibited scope;
- high-impact actions;
- approval requirements;
- escalation triggers;
- evidence requirements;
- uncertainty handling;
- audit/logging expectations.

Sensitive domains such as healthcare, finance, legal, security, public sector, robotics, and infrastructure require stronger safeguards and tests specific to the domain.

## 9. Testing requirements

A single smoke test is not sufficient. Every repository must include:

- unit tests for agents;
- unit tests for tools;
- orchestration tests;
- schema/state validation tests;
- invalid or missing input tests;
- tool failure tests;
- contradictory evidence tests;
- approval-gate tests where applicable;
- at least one domain-specific adversarial/red-team test;
- one minimal end-to-end test;
- one complete end-to-end scenario.

Tests must validate behavior and state transitions, not only a fixed status string.

## 10. Evaluation and benchmarks

Each repository must define measurable success criteria in `docs/EVALUATION.md` and executable or reproducible evaluations in `evals/` and `benchmarks/`.

Metrics should be domain-specific. Appropriate dimensions may include correctness, completeness, evidence coverage, calibration, constraint satisfaction, consistency, latency, cost, safety violations, escalation accuracy, robustness, or human-review agreement.

Benchmark fixtures must include both normal and failure cases.

## 11. Documentation requirements

Every repository must provide:

- `README.md`: problem, architecture, quick start, examples, limitations, maturity;
- `docs/ARCHITECTURE.md`;
- `docs/AGENTS.md`;
- `docs/EVALUATION.md`;
- `docs/SAFETY.md`;
- `docs/EXTENDING.md`.

Documentation must describe what the implementation actually does. Aspirational capabilities must be labeled as roadmap items, not current functionality.

## 12. Reproducibility and CI

Every repository must document a fresh-clone path and provide CI that verifies the supported Python range. At minimum CI should install the package, run tests, and run a deterministic example or smoke workflow.

A repository cannot be promoted to Gold Standard while required CI is failing.

## 13. Open-source reference quality

Required root artifacts:

- LICENSE;
- CITATION.cff;
- CONTRIBUTING.md;
- SECURITY.md;
- CHANGELOG.md;
- issue templates;
- pull request template.

The README must include the stable F-number and a link back to the Agentic AI Library.

## 14. Maturity levels

Repositories use four maturity levels:

- **L0 Scaffold**: structure or placeholder implementation only.
- **L1 Reference Draft**: runnable core architecture with meaningful agents, but incomplete validation, evaluation, or documentation.
- **L2 Verified Reference**: reproducible tests and CI, substantive tools/agents, documented safety/evaluation, and no known acceptance blockers.
- **L3 Gold Standard**: independently reviewable, benchmarked, adversarially tested, fully documented, reproducible, domain-specific, and suitable for citation as a reference implementation.

No repository may be labeled L3 solely from structure or code volume.

## 15. Gold Standard acceptance gate

A repository reaches L3 only when:

1. every applicable item in `REPOSITORY_ACCEPTANCE_CHECKLIST.md` passes;
2. all mandatory tests pass;
3. CI is green;
4. no placeholder agents/tools remain;
5. documentation matches implementation;
6. benchmark/evaluation results are recorded;
7. safety/red-team tests pass;
8. the canonical catalog records the verified maturity honestly.

## 16. Library-wide objective

The F01-F170 collection will be modernized without flattening domain differences. Rich legacy implementations should be preserved and wrapped with modern quality layers. Thin scaffolds should be deepened with real domain reasoning, real tools, behavioral tests, benchmarks, safety, and documentation.

The standard is not uniform code. The standard is uniform rigor.
