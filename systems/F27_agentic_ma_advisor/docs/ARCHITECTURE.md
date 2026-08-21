# F27 Architecture

F27 separates reasoning responsibilities across five visible agents. Agents use reusable skills and deterministic tools. The workflow maintains explicit context, memory, safety gates, and trace events. Evaluation checks coverage and evidence handling. Human approval is required before consequential external actions.

## Layers

1. AGENTS: specialist decision support roles
2. TOOLS: deterministic calculations and data operations
3. SKILLS: reusable analysis procedures
4. orchestration: workflow coordination
5. memory: local execution memory
6. schemas: structured context
7. prompts: behavior guidance
8. safety: approval and stop conditions
9. observability: execution tracing
10. evals and benchmarks: quality validation
