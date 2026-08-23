# Enterprise Agentic AI Readiness Assessment Engine

This package operationalizes the **Agentic AI Gold Standard v1.0** as a deterministic, evidence-first assessment workflow.

It is designed for repeatable consulting delivery today and for later reuse inside a dashboard, API, or Agentic AI Control Plane.

## What the engine produces

Given one JSON assessment input, the engine generates:

- a weighted 0 to 100 readiness score
- a maturity band
- evidence-completeness percentage
- Gold Standard Candidate determination
- production recommendation
- strongest and weakest pillars
- critical production blockers
- P0, P1, P2, and P3 remediation queues
- machine-readable `assessment.json`
- executive Markdown report
- technical Markdown report

## Ten weighted pillars

| Pillar | Weight |
|---|---:|
| Agent specialization and boundaries | 10 |
| Orchestration and workflow control | 12 |
| Deterministic tools and structured state | 10 |
| Memory and context governance | 8 |
| Evaluation and held-out testing | 15 |
| Observability and failure visibility | 10 |
| Safety, security, and privacy | 12 |
| Human authority and protected actions | 10 |
| Provenance, evidence, and auditability | 7 |
| Lifecycle governance and operations | 6 |
| **Total** | **100** |

## Maturity bands

| Score | Band |
|---:|---|
| 0 to 39 | Experimental |
| 40 to 59 | Emerging |
| 60 to 74 | Managed |
| 75 to 89 | Production Candidate |
| 90 to 100 | Gold Standard Candidate, subject to blocker and evidence gates |

A score of 90 or more is **not enough by itself**. Gold Standard Candidate requires:

- score of at least 90
- no unresolved critical blockers
- at least 80% standard evidence completeness

If either gate fails, the engine caps the maturity designation at **Production Candidate**.

## Critical blockers

The engine recognizes explicit blocker types including:

- uncontrolled consequential action
- missing authorization boundary
- critical security exposure
- fabricated or unverifiable evidence
- sensitive-data exposure
- missing fail-closed behavior
- unbounded external side effect
- missing incident or rollback path

Any open P0 finding is also treated as a production blocker.

## Evidence completeness

The standard evidence package contains ten categories:

1. architecture
2. agent inventory
3. tool inventory
4. permission map
5. memory policy
6. evaluation results
7. observability traces
8. security review
9. protected-action map
10. incident and rollback evidence

The engine reports how many of these categories are represented. Presence does not mean quality is sufficient. Reviewers still need to inspect the evidence.

## Input format

See `sample_input.json` for the complete schema pattern.

Pillar scores are entered from 0 to 100. Each score should be backed by assessment evidence and reviewer rationale rather than intuition alone.

Findings include:

```json
{
  "id": "P0-1",
  "pillar": "human_authority",
  "title": "Consequential action lacks authorization boundary",
  "evidence": "Observed architecture evidence",
  "risk": "Why the finding matters",
  "recommendation": "Required remediation",
  "priority": "P0",
  "blocker_type": "missing_authorization_boundary"
}
```

## Running the engine

From the repository root:

```bash
python -m assessment_engine.engine assessment_engine/sample_input.json --output assessment_output
```

The command creates:

```text
assessment_output/
├── assessment.json
├── executive_report.md
└── technical_report.md
```

## Commercial delivery workflow

A paid assessment can follow this sequence:

1. discovery and scope
2. evidence request
3. architecture and authority mapping
4. reviewer scoring across the ten pillars
5. finding creation with evidence and risk rationale
6. deterministic engine run
7. P0 blocker verification
8. internal quality review
9. executive report delivery
10. technical findings review
11. remediation planning
12. optional reassessment after P0 and P1 closure

## Reviewer discipline

The engine should not manufacture confidence. Reviewers should:

- distinguish missing evidence from negative evidence
- preserve source provenance
- record assumptions
- avoid scoring a control as mature merely because it is documented
- test consequential authority boundaries where authorized
- distinguish model behavior from deterministic system controls
- treat self-attestation as weaker evidence than reproducible tests or system traces
- disclose assessment limitations

## CI

`test_engine.py` is automatically discovered by the repository's existing pytest workflow on Python 3.10, 3.11, and 3.12.

Tests verify scoring, blocker behavior, Gold Standard gating, evidence gating, validation, report generation, and delivery artifact creation.

## Scope and limitations

This is an engineering maturity framework. It is not a regulatory certification, audit opinion, penetration test, legal opinion, medical determination, financial assurance engagement, or guarantee that a system is safe.

Domain-specific compliance, security, privacy, legal, clinical, financial, and regulatory obligations require appropriate qualified review.

## Intellectual property and positioning

The engine is the operational layer behind the Agentic AI Gold Standard and Enterprise Readiness Assessment. The open implementation demonstrates the methodology and supports reproducibility. Commercial value can be created through evidence collection, expert review, architecture analysis, remediation design, enterprise implementation, reassessment, training, advisory, and future tooling around the framework.

**Created by Mahsa Keikha.**