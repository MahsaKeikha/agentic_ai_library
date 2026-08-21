# F48 Database Architecture

F48 is a multi-agent database architecture system with separate executable agents, tools, skills, orchestration, state, memory, schemas, prompts, safety, observability, evaluation, benchmarks, examples, tests, and architecture documentation.

## Agents

- [`schema_agent.py`](AGENTS/schema_agent.py)
- [`query_performance_agent.py`](AGENTS/query_performance_agent.py)
- [`migration_agent.py`](AGENTS/migration_agent.py)
- [`resilience_agent.py`](AGENTS/resilience_agent.py)
- [`security_agent.py`](AGENTS/security_agent.py)

## Core layers

- [`TOOLS/`](TOOLS/)
- [`SKILLS/`](SKILLS/)
- [`orchestration/`](orchestration/)
- [`memory/store.py`](memory/store.py)
- [`state/run_state.py`](state/run_state.py)
- [`schemas/contracts.py`](schemas/contracts.py)
- [`prompts/system_prompts.py`](prompts/system_prompts.py)
- [`config/settings.py`](config/settings.py)
- [`safety/`](safety/)
- [`observability/tracing.py`](observability/tracing.py)
- [`evals/evaluator.py`](evals/evaluator.py)
- [`benchmarks/benchmark.py`](benchmarks/benchmark.py)
- [`examples/example_run.py`](examples/example_run.py)
- [`tests/test_structure.py`](tests/test_structure.py)
- [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md)

## Run

```bash
python launcher.py F48
```

Human approval remains required for consequential production database changes.
