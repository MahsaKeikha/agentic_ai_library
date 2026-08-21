# F50 IoT Engineering

F50 is a multi-agent IoT engineering system with separate executable agents, tools, skills, orchestration, state, memory, schemas, prompts, safety, observability, evaluation, benchmarks, examples, tests, and architecture documentation.

## Agents

- [`device_onboarding_agent.py`](AGENTS/device_onboarding_agent.py)
- [`telemetry_agent.py`](AGENTS/telemetry_agent.py)
- [`edge_processing_agent.py`](AGENTS/edge_processing_agent.py)
- [`connectivity_agent.py`](AGENTS/connectivity_agent.py)
- [`fleet_operations_agent.py`](AGENTS/fleet_operations_agent.py)

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
python launcher.py F50
```

Human approval remains required for fleet rollout, rollback, credential, and physical deployment decisions.
