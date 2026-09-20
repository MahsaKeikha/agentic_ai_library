# Experimental Plan
## NeurIPS 2027 selective human oversight

## Phase 1: controlled research harness

Build deterministic action traces with known unsafe-action labels and controlled reviewer availability.

Fault families:
- indirect prompt injection;
- stale evidence;
- corrupted tool output;
- permission escalation;
- action irreversibility;
- conflicting agent recommendations;
- critic failure;
- state desynchronization;
- delayed reviewer response;
- reviewer unavailable.

Purpose:
- validate implementation;
- test finite-sample certificate;
- construct counterexamples;
- establish ablations before expensive model runs.

## Phase 2: public agent benchmarks

### AgentDojo

Use realistic tool-use tasks and prompt-injection attacks.

Add an oversight adapter that observes the proposed tool call and available state features before execution.

Report both user-task utility and security outcomes.

### AgentHarm

Use the benchmark to study whether the oversight policy detects and escalates harmful multi-step actions without making benign operation unusable.

### WASP

Use web-agent prompt-injection tasks to test whether the intervention policy transfers to a different action environment.

## Phase 3: Atlas-derived high-consequence scenarios

Use controlled scenarios where authority and evidence semantics are explicit:
- F117 Digital Twin Engineer;
- AGEWELL CITY;
- Smart City Agentic AI;
- release and deployment workflow.

These environments are not substitutes for public benchmarks. They are used for mechanism isolation and interpretable failure analysis.

## Models

Evaluate multiple model families and at least one open-weight model if computationally feasible.

Do not tune and evaluate on the same benchmark split.

Preserve:
- exact model identifiers;
- decoding parameters;
- prompts;
- tool schemas;
- seeds where applicable;
- environment versions;
- raw trajectories.

## Risk models

Compare:
1. model self-confidence where available;
2. LLM-as-judge risk score;
3. disagreement score across independent critics;
4. supervised lightweight risk model;
5. combined feature model.

The final paper should not depend on privileged chain-of-thought.

## Human review representations

Stage A:
- expert-authored gold intervention labels;
- deterministic simulated reviewer availability.

Stage B, only with appropriate study approval:
- human reviewers approve, reject, or edit proposed actions;
- measure review time, error rate, fatigue, and information sufficiency.

No human-subject claims before Stage B is actually conducted.

## Baselines

- always act;
- always ask;
- static hard-gate only;
- raw risk threshold;
- uncalibrated uncertainty gate;
- LLM judge gate;
- disagreement gate;
- RCSO;
- RCSO without hard authority;
- RCSO without evidence features;
- RCSO without disagreement features.

## Main plots

1. residual episode risk versus autonomy coverage;
2. task utility versus human review fraction;
3. unsafe-autonomy rate at fixed review budgets;
4. calibration curves by environment;
5. intervention lead time;
6. review precision-recall;
7. failure taxonomy after oversight;
8. distribution-shift degradation.

## Statistical reporting

Report confidence intervals and independent seeds.

Use episode-level resampling when actions inside episodes are dependent.

Avoid treating every tool call as an independent sample.

## Success criterion

The paper becomes submission-ready only if the proposed method demonstrates a reproducible improvement in the safety-review tradeoff on external public agent benchmarks, not only on Atlas-derived scenarios.
