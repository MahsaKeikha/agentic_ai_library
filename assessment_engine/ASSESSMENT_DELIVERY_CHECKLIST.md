# Enterprise Readiness Assessment Delivery Checklist

Use this checklist for every paid or formal Agentic AI Readiness Assessment.

## 1. Commercial and scope gate

- signed scope or written engagement authorization
- system boundary defined
- organization and system owner identified
- assessment objectives documented
- confidentiality channel established
- excluded systems and assumptions documented
- no promise of regulatory certification

## 2. Evidence request

Request only what is necessary and use an approved private channel for sensitive material.

Core evidence:

- current architecture diagram
- agent inventory and responsibilities
- orchestration or workflow definition
- tool/API inventory
- permission and credential model
- protected-action inventory
- human approval design
- memory/context design
- retention and deletion policy
- evaluation suites and results
- adversarial test results
- observability traces
- incident history where disclosable
- rollback and kill-switch procedures
- security/threat-model evidence
- production release process
- ownership and escalation matrix

## 3. Interview set

Recommended stakeholders:

- engineering lead
- AI/ML lead
- product owner
- security representative
- risk/compliance/legal representative where relevant
- operations/SRE owner
- domain expert for consequential workflows
- executive sponsor for decision-right questions

## 4. Architecture review

Document:

- entry points
- agent roles
- handoffs
- shared state
- memory
- tool permissions
- external side effects
- protected actions
- approvals
- retries
- failure paths
- escalation
- rollback

## 5. Ten-pillar scoring

For each pillar, record:

- score from 0 to 100
- evidence reviewed
- evidence quality
- reviewer rationale
- open assumptions
- relevant findings

Do not award maturity solely because a policy exists on paper. Prefer executable controls, reproducible tests, system traces, and attributable approvals.

## 6. Critical-blocker review

Explicitly test for:

- uncontrolled consequential actions
- missing authorization boundaries
- critical security exposure
- fabricated or unverifiable evidence
- sensitive-data exposure
- fail-open behavior
- unbounded external side effects
- absent incident or rollback paths

Any open P0 finding blocks a production-ready recommendation.

## 7. Finding quality gate

Every material finding must contain:

- stable finding ID
- Gold Standard pillar
- evidence
- risk statement
- recommendation
- priority
- blocker type if applicable
- closure criteria

Avoid vague findings such as `security should be improved`.

## 8. Engine run

Prepare the JSON assessment input and run:

```bash
python -m assessment_engine.engine client_input.json --output client_output
```

Verify:

- pillar weights total 100
- score matches reviewer worksheet
- blockers are represented correctly
- evidence completeness is accurate
- maturity gate behaves as expected
- report text does not overstate certainty

## 9. Internal quality review

Before client delivery:

- second-person review of P0 findings
- verify calculations
- verify source attribution
- remove unsupported claims
- remove accidental secrets or sensitive raw data
- verify recommendations are within scope
- verify limitations
- ensure executive and technical reports agree

## 10. Client delivery package

Recommended package:

```text
01_Executive_Readiness_Report.pdf
02_Technical_Findings_Report.pdf
03_Readiness_Scorecard.xlsx or CSV
04_Architecture_Authority_Map.pdf
05_P0-P3_Remediation_Roadmap.pdf
06_Evidence_Register.xlsx or CSV
07_Assessment_Limitations.md
```

The open-source engine currently produces Markdown and JSON. Commercial formatting can render the reviewed content into branded PDF, document, and spreadsheet deliverables.

## 11. Executive readout

Cover:

- score and maturity
- what the score does and does not mean
- production recommendation
- P0 blockers
- strongest controls
- largest maturity gaps
- authority model
- 30/60/90-day remediation
- decisions required from leadership

## 12. Technical readout

Cover:

- pillar-by-pillar evidence
- architecture findings
- tool and permission findings
- memory findings
- evaluation gaps
- observability gaps
- security/privacy findings
- protected-action boundaries
- provenance gaps
- lifecycle/incident controls
- closure evidence required

## 13. Reassessment

A finding is not closed because a client says it is fixed.

Request applicable closure evidence such as:

- code or configuration changes
- policy-gate evidence
- test results
- traces
- approval records
- adversarial results
- incident drills
- rollback evidence

Then rerun the engine with updated evidence and findings.

## 14. Case-study permission

Never publish a client name, architecture, score, quotation, outcome, or logo without appropriate permission.

For anonymous case studies, remove identifying technical details and obtain agreement on the description where required.

## 15. Assessment integrity principles

- evidence before confidence
- blockers before averages
- human authority before autonomy expansion
- reproducibility before marketing claims
- uncertainty should remain visible
- domain-specific obligations remain domain-specific
- no fabricated customer outcomes

**Agentic AI Gold Standard and Enterprise Readiness Assessment framework by Mahsa Keikha.**