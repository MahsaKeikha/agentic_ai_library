# F29 Agentic Innovation Officer

Multi-agent workflow for enterprise innovation portfolio management. It supports opportunity discovery, portfolio prioritization, experiment design, adoption planning, innovation governance, and explicit human approval before consequential actions.

The system supports structured decision making. It does not autonomously approve investments, procurement, partnerships, budget commitments, or public commitments.

## Visible architecture

The implementation is intentionally exposed through separate folders so readers can inspect actual agents, tools, skills, orchestration, memory, schemas, prompts, configuration, safety gates, observability, evaluations, benchmarks, and tests.

## Agents

- [Opportunity Agent](AGENTS/opportunity_agent.py)
- [Portfolio Agent](AGENTS/portfolio_agent.py)
- [Experiment Agent](AGENTS/experiment_agent.py)
- [Adoption Agent](AGENTS/adoption_agent.py)
- [Governance Agent](AGENTS/governance_agent.py)

## Tools

- [Opportunity Score Tool](TOOLS/opportunity_score_tool.py)
- [Portfolio Tool](TOOLS/portfolio_tool.py)
- [Experiment Registry](TOOLS/experiment_registry.py)
- [Adoption Tracker](TOOLS/adoption_tracker.py)
- [Risk Register Tool](TOOLS/risk_register_tool.py)

## Skills

- [Opportunity Discovery](SKILLS/opportunity_discovery.py)
- [Portfolio Prioritization](SKILLS/portfolio_prioritization.py)
- [Experiment Design](SKILLS/experiment_design.py)
- [Adoption Planning](SKILLS/adoption_planning.py)
- [Innovation Governance](SKILLS/innovation_governance.py)

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
python3 systems/F29_agentic_innovation_officer/run.py --offline
```
