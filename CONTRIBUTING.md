# Contributing to the Agentic AI Library

Thank you for helping improve this reference library for agentic AI and multi-agent systems.

## What belongs here

Contributions should strengthen one or more of the following:

- multi-agent architecture and orchestration
- agent roles, tools, state, and memory
- evaluation and held-out scenarios
- observability and provenance
- safety and security boundaries
- human approval gates
- documentation and reproducibility
- domain-specific reference implementations
- tests, reliability, and developer experience

## Before opening a pull request

1. Search existing repositories and issues to avoid duplication.
2. Keep the scope focused and explain the engineering problem being solved.
3. Preserve existing public links and identifiers unless a migration is intentional and documented.
4. Add or update tests when behavior changes.
5. Do not remove safety, authorization, provenance, or observability controls merely to simplify an example.
6. Never include secrets, private credentials, personal data, proprietary datasets, or confidential material.

## Reference architecture expectations

Where applicable, agentic systems should make these elements explicit:

- specialized agents with clear responsibilities
- orchestration and state transitions
- deterministic tools or bounded interfaces
- evidence and provenance
- memory or state boundaries
- observability
- evaluations and failure cases
- explicit human authority for consequential actions
- fail-closed behavior when required review is missing

## Pull request quality

A strong pull request includes:

- a concise problem statement
- summary of the proposed change
- affected systems or IDs
- tests or evaluation evidence
- safety and security impact
- screenshots or output examples when useful
- migration notes for breaking changes

## Style

Use clear engineering language. Prefer explicit assumptions and failure states over vague claims such as "safe," "autonomous," or "production ready" without evidence.

Keep Markdown readable, links direct, and examples reproducible.

## Safety-sensitive contributions

Changes involving healthcare, finance, legal workflows, robotics, public-sector decisions, security, employment, elections, or other consequential domains should preserve qualified human review and domain-appropriate authority boundaries.

## Security reports

Do not use a public pull request or issue to disclose an unpatched vulnerability. Follow `SECURITY.md`.

## Code of conduct

Participation in this project requires adherence to `CODE_OF_CONDUCT.md`.

## Attribution

By contributing, you agree that your contribution may be distributed under the repository's applicable license and that you have the right to submit the material.
