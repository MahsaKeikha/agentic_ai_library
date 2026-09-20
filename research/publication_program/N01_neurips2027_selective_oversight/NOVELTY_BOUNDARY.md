# Novelty Boundary and Prior-Art Map

Updated: 2026-09-19

## What is already established

Human approval for sensitive tool calls is already an engineering pattern in current agent frameworks. Fixed approval gates therefore cannot be the novelty claim.

Agent safety benchmarks already evaluate harmful multi-step behavior and prompt-injection attacks. A new paper must do more than introduce another list of harmful tasks.

Selective autonomy and confidence-based deferral are also established ideas in machine learning and have recently been demonstrated in domain-specific agent systems. A plain confidence threshold is not a sufficient contribution.

Formal tool-use safety work already studies information-flow constraints, temporal tool policies, runtime authorization, and independent enforcement at tool boundaries.

## Current gap targeted by this paper

The targeted gap is the joint problem of:

- sequential tool-using agents;
- learned action risk;
- hard nonlearned authority boundaries;
- scarce human-review capacity;
- episode-level residual risk;
- calibrated act/ask/abstain decisions;
- safety and utility measured together.

The paper should make human review a measurable resource rather than a binary design slogan.

## Closest comparison families

### Fixed human approval gates

Strength:
- simple;
- fail closed for explicitly listed actions.

Limitation for this research question:
- no learned prioritization of reviewer attention;
- no calibrated residual-risk target;
- depends on hand-written action classes.

### AgentDojo and related prompt-injection benchmarks

Strength:
- realistic tool-use environments;
- joint utility and security evaluation.

Difference:
- our primary object is the intervention policy and human-review allocation, not only attack success.

### AgentHarm

Strength:
- measures harmful multi-step agent capability and misuse.

Difference:
- our question is whether selective human oversight can control residual autonomous risk while preserving useful autonomy.

### Selective autonomy and deferral

Strength:
- established accuracy-coverage framework;
- relevant foundation for review routing.

Difference:
- the proposed benchmark is sequential and action-taking;
- risk is measured at episode level;
- hard authority constraints remain outside the learned risk model;
- reviewer availability and abstention are explicit.

### Formal tool-use safety

Strength:
- can enforce explicit requirements and tool/data constraints.

Difference:
- deterministic safety rules remain complementary;
- this paper studies learned risk ranking and review allocation for behavior not fully captured by hard rules.

## Claims we should not make

Do not claim:
- the first human-in-the-loop agent system;
- the first selective-autonomy method;
- the first risk-calibration method;
- the first safety benchmark for agents;
- the first tool-authorization framework;
- guaranteed real-world safety.

A defensible novelty claim will depend on the final method and experiments, not on terminology.
