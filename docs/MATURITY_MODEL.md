# Agentic AI Library Maturity Model

This maturity model is the canonical interpretation of repository quality for F01-F170.

## L0 Scaffold

A repository is L0 when it primarily demonstrates structure rather than validated behavior.

Typical indicators:

- placeholder or pass-through agents;
- shallow tools;
- hard-coded status values;
- smoke-only tests;
- minimal README;
- no adversarial/safety evaluation;
- missing governance artifacts;
- claims that exceed implementation.

L0 repositories are useful as starting points but must not be presented as verified reference systems.

## L1 Reference Draft

A repository is L1 when its core workflow is genuinely implemented and runnable, but important quality layers are incomplete.

Required characteristics:

- four or more meaningfully distinct agents;
- explicit orchestration;
- shared state;
- real domain logic in agents and/or tools;
- runnable example;
- basic unit and integration tests;
- documented limitations;
- no misleading production claims.

Common remaining gaps may include incomplete safety testing, limited benchmarks, missing CI coverage, incomplete provenance, or incomplete open-source documentation.

## L2 Verified Reference

A repository is L2 when it is reproducible and independently verifiable as an engineering reference.

Required characteristics:

- fresh-clone install/run instructions verified;
- deterministic core workflow;
- meaningful agent and tool implementations;
- structured state and contracts;
- failure handling and retries where appropriate;
- evidence/provenance discipline;
- safety boundaries and approval gates;
- unit, integration, failure, and safety tests;
- CI green on supported Python versions;
- documented evaluation methodology;
- benchmark fixtures and recorded results;
- complete required docs;
- required open-source governance files.

L2 is the minimum level for a repository to be described as verified.

## L3 Gold Standard

L3 is reserved for repositories that can serve as exemplary public reference implementations.

In addition to all L2 requirements, L3 requires:

- substantive domain-specific reasoning rather than generic templates;
- at least one realistic complete scenario and multiple challenging scenarios;
- adversarial/red-team test coverage appropriate to domain risk;
- robust evidence conflict and uncertainty handling;
- explicit observability and trace inspection;
- benchmark results that are reproducible and interpreted honestly;
- clear extension architecture;
- no known placeholder implementation in the critical path;
- documentation that can teach an engineer how and why the system works;
- independent-review readiness;
- stable citation/version metadata.

## Promotion rules

Promotion is evidence-based. Repository age, code volume, number of folders, and number of agents do not independently determine maturity.

- L0 -> L1 requires substantive runnable behavior.
- L1 -> L2 requires reproducibility, testing, CI, safety, evaluation, and documentation.
- L2 -> L3 requires depth, robustness, benchmark evidence, adversarial validation, observability, and reference-quality teaching value.

A regression in tests, reproducibility, safety, or documentation may lower maturity until corrected.

## Domain-specific rigor

The same maturity label applies across domains, but evidence required to earn it differs. High-impact domains require stricter validation.

Healthcare repositories must emphasize decision-support boundaries, uncertainty, clinical escalation, provenance, and non-diagnostic behavior where applicable. Finance repositories must emphasize assumptions, sensitivity, suitability/authorization boundaries, and auditability. Legal/compliance repositories must preserve jurisdiction, source authority, uncertainty, and qualified-review boundaries. Security repositories must constrain scope and authorization. Robotics/infrastructure repositories must model physical safety and fail-safe behavior. Public-sector repositories must emphasize source provenance, neutrality, privacy, and human authority.

## Catalog representation

The master catalog should eventually record the maturity level of every F01-F170 repository. Until a repository has passed the applicable acceptance gates, it should remain L0 or L1 rather than being described as Gold Standard.
