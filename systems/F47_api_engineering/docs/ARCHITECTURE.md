# F47 API Engineering Architecture

F47 uses separate agent, skill, and tool layers coordinated by an orchestrator. Run state, memory, schemas, prompts, safety controls, observability, and evaluation remain explicit so each decision can be inspected independently.

## Execution flow

1. Contract analysis defines consumers, resources, operations, compatibility, and error semantics.
2. Authentication and authorization analysis defines trust boundaries and access requirements.
3. Reliability analysis defines latency, availability, retries, idempotency, and failure behavior.
4. Testing analysis defines contract, integration, negative, and regression coverage.
5. Documentation analysis produces a traceable developer handoff.
6. Human approval remains required before consequential release actions.
