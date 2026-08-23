# Agentic AI Enterprise Readiness Assessment

## Purpose

This assessment converts the Agentic AI Gold Standard into a practical enterprise review for organizations designing, piloting, or operating agentic and multi-agent AI systems.

It is intended to answer one question:

**Is this agentic system ready to move from experimentation toward responsible organizational use?**

The assessment is a decision-support framework, not a regulatory certification, legal opinion, audit opinion, or guarantee of safety.

## Assessment dimensions

Score each dimension from 0 to 5 using documented evidence.

| Dimension | Weight | Core question |
|---|---:|---|
| Architecture and agent roles | 10% | Are roles, inputs, outputs, dependencies, and boundaries explicit? |
| Orchestration and workflow control | 10% | Is coordination inspectable, deterministic where needed, and recoverable? |
| Tool authority and protected actions | 15% | Can the system clearly distinguish allowed actions from human-only authority? |
| Safety, security, and privacy | 15% | Are prompt injection, secrets, permissions, data leakage, and misuse addressed? |
| Evaluation and robustness | 15% | Are happy paths, failures, adversarial cases, and held-out scenarios tested? |
| Observability and provenance | 10% | Can important decisions, tools, evidence, and approvals be reconstructed? |
| Human oversight and escalation | 10% | Are consequential actions reviewed by accountable people? |
| Data and memory governance | 5% | Are state, memory, retention, corrections, and sensitive data bounded? |
| Reliability and lifecycle controls | 5% | Are retries, rollback, incidents, continuity, and release gates addressed? |
| Governance and organizational ownership | 5% | Are owners, reviewers, accountability, and policy boundaries explicit? |

Total: 100%

## Scoring scale

### 0 - Absent
No meaningful evidence exists.

### 1 - Ad hoc
The capability exists informally or only in prompts, individual knowledge, or undocumented practice.

### 2 - Emerging
Some controls exist but are incomplete, inconsistent, or weakly tested.

### 3 - Defined
The capability is documented and generally repeatable.

### 4 - Governed
The capability is enforced through code, process, review, evidence, and measurable controls.

### 5 - Gold Standard
The capability is explicit, tested, observable, fail-closed where necessary, and integrated into lifecycle governance.

## Readiness bands

### 0-39: Experimental
Suitable primarily for exploration, research, or contained internal experimentation.

### 40-59: Structured Pilot
The system may support limited pilots if scope and permissions remain narrow and accountable humans retain control.

### 60-74: Governed Pilot
The system demonstrates meaningful governance but still has material gaps before broad production use.

### 75-89: Production Candidate
The system has strong engineering and governance maturity. Organization-specific security, legal, operational, and regulatory approval is still required.

### 90-100: Gold Standard Candidate
The system demonstrates mature agentic engineering controls and may be considered for Gold Standard review, subject to evidence validation and organization-specific deployment governance.

## Automatic blockers

Regardless of numeric score, the system should not be classified as production ready when any of the following remain unresolved:

- agents can move money or execute material transactions without authorized controls
- agents can sign or create binding legal commitments without authorization
- agents can deploy or modify production systems without appropriate release controls
- agents can suppress incidents, defects, safety findings, or required reporting
- high-risk tools operate with broad credentials or excessive privileges
- sensitive data is exposed without an approved privacy basis
- consequential decisions have no accountable human owner
- the system cannot reconstruct material decisions or tool actions
- known critical security or safety defects remain open
- required regulatory, legal, or compliance review is missing

## Assessment evidence request

A professional assessment should request, where applicable:

- architecture diagrams
- agent inventory and responsibilities
- orchestrator or workflow definition
- tool inventory and permissions
- prompts and policies relevant to authority
- memory/state design
- logs and traces
- test suites and evaluation results
- held-out scenarios
- incident history
- release workflow
- access-control model
- threat model
- privacy/data classification
- human approval workflow
- escalation matrix
- regulatory or compliance constraints
- known limitations and unresolved risks

## Deliverable structure

A commercial assessment report can contain:

1. Executive summary
2. Overall readiness score
3. Readiness band
4. Critical blockers
5. Dimension-by-dimension scoring
6. Architecture findings
7. Safety and security findings
8. Evaluation gaps
9. Governance and authority gaps
10. Prioritized remediation roadmap
11. 30-day actions
12. 90-day actions
13. Gold Standard gap analysis
14. Appendix with evidence references

## Example executive output

```text
Agentic AI Enterprise Readiness Score: 72 / 100
Band: Governed Pilot

Critical blockers: 2
High-priority findings: 5
Medium-priority findings: 8

Strongest areas:
- agent-role decomposition
- observability
- workflow orchestration

Highest-risk gaps:
- excessive tool permissions
- no independent held-out governance evaluation
- incomplete protected-action model

Recommendation:
Do not expand production scope until critical blockers are closed.
```

## Remediation priority model

### P0 Critical
Immediate risk of material harm, unauthorized authority, security compromise, or regulatory failure.

### P1 High
Blocks broader production use or materially weakens governance.

### P2 Medium
Important maturity or resilience gap that should enter the engineering roadmap.

### P3 Improvement
Enhances clarity, maintainability, efficiency, or long-term maturity.

## Commercial use

The framework can support:

- pre-production agentic AI reviews
- multi-agent architecture assessments
- governance readiness reviews
- AI startup diligence
- enterprise design-partner engagements
- regulated-industry AI reviews
- post-incident remediation planning
- procurement and vendor assessment
- internal audit preparation
- board and executive briefings

## Boundary

This framework assesses engineering and governance maturity. It does not replace qualified legal, compliance, cybersecurity, privacy, clinical, financial, regulatory, or domain-specific review.

## Maintainer

Mahsa Keikha

Agentic AI Library
