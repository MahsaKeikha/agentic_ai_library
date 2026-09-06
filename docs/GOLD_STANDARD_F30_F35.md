# Gold Standard Reference Cohort: F30-F35

F30-F35 are the validation cohort for the standalone Agentic AI Library architecture. No mass migration to F36-F170 should be treated as complete until this cohort demonstrates the quality bar expected of a globally useful reference collection.

## Cohort

| ID | System | Reference emphasis |
|---|---|---|
| F30 | Agentic Corporate Governance | evidence-aware governance, board process, decision traceability, human authority |
| F31 | Agentic ML Engineer | data/model lifecycle, reproducibility, evaluation, deployment handoff |
| F32 | Agentic MLOps Team | model delivery, observability, rollback, release gates, operational state |
| F33 | Agentic Data Engineering | contracts, lineage, quality, orchestration, reliability |
| F34 | Agentic Prompt Engineering | prompt lifecycle, evaluation sets, regression testing, injection resistance |
| F35 | Agentic RAG Engineering | ingestion, retrieval, grounding, citation, evaluation, failure analysis |

## Required architecture for every cohort repository

Each repository must be independently runnable and include:

1. A domain-specific multi-agent team with meaningful responsibility boundaries.
2. An orchestrator with explicit workflow transitions rather than an unstructured conversation loop.
3. Typed shared state and traceable artifacts.
4. Evidence/provenance records and explicit unknowns.
5. Conflict and failure handling.
6. Human approval gates for consequential actions.
7. Deterministic offline reference execution.
8. Optional provider/tool adapters behind stable interfaces.
9. Unit, integration, gate, and adversarial tests.
10. A domain evaluation rubric and reproducible example cases.
11. Architecture and sequence documentation.
12. SECURITY.md, CONTRIBUTING.md, CITATION.cff, CHANGELOG.md, LICENSE, and version metadata.
13. GitHub Actions across supported Python versions.
14. Clear maturity labeling: Reference, Integrated, Validated, or Production-ready.
15. No claim of production readiness without operational evidence.

## Common interface

All F-series standalone repositories should converge on a recognizable interface:

```python
result = run_system(case, approve=False)
```

The result should expose at minimum:

- system identity and version
- run/correlation identifier
- agent outputs
- evidence and provenance
- unresolved questions
- conflicts
- risks and blockers
- recommendation
- approval/gate state
- execution trace

Consistency is intentional: it allows researchers and engineers to compare architectures across domains while preserving domain-specific agent behavior.

## Reference-quality documentation

Every README should answer, without marketing inflation:

- What problem does this system solve?
- Why is a multi-agent architecture justified?
- What does each agent own?
- How does information move through the system?
- What state is shared?
- What can block progression?
- What does the human approve?
- How is the system evaluated?
- What are known limitations?
- How can a researcher reproduce the examples?
- How can a contributor extend the system safely?

## F30 domain bar

Corporate Governance must demonstrate a traceable path from intake to board-process preparation, policy/register review, decision record, risk review, action tracking, and briefing. It must never imply that an AI agent itself exercises fiduciary authority or legally binds a corporation.

## F31 domain bar

ML Engineer must separate data assessment, feature/model design, training strategy, evaluation, reproducibility, model-card evidence, and deployment handoff. Benchmark results must retain dataset/evaluation context and uncertainty.

## F32 domain bar

MLOps must model build, registry, release, deployment, observability, incident response, rollback, and change approval as explicit operational states. A release gate must be independently testable.

## F33 domain bar

Data Engineering must make schemas/contracts, lineage, data quality, transformations, orchestration, reliability, and downstream impact first-class artifacts. Missing lineage or failed quality gates must be visible.

## F34 domain bar

Prompt Engineering must treat prompts as versioned engineering artifacts. It must include evaluation datasets, regression criteria, injection/adversarial cases, structured-output checks, and model/config provenance.

## F35 domain bar

RAG Engineering must distinguish ingestion, chunking/indexing, retrieval, reranking, context assembly, generation, citation, and evaluation. It must measure retrieval and answer quality separately and expose insufficient-grounding cases rather than fabricating certainty.

## Acceptance gate before F36-F170 scale-out

The cohort passes only when all six repositories:

- exist as real standalone repositories;
- run without the umbrella repository;
- pass CI;
- pass their domain-specific acceptance tests;
- contain reproducible examples;
- expose their architecture and limitations clearly;
- use the common result contract;
- contain no broken links or placeholder claims;
- have an explicit release version;
- can be cited independently.

Only then should the same architecture be propagated to F36-F170, with domain-specific specialization rather than blind template cloning.
