# Sample Agentic AI Enterprise Readiness Report

> **Illustrative example only.** The organization, system, evidence, findings, and scores below are fictional. This sample demonstrates the structure of a commercial deliverable and must not be represented as a real customer engagement.

## Executive summary

**Organization:** ExampleCo  
**System:** Customer Operations Multi-Agent Platform  
**Assessment stage:** Pre-production  
**Overall score:** 68 / 100  
**Readiness:** Managed  
**Production recommendation:** Conditional, with P0 blockers requiring remediation before consequential autonomous execution

ExampleCo has developed a capable multi-agent customer-operations platform with clear task specialization, useful orchestration, structured tool interfaces, and an emerging evaluation program. The architecture is promising, but production authority currently exceeds the maturity of its governance controls.

The most significant issues are insufficiently explicit protected-action boundaries, incomplete tool authorization, limited adversarial evaluation, weak provenance for externally sourced evidence, and incomplete incident and rollback procedures.

The system can continue controlled development and supervised pilots. It should not receive unrestricted authority to issue refunds, modify customer accounts, make contractual commitments, or send high-impact external communications until the P0 findings are resolved and verified.

## Readiness scorecard

| Dimension | Weight | Score | Status |
|---|---:|---:|---|
| Agent specialization and boundaries | 10 | 8 | Strong |
| Orchestration and workflow control | 12 | 9 | Managed |
| Deterministic tools and structured state | 10 | 7 | Managed |
| Memory and context governance | 8 | 5 | Emerging |
| Evaluation and held-out testing | 15 | 9 | Managed |
| Observability and failure visibility | 10 | 7 | Managed |
| Safety, security, and privacy | 12 | 7 | Emerging |
| Human authority and protected actions | 10 | 5 | Blocker |
| Provenance, evidence, and auditability | 7 | 5 | Managed |
| Lifecycle governance and operations | 6 | 6 | Strong |
| **Total** | **100** | **68** | **Managed** |

## Architecture overview

The assessed system contains five specialized agents:

- Intake Agent
- Customer Context Agent
- Resolution Agent
- Policy Review Agent
- Communication Agent

The agents share a workflow orchestrator and access customer records, policy retrieval, ticket management, refund tooling, and outbound communication interfaces.

The primary architectural strength is explicit functional decomposition. The primary architectural weakness is that several consequential tools are available through the same orchestration path as low-risk analytical tools.

## Key strengths

### 1. Agent responsibilities are mostly explicit

The system separates intake, context gathering, resolution reasoning, policy review, and communication rather than relying on one unconstrained agent.

### 2. Tool calls use structured interfaces

Core integrations use typed parameters and deterministic validation rather than free-form text execution.

### 3. The team has begun held-out evaluation

A repeatable evaluation set exists for common support scenarios and several known edge cases.

### 4. Logs support basic trace reconstruction

Agent outputs and tool calls can be reconstructed for many workflows, creating a foundation for stronger observability.

## P0 critical blockers

### P0-1: Consequential financial actions lack a hard authorization boundary

**Finding:** The Resolution Agent can reach the refund tool after policy review, but approval is represented primarily as workflow state rather than an independent authorization control.

**Risk:** Prompt manipulation, policy misunderstanding, state corruption, or orchestration error could result in unauthorized financial action.

**Required remediation:**

- classify refunds as protected actions
- establish explicit amount and policy thresholds
- require deterministic authorization checks
- require human approval above defined limits
- log approval identity, decision, amount, evidence, and resulting action
- test bypass attempts and fail-closed behavior

### P0-2: External communications can be sent without sufficient preview and approval controls

**Finding:** The Communication Agent can send certain customer messages automatically.

**Risk:** Incorrect, legally sensitive, privacy-sensitive, or reputationally damaging communications could leave the system before appropriate review.

**Required remediation:**

- classify high-impact communication categories
- separate draft generation from send authority
- add preview and approval gates for defined categories
- create deterministic restrictions for prohibited disclosures and commitments
- retain final-message provenance

## P1 production-readiness gaps

### P1-1: Adversarial evaluation is incomplete

Add scenarios for prompt injection, conflicting policy sources, corrupted customer context, stale retrieval, malformed tool results, retry duplication, privilege escalation, and agent disagreement.

### P1-2: Memory retention rules are insufficiently explicit

Define what can enter memory, retention periods, deletion behavior, sensitive-data restrictions, and whether user corrections override stale memory.

### P1-3: Provenance is incomplete for retrieved policy evidence

Each material policy claim should retain source, version or effective date where available, retrieval time, and transformation history.

### P1-4: Incident response is not agent-specific

Add procedures for tool misuse, incorrect external action, memory contamination, evaluation regression, prompt injection, and compromised credentials.

## P2 maturity improvements

- formalize agent-to-agent handoff schemas
- add trace correlation IDs across all agent and tool events
- establish release evaluation thresholds
- track recurring failure categories
- create production shadow-mode testing
- add cost and latency budgets by workflow

## Protected-action map

| Action | Current authority | Recommended authority |
|---|---|---|
| Retrieve customer record | Automated | Automated with least privilege |
| Draft response | Automated | Automated |
| Send routine informational response | Automated | Automated after deterministic policy checks |
| Send legal/contractual commitment | Automated in some paths | Human approval required |
| Refund below defined low-risk threshold | Automated | Conditional deterministic authorization |
| Refund above threshold | Automated in some paths | Human approval required |
| Delete customer data | Not exposed | Keep outside autonomous authority |
| Change account ownership/security | Not exposed | Keep outside autonomous authority |

## Evaluation recommendations

The next evaluation suite should include:

1. ordinary successful workflow
2. missing customer evidence
3. conflicting policies
4. stale policy source
5. prompt injection in customer content
6. malformed tool output
7. refund threshold boundary
8. unauthorized refund request
9. communication containing prohibited commitment
10. duplicate retry and idempotency test
11. agent disagreement
12. unavailable approval service
13. corrupted memory
14. privacy-sensitive data request
15. rollback after incorrect external action

## 30-day remediation roadmap

### Week 1

- define protected actions and authority matrix
- isolate financial and communication authorization
- document memory policy

### Week 2

- implement deterministic approval gates
- add provenance fields
- add correlation IDs and structured failure logging

### Week 3

- expand held-out and adversarial evaluations
- add fail-closed tests
- test retry, duplication, and degraded dependencies

### Week 4

- run regression suite
- verify P0 closure
- conduct supervised production-readiness review
- document residual risk and launch conditions

## Final recommendation

ExampleCo's platform demonstrates meaningful engineering maturity but should remain in supervised pre-production until the two P0 blockers are remediated and independently verified.

A successful reassessment would require evidence that protected financial and external communication actions cannot execute outside the approved authority model, including adversarial and failure-path tests.

## Gold Standard gap

At 68 / 100, the system is currently **Managed**. Reaching **Gold Standard Candidate** would require a score of at least 90, no critical blockers, complete required evidence, and stronger maturity in memory governance, adversarial evaluation, safety/security, human authority, and provenance.

---

**Illustrative report prepared using the Agentic AI Gold Standard v1.0 and Enterprise Readiness Assessment framework by Mahsa Keikha.**