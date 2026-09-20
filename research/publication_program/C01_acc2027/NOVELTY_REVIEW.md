# C01 Novelty Review
## Supervisory Control of Protected Actions in Tool-Using Multi-Agent AI

Updated: 2026-09-19

## Research gap retained after prior-art review

The initial concept "put a runtime safety supervisor around an agent" is not novel. Runtime assurance, Simplex architectures, tool-call enforcement, temporal constraints, authorization layers, provenance-aware execution, and human-approval guardrails already exist.

The paper is therefore narrowed to a different systems/control question:

> Given a finite abstraction of a tool-using multi-agent workflow, can we automatically synthesize a supervisor that not only blocks directly forbidden protected actions, but also disables otherwise-benign precursor actions when an uncontrollable evidence/authority invalidation can leave the workflow with no safe path to completion, review, or fail-closed termination?

The reviewed agent-safety methods generally enforce action-level, temporal, information-flow, or authorization properties at runtime. The proposed contribution instead uses supervisory control of discrete-event systems to compute the maximally permissive safe and nonblocking subbehavior of an agentic task automaton.

This statement is a scoped novelty position, not a claim of absolute priority. It should be rechecked immediately before submission.

## Closest reviewed work

### Distributed / Black-Box Simplex
Relevant because it establishes runtime assurance for multi-agent or autonomous cyber-physical systems by switching away from an unverified advanced controller.

Difference retained here:
- AESC operates on discrete task/tool events rather than continuous plant safety sets.
- Authority, evidence validity, and human-review states are explicit workflow semantics.
- The control objective includes nonblocking task/review reachability and maximal permissiveness.

### Agent-C: Enforcing Temporal Constraints for LLM Agents
Relevant because it enforces temporal policies on sequences of LLM tool calls.

Difference retained here:
- Agent-C checks/formally constrains action traces against temporal properties.
- AESC synthesizes a supervisor from an explicit plant/task model and uncontrollable events.
- AESC's distinctive test is precursor suppression: an action may be locally legal yet disabled because it enters a state from which uncontrollable invalidation can destroy safe nonblocking completion.

### Towards Verifiably Safe Tool Use for LLM Agents
Relevant because it uses STPA-derived requirements, information-flow constraints, and capability labels for tool safety.

Difference retained here:
- that work focuses on hazard derivation and enforceable data-flow/tool-sequence specifications;
- AESC focuses on discrete-event supervisor synthesis, controllability, nonblockingness, and maximal permissiveness.

### Governed Agentic Process Automation
Relevant because it provides a deterministic policy-derived floor that prevents under-escalation below a mandated minimum.

Difference retained here:
- floor-safety is a pointwise routing guarantee;
- AESC reasons about future reachability and uncontrollable invalidations in the task graph.

### Commit-Time Authorization / SARA / authenticated delegation
Relevant because these works separate capability from authority, preserve provenance, or require action-specific authorization at execution.

Difference retained here:
- AESC does not replace commit-time authorization.
- It addresses an earlier control question: whether a precursor transition should be allowed at all when later invalidation can strand the workflow.

### AgentGuard
Relevant because it maps agent I/O into formal events and performs runtime probabilistic verification.

Difference retained here:
- AgentGuard estimates/verifies probabilistic properties online;
- AESC synthesizes deterministic disabling control for a modeled finite-state task abstraction.

### Vera
Relevant as a strong recent safety-testing benchmark for non-deterministic tool-using agents.

Difference retained here:
- Vera is a testing and evidence-grounded verification framework;
- AESC is a controller-synthesis method.

## Novelty that should be claimed

The manuscript may claim a new *formulation and synthesis application* consisting of:

1. an Authority-Evidence Task Automaton (AETA) for tool-using multi-agent workflows;
2. explicit partition of agent/tool actions as controllable events and evidence/authority invalidations as uncontrollable events;
3. human-review states as accepted safe marked modes;
4. automatic synthesis of the largest safe, uncontrollable-closed, nonblocking subbehavior;
5. upstream suppression of locally legal precursor actions when future uncontrollable invalidation would make safe completion impossible;
6. reproducible cross-domain Atlas-derived abstractions plus finite-state scaling tests.

Do not claim that supervisory control theory, runtime assurance, authorization gating, human-in-the-loop control, provenance, or evidence freshness are individually new.

## Title-level supervisory-control precedent checked

The 2026 CAIS paper by Wangfan Li and Carlos Toxtli, "Supervisory Control Theory for LLM Revision," was checked through its bibliographic record and public presentation/expanded description. It introduces Prompt-Level Supervisory Alignment for iterative manuscript revision and uses supervisory-control functions as a structured prompting/oversight strategy. It does not synthesize a Ramadge--Wonham discrete-event supervisor over tool/task events, uncontrollable authority/evidence invalidations, forbidden protected-action states, and marked human-review states.

This removes the main title-level collision identified in the first scan. The paper should nevertheless cite Li and Toxtli directly and avoid implying that applying any form of supervisory-control language to LLMs is itself new.

## Submission position

The contribution is best framed as a control/systems paper at ACC 2027. A later journal extension must add substantially more than the conference result, for example:
- compositional multi-agent contracts;
- partial observation;
- asynchronous message-age models;
- dynamic/incremental supervisor updates;
- richer real-agent experiments;
- formal treatment of human availability and escalation delay.
