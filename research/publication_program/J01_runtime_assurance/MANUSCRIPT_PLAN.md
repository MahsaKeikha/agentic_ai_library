# J01 Research Plan
## Compositional Runtime Assurance for Heterogeneous Agentic AI Systems Under Human Authority

## Research question

Can a heterogeneous multi-agent AI system use high-performance, non-deterministic agents while guaranteeing that protected actions and other authority constraints remain invariant under runtime execution, stale evidence, agent disagreement, tool faults, and asynchronous handoffs?

## Distinction from existing Atlas material

The Atlas already contains protected actions, deterministic gates, evidence ledgers, human review states, and fail-closed behavior. Those are engineering design patterns.

J01 must add a formal control model and prove properties that the current Atlas does not establish.

## Proposed system model

Let the closed-loop agentic system be a hybrid/discrete-event system with state

x_k = (q_k, e_k, a_k, z_k, h_k, r_k)

where:
- q_k: workflow/task state
- e_k: evidence state including completeness and freshness
- a_k: authority and permission state
- z_k: tool/environment state
- h_k: human-review availability/state
- r_k: risk and unresolved-blocker state

The advanced agent team proposes action u^A_k.

A verified runtime supervisor maps

u_k = S(x_k, u^A_k)

into one of:
- EXECUTE(u^A_k)
- MODIFY(u^A_k)
- SAFE_FALLBACK
- HUMAN_REVIEW
- ABSTAIN

## Safe set

Define the authority-safe set K as all states satisfying:
1. no protected action is executed without a valid authority certificate,
2. required evidence is present and fresh,
3. tool permissions remain within the delegated scope,
4. unresolved hard blockers cannot be converted into success,
5. escalation state remains reachable when a safe autonomous action does not exist.

## Candidate theorem family

### T1 Authority invariance
If x_0 is in K, the baseline supervisory policy is feasible, and every executed action is filtered by S, then x_k remains in K for all k.

### T2 Compositional safety
If each subsystem i enforces a local admissible-action contract and shared cross-agent constraints satisfy a compatibility condition, then the composed multi-agent system preserves the global authority-safe set.

### T3 Safe degradation under evidence loss
If evidence freshness crosses a specified boundary, the supervisor moves the system into HUMAN_REVIEW or SAFE_FALLBACK before any protected transition becomes enabled.

### T4 Conditional nonblocking/liveness
If at each reachable safe state there exists either an admissible autonomous transition or a reachable authorized human transition, the supervisor does not introduce deadlock except at explicitly terminal fail-closed states.

These are proof obligations, not established results until formally derived and checked.

## Experimental plan

Use at least four heterogeneous Atlas scenarios:
- F36 software/release orchestration
- F117/F118 industrial digital twin/factory automation
- AGEWELL CITY
- Smart City Agentic AI

Inject:
- stale evidence
- prompt/tool injection
- delayed human approval
- tool unavailability
- agent disagreement
- corrupted critic output
- correlated agent error
- permission escalation request
- state desynchronization

Compare:
1. unconstrained agent execution
2. prompt-only policy
3. deterministic rule gate
4. proposed runtime-assurance supervisor
5. ablated supervisor without evidence freshness
6. ablated supervisor without human escalation mode

Primary metrics:
- protected-action violation rate
- unsafe-transition rate
- task completion
- human interventions per run
- time to escalation
- false escalation rate
- recovery success
- deadlock rate
- evidence freshness at execution
- authority leakage events

## Reproducibility package

Planned files:
- formal_model.md
- supervisor.py
- scenario_adapters/
- fault_injection.py
- experiments.yaml
- run_experiments.py
- results/raw/
- results/summary.csv
- figures/
- tests/
- environment lock file
- RESULT_MANIFEST.md

## Literature risks already identified

Runtime assurance and Simplex architectures are established in control systems and multi-agent systems. Recent work also addresses bounded/governed agentic execution and delegation safety. Therefore J01 cannot claim that runtime supervision itself is new.

The novelty must come from the specific formalization and guarantees for heterogeneous tool-using LLM agent workflows: authority state, evidence freshness, protected-action reachability, human escalation as a control mode, and compositional safety across asynchronous agent/tool boundaries.

## Primary venue

IEEE Transactions on Automatic Control, only if the final contribution contains genuinely strong control-theoretic results and proofs.

Fallback scope-aligned venues:
- Automatica
- IEEE Transactions on Systems, Man, and Cybernetics: Systems
- IEEE Transactions on Artificial Intelligence

## Status

Research formulation started. No theorem or quantitative result is yet claimed.
