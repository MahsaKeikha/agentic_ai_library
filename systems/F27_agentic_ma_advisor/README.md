# F27 Agentic M&A Advisor

Multi-agent decision support workflow for acquisition screening, diligence, valuation analysis, risk review, and integration planning. It supports structured evidence handling and preserves human authority for consequential decisions.

Not legal, tax, accounting, valuation, or investment advice. No autonomous transaction, offer, commitment, filing, or external submission.

## Visible architecture

The implementation is intentionally exposed through separate folders so readers can inspect actual agents, tools, skills, orchestration, memory, schemas, prompts, configuration, safety gates, observability, evaluations, benchmarks, and tests.

## Agents

- [Deal Intake Agent](AGENTS/deal_intake_agent.py)
- [Due Diligence Agent](AGENTS/due_diligence_agent.py)
- [Valuation Agent](AGENTS/valuation_agent.py)
- [Risk Agent](AGENTS/risk_agent.py)
- [Integration Agent](AGENTS/integration_agent.py)

## Tools

- [Financial Model Tool](TOOLS/financial_model_tool.py)
- [Comparable Company Tool](TOOLS/comparable_company_tool.py)
- [Diligence Checklist Tool](TOOLS/diligence_checklist_tool.py)
- [Risk Register Tool](TOOLS/risk_register_tool.py)
- [Synergy Tool](TOOLS/synergy_tool.py)

## Skills

- [Deal Screening](SKILLS/deal_screening.py)
- [Valuation Reasoning](SKILLS/valuation_reasoning.py)
- [Diligence Planning](SKILLS/diligence_planning.py)
- [Risk Assessment](SKILLS/risk_assessment.py)
- [Integration Planning](SKILLS/integration_planning.py)

## Supporting layers

- [Orchestration](orchestration/workflow.py)
- [Memory](memory/store.py)
- [Schemas](schemas/models.py)
- [Prompts](prompts/system_prompt.md)
- [Configuration](config/defaults.json)
- [Safety Gates](safety/gates.py)
- [Observability](observability/tracing.py)
- [Evaluation](evals/evaluator.py)
- [Benchmarks](benchmarks/README.md)
- [Architecture](docs/ARCHITECTURE.md)
- [Architecture Test](tests/test_visible_architecture.py)

## Quick start

```bash
python3 systems/F27_agentic_ma_advisor/run.py --offline
```
