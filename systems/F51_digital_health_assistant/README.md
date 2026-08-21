# F51 Agentic Digital Health Assistant

A non-diagnostic multi-agent digital health workflow assistant.

## Agents
- [Intake Coordinator](AGENTS/intake_coordinator.py)
- [Data Quality Agent](AGENTS/data_quality_agent.py)
- [Care Plan Organizer](AGENTS/care_plan_organizer.py)
- [Education Agent](AGENTS/education_agent.py)
- [Risk Escalation Agent](AGENTS/risk_escalation_agent.py)
- [Human Gatekeeper](AGENTS/human_gatekeeper.py)

## Core layers
- [Tools](TOOLS/)
- [Skills](SKILLS/)
- [Orchestration](orchestration/)
- [Memory](memory/store.py)
- [State](state/run_state.py)
- [Schemas](schemas/contracts.py)
- [Prompts](prompts/system_prompts.py)
- [Config](config/settings.py)
- [Safety](safety/clinical_gate.py)
- [Observability](observability/tracing.py)
- [Evals](evals/evaluator.py)
- [Benchmarks](benchmarks/benchmark.py)
- [Examples](examples/example_run.py)
- [Tests](tests/test_structure.py)
- [Architecture](docs/ARCHITECTURE.md)

Patient-specific outputs require qualified human review.
