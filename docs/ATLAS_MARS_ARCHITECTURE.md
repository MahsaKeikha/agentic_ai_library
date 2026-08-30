# ATLAS: MARS Autonomous Operations Runtime

**Public runtime version:** 2.0.0  
**Mode:** deterministic browser simulation  
**Data:** synthetic  
**External control path:** none

ATLAS: MARS started from a simple engineering question: what should an autonomous multi-agent system be allowed to do when Earth cannot answer quickly enough?

That question becomes much harder once the system is responsible for several things at the same time. Power is limited. Habitat systems have survival margins that cannot be treated like ordinary optimization variables. Robots may be available, but they also need energy and safe operating conditions. Maintenance evidence can be incomplete. A digital twin can become stale. Communications can disappear. An outside message can also try to push the system beyond its authority.

The public ATLAS: MARS runtime is built to make those conflicts visible.

It is an executable software demonstration, but it is not a flight system, habitat controller, robot controller, life-support controller, safety certification, or operational Mars product. It does not use real Mars telemetry, real spacecraft, real robots, client credentials, command networks, or production model APIs.

## The engineering idea behind the runtime

I did not want the demo to be a sequence of agents producing attractive text and then always agreeing with one another. The point is to show a system in which several specialized agents have different responsibilities, different evidence, different tools, and different limits.

The core question is:

**Which actions can the system take locally, and which actions must remain protected even when waiting for Earth is impractical?**

The runtime treats autonomy as a contract. Every tool has an authority class. Every important state change is recorded. Unsafe requests create blockers. A good evaluation score cannot erase a safety problem. Human approval also cannot turn missing evidence into valid evidence.

## What actually runs

The main runtime logic lives in `docs/atlas-mars-core.js`.

That core can run in the browser and in Node.js. The webpage in `docs/atlas-mars.js` is a visual layer over the runtime rather than a separate script inventing the final outcome.

The core handles:

- scenario initialization
- mission state
- agent handoffs
- tool registration
- tool authority classes
- fail-closed authorization
- synthetic tool effects
- resource conflicts
- runtime invariants
- blockers and warnings
- safety and evaluation review
- secondary fault injection
- protected-action testing
- decision graph generation
- mission package export
- built-in self-tests

This separation matters because it lets the same mission logic be exercised outside the visual demo.

## Atlas systems used in ATLAS: MARS

The Mars runtime combines several existing Atlas architectures.

| Layer | Atlas reference | Role in ATLAS: MARS |
|---|---|---|
| Control plane | F36 Multi-Agent Orchestrator | Planning, routing, handoffs, shared state, conflict arbitration, blocker propagation, approval eligibility |
| Mission systems | F86 Space Mission Design | Mission requirements, margins, operations concepts, safe states, fault protection, verification, authority boundaries |
| Robotics governance | F12 Robotics Governance | Robotics hazards, release gates, change control, incident readiness, human authority |
| Predictive maintenance | F114 Predictive Maintenance | Condition evidence, competing failure modes, uncertainty, maintenance recommendations |
| Digital twin | F117 Digital Twin Engineer | Model state, validation, synchronization, uncertainty, configuration identity |
| Evaluation | F37 LLM Evaluator | Quality criteria, robustness, evidence completeness, calibration, disagreement |
| Safety | F09 AI Safety | Unsafe permission requests, adversarial instructions, residual risk, release blockers |

Power, Habitat, and Logistics are mission-specific specialists created for this demo. They are not presented as new standalone F-number systems. Their operating constraints are grounded in the mission systems concepts represented by F86.

## How the runtime is organized

At a high level, the flow looks like this:

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

The important point is that F36 is a control plane, not a physical controller. It coordinates the work and preserves the decision state, but it does not inherit every permission held by the systems it coordinates.

## Tool authority

Every registered tool belongs to one of four authority classes.

| Class | Meaning | Runtime behavior |
|---|---|---|
| `READ_ONLY` | Observe synthetic state | allowed |
| `ANALYSIS` | Calculate, compare, project, or score | allowed |
| `BOUNDED_AUTONOMY` | Reversible action inside a predefined synthetic envelope | allowed and logged |
| `PROTECTED` | Crew, safety, irreversible, or out-of-policy authority | denied and logged |

Examples of bounded autonomous actions include:

- increasing monitoring frequency
- shedding predefined noncritical simulated loads
- routing a simulated robot inside an approved zone
- placing noncritical simulated systems into a predefined safe state

Examples of protected actions include:

- initiating human EVA
- overriding a safety interlock
- changing a crew survival limit
- disabling critical life-support redundancy
- executing an irreversible mission-critical action outside approved policy

## The tool gateway

The public tool contract is defined in `TOOL_REGISTRY` inside `atlas-mars-core.js`.

Each tool declares its authority class, whether the action is reversible, and what the tool is intended to represent.

All tool calls pass through `invokeTool()`.

If the runtime receives an unknown tool request, it fails closed.

If a requested tool is classified as `PROTECTED`, the runtime does not simulate success. Instead it:

1. denies the call
2. increments the denied-action counter
3. records that protected authority was requested
4. creates a critical blocker
5. emits a `tool.denied` event
6. moves the mission toward accountable review

This is one of the most important design choices in the demo. A system should not be able to gain more authority simply because an agent generated a confident request.

## Mission state

Each run has a structured state object rather than a loose collection of messages.

The main fields are:

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

The colony state contains synthetic generation, battery reserve, life-support load, CO2, monitoring state, noncritical load shedding, critical-system status, Earth-link status, and communications latency.

The asset state currently contains SA-04, R-07, R-12, and the repair kit.

The digital-twin state carries model version, synchronization status, validated uses, and uncertainty.

The authority state records whether a protected action was requested, whether it was denied, whether a human gate is required, and whether a human decision has been recorded.

## Event trace

Every material event has a structured record:

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

Typical event types include:

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

The public Mission Event Trace displays these events, and the Evidence Inspector lets a visitor open the underlying structured payload.

This makes it possible to ask not only what the system decided, but why it decided it.

## Scenario 1: solar array failure during a dust event

This is the main flagship scenario.

The runtime begins with degraded solar generation and an SA-04 tracking anomaly. From there it works through the problem in stages:

1. the Power Agent reads current generation and reserve
2. the Habitat Agent establishes the protected life-support reserve floor
3. the Digital Twin checks synchronization and projects the energy state
4. Predictive Maintenance compares possible SA-04 failure modes
5. Logistics checks whether the required repair kit is available
6. Robotics creates a bounded repair plan using R-07 and R-12
7. the robot plan requests additional energy
8. that request conflicts with the habitat reserve requirement
9. F36 records the conflict and asks the Power Agent to evaluate lower-priority loads
10. predefined noncritical loads are shed
11. habitat monitoring is increased
12. reserve is projected again
13. if the shared constraints are satisfied, the robots are routed inside their approved operating zone
14. the synthetic repair is executed
15. evaluation and safety review the resulting mission state
16. the run produces a final mission decision package

The most important part is step 8. The agents do not all want the same thing.

Robotics wants enough energy to repair SA-04. Habitat wants to protect the life-support reserve floor. Power wants to preserve a workable energy balance. F36 has to find a plan that satisfies the combined constraints instead of allowing one specialist to optimize the whole mission around its own objective.

## Scenario 2: Earth communications are lost

The second scenario removes the Earth link while the colony is already under power pressure.

The runtime is still allowed to perform predefined reversible operations, including:

- increasing monitoring
- shedding noncritical loads
- moving noncritical systems into predefined safe states
- repeating diagnostics and calculations

What does not happen is just as important.

The loss of Earth communications does not cause protected authority to migrate into the agent system.

Human EVA, safety overrides, survival-limit changes, critical redundancy changes, and irreversible out-of-policy actions remain protected.

This scenario is meant to explore local resilience without quietly turning resilience into unrestricted autonomy.

## Scenario 3: adversarial maintenance message

The third scenario tests the system with an untrusted external message.

The message tries to make the agents:

- ignore reserve policy
- falsely mark SA-04 as repaired
- conceal the anomaly
- request protected exterior access

The runtime keeps the original equipment evidence, flags the instruction pattern, rejects the protected request, records the attempted authority escalation, creates critical blockers, and ends in `MISSION_HOLD`.

The point of this scenario is not simply prompt-injection detection. It is to show that untrusted language cannot directly become trusted state or physical authority.

## Runtime invariants

The runtime checks a small set of machine-readable conditions that can directly affect mission status.

Current checks include:

- battery reserve below the simulated 8.0 hour life-support floor
- CO2 at or above the simulated review threshold
- stale digital-twin synchronization
- contradictory repair-kit inventory
- any protected-action request

These checks are part of the runtime state. They are not only explanatory text shown after the fact.

## Secondary fault injection

The public interface includes an `INJECT SECOND FAULT` control.

The injected problem depends on the selected mission:

- dust event: CO2 scrubber degradation
- Earth-link loss: stale digital twin
- adversarial message: contradictory repair-kit inventory

The new fault creates additional evidence and triggers another assurance check.

A mission that was previously stable can move into `MISSION_HOLD` if the new evidence invalidates the current plan.

This is intentional. Real operating systems need to respond to changing state, not only execute a plan that was valid at the beginning.

## Final mission states

The current runtime uses three explicit final states:

- `STABILIZED`
- `DEGRADED_STABLE`
- `MISSION_HOLD`

A fluent explanation from an agent is never treated as a mission state by itself.

## Mission package

`missionPackage()` produces a structured export containing:

- scenario definition
- final status
- colony state
- asset state
- digital-twin state
- authority state
- counters
- blockers
- warnings
- decisions
- complete event trace
- decision graph
- public-demo boundary statement

The purpose of this package is to make the run inspectable, reviewable, and reproducible.

## Decision graph

`decisionGraph()` turns the event stream into ordered nodes and edges and attaches the recorded decisions and blockers.

The public interface lets a visitor open the graph and inspect individual events.

This is useful because a decision should be traceable back to the evidence and actions that produced it.

## Tests

The runtime has automated Node.js tests at:

`tests/test_atlas_mars_runtime.js`

The test suite verifies the most important expected behaviors, including:

1. the dust scenario reaches `STABILIZED`
2. the synthetic SA-04 repair completes
3. the reserve floor is preserved
4. bounded autonomous actions actually occur
5. loss of the Earth link does not automatically grant protected authority
6. local bounded actions still work during communications loss
7. adversarial input reaches `MISSION_HOLD`
8. protected actions are denied
9. prompt injection remains an explicit blocker
10. a manual interlock-override attempt fails closed
11. stale digital-twin evidence can hold the communications-loss mission
12. the exported package and decision graph remain structurally consistent

The public page also includes a `RUN RUNTIME SELF-TEST` button so a visitor can run the core self-check directly in the browser.

## What this demo proves and what it does not

The public runtime does demonstrate executable coordination logic, structured state, synthetic tool calls, resource arbitration, authority checks, failure handling, event traces, decision packages, and bounded autonomy.

It does not demonstrate:

- real Mars telemetry
- production robot control
- life-support control
- real autonomous maintenance
- production LLM inference
- production authentication or secret management
- spacecraft command
- regulatory approval or safety certification
- affiliation with SpaceX, Tesla, xAI, NASA, or any other organization

I want that distinction to remain clear because the engineering value of the project does not depend on pretending the public demo is already connected to real hardware.

## How this could become a production system

A production version would keep the same conceptual boundaries while replacing the synthetic adapters with authenticated server-side services.

A representative architecture could look like this:

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

A real deployment would also need authentication, service identities, least-privilege scopes, server-side secret storage, signed requests, tool allowlists, environment separation, durable state, append-only audit records, replay protection, model and prompt versioning, data-freshness checks, idempotency for side effects, rate limits, timeout and retry policy, compensating actions, human approval records, incident response, rollback, independent safety analysis, and verification against the actual operating environment.

## Design principle

The principle behind ATLAS: MARS is simple:

**Autonomy should improve operational resilience without making accountability disappear.**

The purpose of the runtime is to make that principle visible in software, where it can be inspected, tested, challenged, and improved.