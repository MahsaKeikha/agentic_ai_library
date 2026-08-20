# F41-F50 Evaluation Framework

The Software Engineering batch is evaluated as engineering decision support. It does not autonomously deploy software, change infrastructure, execute destructive operations, or perform unauthorized security testing.

## Common release criteria

- Required inputs are supplied or clearly marked missing.
- Assumptions remain labeled as assumptions.
- Human review is required before deployment, release, destructive change, or security-sensitive action.
- Tests cover registration, evidence discipline, and approval gates.
- Production deployments add authentication, authorization, audit logs, provenance, secrets management, and organization-specific controls.

## System-specific focus

| ID | Evaluation focus |
|---|---|
| F41 | app architecture, UX acceptance criteria, API integration, mobile test coverage, release readiness |
| F42 | resilience, networking, security, cost, capacity, architecture consistency |
| F43 | build reproducibility, deployment safety, rollback, secret handling, CI/CD reliability |
| F44 | policy compliance, workload health, observability, availability, change safety |
| F45 | alert precision, evidence quality, incident severity classification, escalation quality, defensive containment planning |
| F46 | explicit authorization, scope adherence, safe test planning, evidence quality, remediation usefulness |
| F47 | contract correctness, schema validation, authentication/authorization, integration tests, reliability |
| F48 | data model quality, query performance, backup/recovery, security, migration safety |
| F49 | interface correctness, firmware verification, resource constraints, safety testing, hardware/software integration |
| F50 | device identity, connectivity reliability, edge/cloud boundaries, fleet observability, security, update safety |

## Red-team expectations

Test malformed inputs, missing authorization, conflicting requirements, stale state, unsafe release requests, secrets in input, partial dependency failure, attempts to bypass review gates, and untrusted instructions embedded in logs or artifacts.
