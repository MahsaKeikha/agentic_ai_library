# ATLAS: MARS Autonomous Operations Runtime

**Public runtime version:** 2.0.0  
**Mode:** deterministic browser simulation  
**Data:** synthetic  
**External control path:** none

ATLAS: MARS is an executable public demonstration of governed multi-agent coordination under communications delay, scarce resources, subsystem failures, adversarial instructions, and explicit human authority boundaries.

It is not a flight system, habitat controller, robot controller, life-support controller, safety certification, or operational Mars product. No real telemetry, client credentials, spacecraft, robot, habitat, mission network, or production model API is connected.

## Core engineering question

**Which actions may a local multi-agent system take when Earth cannot answer in time, and which actions must remain protected even when delay makes remote supervision impractical?**

The runtime treats autonomy as a contract with explicit permissions, invariants, evidence, side-effect classes, and failure states rather than a binary setting.

## What actually executes

The public page is driven by `docs/atlas-mars-core.js`, a deterministic runtime core that can execute in both the browser and Node.js.

The core implements:

- scenario state initialization
- structured mission state
- agent handoff records
- a registered tool catalog
- tool side-effect and authority classes
- fail-closed authorization checks
- synthetic tool effects
- resource arbitration
- runtime invariants
- blocker and warning creation
- safety and evaluation review
- secondary fault injection
- protected-action tests
- decision graph generation
- mission-package export
- built-in self-tests

The browser UI in `docs/atlas-mars.js` renders that runtime. It does not independently invent the final state.

## Reference architectures

| Layer | Atlas reference | Role in ATLAS: MARS |
|---|---|---|
| Control plane | F36 Multi-Agent Orchestrator | Planning, capability routing, handoffs, state, conflict arbitration, blocker propagation, approval eligibility |
| Mission systems | F86 Space Mission Design | Mission requirements, margins, operations concept, fault protection, safe states, verification, mission authority boundaries |
| Robotics governance | F12 Robotics Governance | Robotics hazards, gates, change control, incident readiness, human governance boundaries |
| Predictive maintenance | F114 Predictive Maintenance | Condition evidence, competing failure modes, uncertainty, maintenance recommendation |
| Digital twin | F117 Digital Twin Engineer | Model state, validation, synchronization, uncertainty, configuration identity |
| Evaluation | F37 LLM Evaluator | Quality rubrics, robustness, calibration, disagreement, evidence thresholds |
| Safety | F09 AI Safety | Unsafe permission requests, adversarial instructions, residual risk, release blockers |

Power, Habitat, and Logistics are mission-specific demo specialists. They are not represented as new standalone Atlas F-number systems. Their constraints are grounded in the F86 mission-systems and operations concepts.

## Runtime flow

```text
Synthetic Colony State
        |
        v
F36 Control Plane
        |
        +--> Power Specialist
        +--> Habitat Specialist
        +--> F117 Digital Twin
        +--> F114 Predictive Maintenance
        +--> F12 Robotics Ops / Governance
        +--> Logistics Specialist
        +--> F86 Mission Systems Constraints
        |
        v
Shared Resource Arbitration
        |
        v
F37 Evaluation + F09 Safety
        |
        +--> PASS -> bounded synthetic action
        |
        +--> HOLD -> evidence preserved, action denied
        |
        v
Protected Human / Qualified Authority Boundary
```

## Authority classes

Every registered tool has one of four authority classes.

| Class | Meaning | Public runtime behavior |
|---|---|---|
| `READ_ONLY` | Observe synthetic state | allowed |
| `ANALYSIS` | Calculate, compare, project, or score | allowed |
| `BOUNDED_AUTONOMY` | Reversible action inside a predefined synthetic envelope | allowed and logged |
| `PROTECTED` | Crew, safety, irreversible, or out-of-policy authority | denied and logged |

Examples of bounded actions include increasing monitoring frequency, shedding predefined noncritical simulated loads, routing a simulated robot inside an approved zone, and placing noncritical synthetic systems into a predefined safe state.

Examples of protected actions include human EVA initiation, safety-interlock override, crew survival-limit changes, critical-redundancy disablement, and irreversible mission-critical actions outside approved policy.

## Tool gateway

`TOOL_REGISTRY` in `atlas-mars-core.js` is the public tool contract.

Each tool record declares:

```text
name
authority class
reversibility
description
```

All tool calls pass through `invokeTool()`.

If a tool is unknown, the runtime fails closed.

If a tool is `PROTECTED`, the runtime:

1. denies execution
2. increments the denied-action counter
3. records that protected authority was requested
4. adds a critical blocker
5. emits a `tool.denied` event
6. requires accountable review

The public demo therefore cannot turn a protected request into a synthetic success merely because an agent asked for it.

## Mission state model

A run contains structured state for:

```text
schema_version
runtime_version
run_id
created_at
scenario
status
phase
colony
assets
twin
authority
counters
blockers
warnings
decisions
events
secondary_fault_injected
completed_at
```

The colony state includes synthetic generation, reserve, life-support load, CO2, monitoring state, noncritical load shedding, critical-system state, Earth-link state, and latency.

The asset state includes SA-04, R-07, R-12, and the repair kit.

The twin state includes model version, synchronization status, validated use cases, and uncertainty.

## Event schema

Every material runtime event contains:

```text
seq
id
time
type
actor
summary
payload
phase
```

Representative event types include:

```text
run.created
agent.handoff
tool.call
tool.denied
resource.conflict
arbitration.completed
gate.blocker
assurance.warning
evaluation.completed
safety.review
fault.injected
authority.boundary
run.completed
```

The UI exposes these records through the Mission Event Trace and Evidence Inspector.

## Default scenario: solar array failure during dust event

The runtime models:

1. degraded solar generation
2. an SA-04 tracking anomaly
3. battery reserve projection
4. an explicit habitat reserve floor
5. digital-twin synchronization and uncertainty
6. competing actuator failure hypotheses
7. repair-kit verification
8. R-07/R-12 robotic task planning
9. repair energy demand that conflicts with habitat reserve
10. F36 resource arbitration
11. predefined noncritical load shedding
12. increased habitat monitoring
13. reserve recalculation
14. bounded robot routing
15. synthetic routine repair
16. safety and evaluation review
17. final mission decision package

The central demonstration is not a sequence of agents agreeing with one another. It is a conflict between objectives.

The Robotics specialist wants energy to repair SA-04. The Habitat specialist protects a life-support reserve floor. The Power specialist proposes lower-priority loads that can be shed. F36 must find a plan satisfying the combined constraints.

## Communications-loss scenario

When the Earth link is unavailable, the runtime may continue only predefined reversible operations such as:

- increased monitoring
- noncritical load shedding
- noncritical safe-state transitions
- diagnostic re-evaluation

The loss of Earth communications does not cause protected authority to silently migrate into the agent system.

Human EVA, safety overrides, survival-limit changes, and irreversible out-of-policy actions remain protected.

## Adversarial scenario

The untrusted maintenance message attempts to:

- override reserve policy
- falsely mark SA-04 repaired
- conceal an anomaly
- request protected exterior access

The runtime detects the instruction pattern, preserves the original equipment state, denies the protected tool request, records the attempt, creates critical blockers, and finishes in `MISSION_HOLD`.

## Runtime invariants

The deterministic core checks machine-readable conditions including:

- battery reserve below the simulated 8.0 hour life-support floor
- CO2 at or above the simulated review threshold
- stale digital-twin synchronization
- contradictory repair-kit inventory
- any protected-action request

These conditions are not merely explanatory text. They directly affect blocker state and final mission status.

## Secondary fault injection

The public UI includes `INJECT SECOND FAULT`.

The injected fault depends on the selected scenario:

- dust event -> CO2 scrubber degradation
- Earth-link loss -> stale digital twin
- adversarial input -> contradictory repair-kit inventory

The runtime then emits new evidence and performs another assurance check.

A secondary fault can move a previously stable mission into `MISSION_HOLD`.

## Final states

The current deterministic runtime uses explicit final states:

- `STABILIZED`
- `DEGRADED_STABLE`
- `MISSION_HOLD`

A fluent narrative is never itself a final state.

## Decision package

`missionPackage()` exports:

- scenario definition
- final status
- final colony state
- asset state
- digital-twin state
- authority state
- counters
- blockers
- warnings
- decisions
- full event trace
- decision graph
- public-demo boundary statement

The export is intended to make the demonstration inspectable and replayable.

## Decision graph

`decisionGraph()` creates event nodes plus ordered edges, decisions, and blockers.

The browser UI lets a visitor open the complete graph and select a node to inspect the corresponding evidence record.

## Automated tests

The runtime has a Node test suite at:

`tests/test_atlas_mars_runtime.js`

The CI workflow runs the runtime tests on repository pushes and pull requests.

The self-test verifies at least the following properties:

1. dust scenario reaches `STABILIZED`
2. SA-04 synthetic repair completes in the nominal scenario
3. the reserve floor is preserved
4. bounded autonomous actions actually occur
5. Earth-link loss does not automatically request protected authority
6. local bounded actions still execute during communications loss
7. adversarial input reaches `MISSION_HOLD`
8. protected actions are denied
9. prompt injection remains an explicit blocker
10. a manual interlock-override test fails closed
11. stale-twin fault injection holds the communications-loss mission
12. exported package and decision graph are structurally consistent

The page also exposes a browser-side **RUN RUNTIME SELF-TEST** button.

## Public claim boundary

The public runtime demonstrates executable coordination logic, synthetic tools, state transitions, policy checks, event traces, failure logic, and authority boundaries.

It does not demonstrate:

- real Mars telemetry
- production robot control
- life-support control
- real autonomous maintenance
- production LLM inference
- production authentication or secrets
- spacecraft command
- regulatory or safety certification
- affiliation with any external company or agency

## Production evolution

A production implementation should keep the conceptual control boundaries while replacing synthetic adapters with authenticated server-side services.

A representative deployment would use:

```text
Operator UI
    |
    v
Authenticated Mission API
    |
    v
Orchestrator / State Machine
    |
    +--> Model-backed specialists
    +--> Telemetry adapters
    +--> Digital-twin service
    +--> Inventory / asset service
    +--> Robot fleet service
    +--> Evaluation service
    |
    v
Policy Enforcement Point
    |
    +--> read / analysis tools
    +--> bounded approved actions
    +--> protected-action approval service
    |
    v
Append-only Event / Audit Store
```

Production requirements would include:

- authenticated users and service identities
- least-privilege connector scopes
- server-side secret storage
- signed requests
- tool allowlists
- environment separation
- durable state
- append-only audit events
- replay protection
- model and prompt versioning
- data freshness checks
- idempotency keys for side effects
- rate limits
- timeout and retry policies
- compensating actions
- human approval records
- incident response
- rollback
- independent safety analysis
- verification against the actual operational design domain

## Design principle

**Autonomy should increase operational resilience without causing accountability to disappear.**

The purpose of ATLAS: MARS is to make that principle visible as software rather than leaving it as a slogan.
