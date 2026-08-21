# F49 Embedded Systems

F49 is a multi-agent embedded systems engineering system with separate executable agents, tools, skills, orchestration, state, memory, schemas, prompts, safety, observability, evaluation, benchmarks, examples, tests, and architecture documentation.

## Agents

- [`requirements_agent.py`](AGENTS/requirements_agent.py)
- [`hardware_interface_agent.py`](AGENTS/hardware_interface_agent.py)
- [`firmware_architecture_agent.py`](AGENTS/firmware_architecture_agent.py)
- [`timing_agent.py`](AGENTS/timing_agent.py)
- [`verification_agent.py`](AGENTS/verification_agent.py)

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
python launcher.py F49
```

Human approval remains required for hardware release, firmware release, and physical deployment decisions.
