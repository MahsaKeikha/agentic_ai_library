# F46 Penetration Testing

Authorized defensive assessment planning system with explicit scope control, evidence tracking, control validation, finding triage, reporting, and human review.

This system is designed for authorized security assessment workflows only. It does not provide autonomous exploitation or destructive actions.

## Agents

- [`Scope Agent`](AGENTS/scope_agent.py)
- [`Asset Review Agent`](AGENTS/asset_review_agent.py)
- [`Control Validation Agent`](AGENTS/control_validation_agent.py)
- [`Finding Triage Agent`](AGENTS/finding_triage_agent.py)
- [`Reporting Agent`](AGENTS/reporting_agent.py)

## Tools

- [`Scope Validator`](TOOLS/scope_validator.py)
- [`Evidence Register`](TOOLS/evidence_register.py)
- [`Control Checklist`](TOOLS/control_checklist.py)
- [`Severity Ranker`](TOOLS/severity_ranker.py)
- [`Report Builder`](TOOLS/report_builder.py)

## Skills

- [`Authorization Review`](SKILLS/authorization_review.py)
- [`Asset Analysis`](SKILLS/asset_analysis.py)
- [`Control Assessment`](SKILLS/control_assessment.py)
- [`Finding Prioritization`](SKILLS/finding_prioritization.py)
- [`Report Synthesis`](SKILLS/report_synthesis.py)

## Supporting architecture

- [`Workflow`](orchestration/workflow.py)
- [`Authorization Gate`](safety/authorization_gate.py)
- [`Assessment Context`](schemas/context.py)

## Run

```bash
python launcher.py F46
```

All consequential security actions remain under human authority and written authorization.
