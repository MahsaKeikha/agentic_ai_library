# F28 Agentic Startup Accelerator

Multi-agent workflow for moving an early stage idea toward a validated MVP plan. It supports problem framing, market analysis, product validation, growth planning, unit economics, runway analysis, experiment design, fundraising readiness, and human approval before consequential actions.

The system does not guarantee product market fit, funding, or commercial success.

## Visible architecture

The implementation is intentionally exposed through separate folders so readers can inspect actual agents, tools, skills, orchestration, memory, schemas, prompts, configuration, safety gates, observability, evaluations, benchmarks, and tests.

## Agents

- [Venture Intake Agent](AGENTS/venture_intake_agent.py)
- [Market Agent](AGENTS/market_agent.py)
- [Product Agent](AGENTS/product_agent.py)
- [Growth Agent](AGENTS/growth_agent.py)
- [Investor Readiness Agent](AGENTS/investor_readiness_agent.py)

## Tools

- [Market Sizing Tool](TOOLS/market_sizing_tool.py)
- [Experiment Tracker](TOOLS/experiment_tracker.py)
- [Unit Economics Tool](TOOLS/unit_economics_tool.py)
- [Runway Tool](TOOLS/runway_tool.py)
- [Milestone Tool](TOOLS/milestone_tool.py)

## Skills

- [Venture Screening](SKILLS/venture_screening.py)
- [Market Analysis](SKILLS/market_analysis.py)
- [Product Validation](SKILLS/product_validation.py)
- [Growth Planning](SKILLS/growth_planning.py)
- [Investor Readiness](SKILLS/investor_readiness.py)

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
python3 systems/F28_agentic_startup_accelerator/run.py --offline
```
