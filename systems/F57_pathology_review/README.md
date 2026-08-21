# F57 Agentic Pathology Review

## Agents
- [Specimen Workflow Agent](AGENTS/specimen_workflow_agent.py)
- [Metadata Validator](AGENTS/metadata_validator.py)
- [Case Completeness Agent](AGENTS/case_completeness_agent.py)
- [Quality Agent](AGENTS/quality_agent.py)
- [Escalation Agent](AGENTS/escalation_agent.py)
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
- [Safety](safety/pathology_gate.py)
- [Observability](observability/tracing.py)
- [Evals](evals/evaluator.py)
- [Benchmarks](benchmarks/benchmark.py)
- [Examples](examples/example_run.py)
- [Tests](tests/test_structure.py)
- [Architecture](docs/ARCHITECTURE.md)
