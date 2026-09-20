# Multi-Agent AI Atlas Publication Program

## Goal

Build a coordinated portfolio of 10 journal papers and 5 conference papers from the Multi-Agent AI Atlas and AI Engineering Handbook foundations, while ensuring that every paper contains a genuinely new scientific contribution rather than repackaging existing website, book, or repository material.

The existing Atlas is treated as shared research infrastructure: reference architectures, deterministic runtimes, evidence ledgers, protected-action policies, human approval gates, evaluation harnesses, and cross-domain scenarios. New papers must add theory, algorithms, formal models, benchmarks, experiments, or human-machine evidence beyond those assets.

## Publication integrity rules

1. No paper may claim novelty merely because an Atlas feature has not previously appeared in a journal.
2. Every manuscript must have its own research question, formal contribution, experiment set, and main figures.
3. Shared infrastructure is cited and disclosed; paper-specific algorithms and results live in separate reproducible packages.
4. No fabricated measurements, simulated claims presented as real deployment, or invented human-subject results.
5. Human-subject experiments require appropriate ethics/IRB review before data collection when applicable.
6. Conference and journal versions may share a lineage only when the journal adds substantial new theory, proofs, data, or experiments and the relationship is disclosed.
7. Every paper receives a prior-art review before the title, novelty statement, and target venue are frozen.

## Ten journal papers

| ID | Working title | Core new contribution | Primary target |
|---|---|---|---|
| J01 | Compositional Runtime Assurance for Heterogeneous Agentic AI Systems Under Human Authority | Hybrid/discrete-event safety model, compositional safe-set invariance, deterministic protected-action supervisor, human escalation as a formal control mode | IEEE Transactions on Automatic Control |
| J02 | Risk-Aware Event-Triggered Human Oversight for Agentic Systems | Event-triggering law that minimizes unnecessary review while bounding risk and escalation delay; intervention-load theorem and simulations | Automatica |
| J03 | Model Predictive Orchestration of Multi-Agent AI Under Cost, Latency, Evidence, and Risk Constraints | Receding-horizon orchestration of agent/tool selection with hard authority constraints and stochastic task uncertainty | IEEE Transactions on Control Systems Technology |
| J04 | Evidence-Constrained Automation: Provenance and Freshness as Control-State Variables in Agentic Workflows | New evidence-state dynamics, provenance constraints, stale-evidence detection, and safe fallback policy | IEEE Transactions on Automation Science and Engineering |
| J05 | Observability and Diagnosability of Agentic Workflows Through Evidence and Decision Ledgers | Graph-theoretic observability/diagnosability conditions for reconstructing agent actions, hidden failure modes, and approval paths | IEEE Transactions on Systems, Man, and Cybernetics: Systems |
| J06 | Adaptive Human Oversight Under Alert Load in Multi-Agent AI | Human-machine control model for selective escalation, workload-sensitive thresholds, missed-intervention risk, and interface-aware evaluation | IEEE Transactions on Human-Machine Systems |
| J07 | Chance-Constrained Delegation and Authority Allocation for Tool-Using AI Agents | Formal delegation variable, chance constraints on protected actions, uncertainty-aware authority allocation, and calibrated rollback | IEEE Transactions on Artificial Intelligence |
| J08 | Fault-Tolerant Orchestration of LLM Agent Teams Under Correlated and Common-Mode Failures | Correlated failure model, diversity-aware routing, critic independence metric, reconfiguration policy, and benchmark | Autonomous Agents and Multi-Agent Systems |
| J09 | Agentic Control Planes for Industrial Cyber-Physical Systems: Safe Tool Use, Digital Twins, and Recovery | Industrial agentic control architecture with deterministic tool gateway, digital-twin state validation, rollback, and fault-injection experiments | IEEE Transactions on Industrial Informatics |
| J10 | Decision-Theoretic Human Authority in Agentic AI: When Should a System Ask, Act, Abstain, or Escalate? | Unified formal decision model of action, abstention, delegation, review, reversibility, and accountability with cross-domain evaluation | Artificial Intelligence |

## Five conference papers

| ID | Working title | Distinct new contribution | Primary target |
|---|---|---|---|
| C01 | Supervisory Control of Protected Actions in Agentic Task Graphs | Discrete-event supervisory controller that disables unsafe task transitions while preserving nonblocking progress | American Control Conference 2027 |
| C02 | Correlated Failure Benchmarks for Multi-Agent LLM Orchestration | New benchmark, failure-injection protocol, common-mode failure taxonomy, and recovery baselines | AAMAS 2027 |
| C03 | Event-Triggered Human Intervention for Multi-Agent Decision Systems | Compact theory and simulation study of selective human takeover under risk and delay constraints | IEEE Conference on Decision and Control |
| C04 | Evidence-Aware Delegation for Tool-Using AI Agents | New delegation policy that conditions authority on evidence completeness, freshness, and action reversibility | AAAI / ICLR cycle after full benchmark completion |
| C05 | Human-Supervised Agentic Digital Twins for Industrial Automation | Agentic digital-twin testbed with fault injection, constrained tool execution, operator gate, and recovery metrics | IEEE CASE / ICRA-aligned automation venue |

## Shared experimental infrastructure

The following Atlas assets are infrastructure, not paper results:

- F36 Multi-Agent Orchestrator
- F37 LLM Evaluator
- F09 AI Safety
- F117 Digital Twin Engineer
- F118 Factory Automation
- AGEWELL CITY runtime
- Smart City Agentic AI runtime
- protected-action registries
- evidence and event ledgers
- deterministic tests and CI
- the Agentic AI Gold Standard
- the Enterprise Readiness Assessment
- the 170-system taxonomy

Paper-specific experiments must introduce new test harnesses, baselines, metrics, ablations, seeds, and result manifests.

## Immediate sequence

### Phase A: formalize and validate J01 / C01
Build the common mathematical foundation for runtime assurance and supervisory control, while keeping the conference and journal contributions distinct.

### Phase B: build C02 / J08 correlated-failure benchmark
Use heterogeneous Atlas agents and controlled fault injection to quantify common-mode, correlated, critic, routing, and recovery failures.

### Phase C: event-triggered human oversight
Develop C03 and then the broader J02/J06 line, including workload models and, only when approved, human-subject evaluation.

### Phase D: industrial control and digital twin
Extend F117/F118 into J03/J09/C05 with new model-predictive orchestration, tool-gateway constraints, and industrial fault-injection scenarios.

### Phase E: evidence, observability, and delegation
Complete J04/J05/J07/J10/C04 with formal evidence-state, graph-observability, uncertainty, and decision-theoretic models.

## Submission rule

A manuscript is not marked submission-ready until:
- novelty review complete
- mathematical claims checked
- code and tests pass
- figures regenerated from committed data
- results reproduced from a clean environment
- target venue scope and formatting checked
- related Atlas/book material cited and differentiated
- conflict/overlap audit complete
- manuscript, supplement, cover letter, data/code statement, and checklist prepared
