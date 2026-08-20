# F31 to F40: AI Engineering Systems

This batch extends the unified Agentic AI Library with ten engineering-grade multi-agent system specifications. Each system is designed for offline-first examples, explicit evidence/state handling, evaluation, and human approval before consequential external actions.

| ID | System | Core multi-agent roles | Primary output |
|---|---|---|---|
| F31 | Agentic ML Engineer | Requirements Analyst, Data Analyst, Feature Engineer, Model Engineer, Evaluator, Risk Reviewer | ML engineering package and experiment recommendation |
| F32 | Agentic MLOps Team | Release Planner, Pipeline Engineer, Registry Manager, Deployment Reviewer, Observability Agent, Rollback Reviewer | Deployment plan and release gate |
| F33 | Agentic Data Engineering | Source Analyst, Schema Designer, Pipeline Engineer, Data Quality Agent, Lineage Reviewer, Reliability Agent | Data pipeline design and quality report |
| F34 | Agentic Prompt Engineering | Task Analyst, Prompt Designer, Test Generator, Evaluator, Red Team Reviewer, Version Manager | Prompt package with evaluation evidence |
| F35 | Agentic RAG Engineering | Corpus Analyst, Chunking Designer, Retrieval Engineer, Ranking Agent, Grounding Evaluator, Safety Reviewer | RAG architecture and retrieval evaluation |
| F36 | Agentic Multi-Agent Orchestrator | Task Router, Planner, Agent Registry, State Manager, Conflict Resolver, Gatekeeper | Multi-agent execution plan and trace |
| F37 | Agentic LLM Evaluator | Evaluation Designer, Dataset Curator, Judge Coordinator, Bias Reviewer, Safety Evaluator, Report Writer | Model evaluation report |
| F38 | Agentic AI Benchmark Suite | Benchmark Designer, Dataset Validator, Runner, Metrics Analyst, Reproducibility Reviewer, Reporter | Reproducible benchmark package |
| F39 | Agentic AI Product Manager | Problem Analyst, User Research Agent, Requirements Agent, Prioritization Agent, Risk Agent, Launch Reviewer | AI product requirements and release recommendation |
| F40 | Agentic AI Infrastructure Architect | Workload Analyst, Model Gateway Architect, Compute Planner, Reliability Architect, Security Reviewer, Cost Analyst | AI infrastructure architecture package |

## Shared engineering contract

Every implementation in this batch must preserve:

1. explicit inputs and structured outputs
2. specialized agent responsibilities rather than one monolithic prompt
3. shared state or memory with traceable updates
4. deterministic offline demonstration path
5. unknown or missing evidence represented explicitly rather than invented
6. evaluation criteria appropriate to the system
7. failure and escalation paths
8. human approval before deployment, publication, destructive changes, or other consequential external actions
9. tests for core workflow and gate behavior
10. responsible-use notes and operational boundaries

## Build order

F31 and F37 establish the model-development and evaluation primitives. F32 and F38 establish release and benchmark primitives. F33 and F35 establish data and retrieval primitives. F34 provides prompt lifecycle management. F36 provides orchestration primitives. F39 and F40 connect the technical systems to product and infrastructure decisions.

Status: **In development on `feature/unified-f31-f40`**.
