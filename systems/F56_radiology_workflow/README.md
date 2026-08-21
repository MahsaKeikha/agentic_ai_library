# F56 Agentic Radiology Workflow

## Agents
- [Worklist Coordinator](AGENTS/worklist_coordinator.py)
- [Metadata Validator](AGENTS/metadata_validator.py)
- [Prior Study Locator](AGENTS/prior_study_locator.py)
- [Reporting Completeness Agent](AGENTS/reporting_completeness_agent.py)
- [Safety Escalation Agent](AGENTS/safety_escalation_agent.py)
- [Human Reviewer](AGENTS/human_reviewer.py)

## Core layers
- [Tools](TOOLS/)
- [Skills](SKILLS/)
- [Orchestration](orchestration/)
- [Memory](memory/store.py)
- [State](state/run_state.py)
- [Schemas](schemas/contracts.py)
- [Prompts](prompts/system_prompts.py)
- [Config](config/settings.py)
- [Safety](safety/radiology_gate.py)
- [Observability](observability/tracing.py)
- [Evals](evals/evaluator.py)
- [Benchmarks](benchmarks/benchmark.py)
- [Examples](examples/example_run.py)
- [Tests](tests/test_structure.py)
- [Architecture](docs/ARCHITECTURE.md)
