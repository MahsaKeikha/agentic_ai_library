# Release and Change Evidence Policy

## Purpose

The Multi-Agent AI Atlas evolves across a central catalog, standalone repositories, public simulations, documentation, and the field guide. Release records should make it possible to identify what changed, what evidence was rerun, and which claims remain valid.

## Release evidence

A material release should record:

- version or dated release identifier
- source commit
- affected systems and public pages
- behavior, architecture, or policy changes
- tests and evaluations completed
- known limitations and unresolved findings
- migration notes when interfaces or expected behavior change
- rollback or correction path when relevant

## Change categories

### Editorial

Language, navigation, accessibility, citations, or visual presentation changes that do not alter system behavior.

### Engineering

Agent roles, orchestration, tools, schemas, state, memory, evaluation, observability, or runtime changes.

### Governance

Authority boundaries, safety controls, permissions, escalation, privacy, security, evidence requirements, or maturity criteria.

### Evidence

New or revised benchmarks, independent reviews, adoption records, case studies, security findings, or correction records.

## Maturity impact

A material change to a verified system may require evaluation to be rerun before the prior maturity claim can be carried forward. Maturity may be suspended when evidence no longer matches the implementation.

## Publication discipline

- Do not describe an unreleased change as publicly available.
- Do not carry forward a benchmark result when the tested behavior materially changed without review.
- Do not remove a material limitation merely because a new release is published.
- Preserve repository history and correction records.
- Keep confidential implementation methods and client information outside public release artifacts.
