# F47 API Engineering

F47 is a multi-agent API engineering system with separate executable agents, tools, skills, orchestration, state, memory, safety, observability, evaluation, benchmarks, examples, tests, and architecture documentation.

## Agents

- [`contract_agent.py`](AGENTS/contract_agent.py)
- [`auth_agent.py`](AGENTS/auth_agent.py)
- [`reliability_agent.py`](AGENTS/reliability_agent.py)
- [`testing_agent.py`](AGENTS/testing_agent.py)
- [`documentation_agent.py`](AGENTS/documentation_agent.py)

## Tools

- [`schema_validator.py`](TOOLS/schema_validator.py)
- [`rate_limit_planner.py`](TOOLS/rate_limit_planner.py)
- [`response_checker.py`](TOOLS/response_checker.py)
- [`test_matrix.py`](TOOLS/test_matrix.py)
- [`doc_builder.py`](TOOLS/doc_builder.py)

## Skills

- [`contract_design.py`](SKILLS/contract_design.py)
- [`auth_policy.py`](SKILLS/auth_policy.py)
- [`reliability_planning.py`](SKILLS/reliability_planning.py)
- [`api_test_design.py`](SKILLS/api_test_design.py)
- [`documentation_planning.py`](SKILLS/documentation_planning.py)

## Supporting architecture

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
python launcher.py F47
```

Human approval remains required before consequential release actions.
