# ATLAS: MARS - Autonomous Operations Architecture

ATLAS: MARS is a public, executable browser simulation for studying multi-agent coordination under communications delay, scarce resources, subsystem failures, and explicit human authority boundaries.

It is not a flight system, habitat controller, robot controller, safety certification, or operational Mars product. All telemetry, assets, crew counts, environmental values, tool calls, failures, and outcomes in the public page are synthetic.

## Core question

**Which actions may an autonomous multi-agent system take when Earth cannot answer in time, and which actions must remain protected even when delay makes remote supervision impractical?**

The demo treats autonomy as a bounded engineering contract rather than a binary on/off property.

## Reference architectures used

| Layer | Atlas reference | Role in ATLAS: MARS |
|---|---|---|
| Control plane | F36 Multi-Agent Orchestrator | Planning, capability routing, handoffs, state, conflict arbitration, blocker propagation, approval eligibility |
| Mission systems | F86 Space Mission Design | Mission requirements, margins, operations concept, fault protection, safe states, verification, mission authority boundaries |
| Robotics governance | F12 Robotics Governance | Robotics hazards, gates, change control, incident readiness, human governance boundaries |
| Predictive maintenance | F114 Predictive Maintenance | Condition evidence, competing failure modes, uncertainty, maintenance recommendation |
| Digital twin | F117 Digital Twin Engineer | Physical-to-digital mapping, model state, validation, synchronization, uncertainty, configuration identity |
| Evaluation | F37 LLM Evaluator | Quality rubrics, robustness, calibration, disagreement, evidence thresholds |
| Safety | F09 AI Safety | Hazard review, unsafe permission requests, adversarial instructions, residual risk, release blockers |

Mission-specific Power, Habitat, and Logistics specialists are public demo roles. They are not represented as new standalone Atlas F-number systems. Their constraints are grounded in F86 mission systems and operations concepts.

## Runtime architecture

```text
Synthetic Colony State
        |
        v
F36 Control Plane
        |
        +--> Power Specialist
        +--> Habitat Specialist
        +--> F117 Digital Twin
        +--> F114 Maintenance
        +--> F12 Robotics Governance / Robotics Ops
        +--> Logistics Specialist
        +--> F86 Mission Systems
        |
        v
Shared Resource Arbitration
        |
        v
F37 Evaluation + F09 Safety
        |
        v
Bounded Autonomous Action OR Mission Hold
        |
        v
Protected Human / Qualified Authority Boundary
```

## Default scenario

The flagship scenario is **Solar array failure during dust event**.

The runtime models:

1. Solar generation degradation.
2. A suspected SA-04 solar-array actuator fault.
3. Battery reserve projection.
4. Habitat critical-load floor.
5. A robotic repair plan using R-07 and R-12.
6. Repair energy demand that conflicts with habitat reserve.
7. Logistics verification for the repair kit.
8. F36 arbitration across subsystem constraints.
9. Bounded noncritical load shedding.
10. Evaluation and safety review.
11. A simulated robotic repair when blockers are clear.
12. A final decision package with traceable evidence.

The central demonstration is the conflict between local objectives. The Robotics specialist wants energy to complete the repair. The Habitat specialist protects life-support reserve. The Power specialist identifies load-shedding options. F36 must produce a plan that satisfies the combined constraints rather than allowing one agent to optimize independently.

## Additional scenarios

### Earth link lost with declining reserve

The system may continue predefined reversible operations such as increased monitoring, noncritical load shedding, safe-state transitions, and approved-zone robot routing. Protected crew or irreversible actions remain behind local accountable human authority.

### Adversarial maintenance message

The runtime receives an instruction attempting to override reserve policy, conceal an anomaly, and request protected access. F09-style safety logic records the attempt, blocks the authority escalation, and prevents the unsafe instruction from becoming a tool side effect.

## Bounded autonomous actions in the public demo

The browser simulation permits only synthetic, reversible state changes:

- increase monitoring frequency
- route a simulated robot within an approved zone
- shed predefined noncritical compute or science loads
- rerun diagnostics
- update the local plan
- move noncritical simulated systems into predefined safe states

These actions do not affect any external system.

## Protected actions

The public architecture keeps the following outside autonomous authority:

- human EVA initiation
- life-support or robotics safety-interlock override
- crew exposure or survival-limit changes
- disabling critical life-support redundancy
- irreversible mission-critical action outside predefined policy
- flight, launch, propulsion, spacecraft-command, or real habitat-control authority

Human approval does not turn failed evidence into passing evidence. Active technical or safety blockers must be resolved first.

## Evidence model

Each public runtime event contains an event identifier, UTC timestamp, event type, actor, summary, and structured payload.

Tool-call records additionally preserve:

- tool name
- arguments
- result
- side-effect class
- authorization class

The final mission package can be exported as JSON and includes the event trace and decision graph.

## Decision graph

The demo preserves a compact graph such as:

```text
Mission state
  -> F36 plan
  -> Power reserve forecast
  -> Digital-twin projection
  -> SA-04 failure hypothesis
  -> Logistics verification
  -> Robotics energy request
  -> Habitat reserve constraint
  -> F36 resource arbitration
  -> F37/F09 assurance
  -> bounded action or mission hold
```

The purpose is to make it possible to move backward from an outcome to the evidence and agent interactions that produced it.

## Public claim boundary

ATLAS: MARS demonstrates browser-executable orchestration logic, synthetic tool interfaces, state transitions, resource arbitration, evidence inspection, adversarial blocking, bounded actions, and authority gates.

It does **not** demonstrate real Mars operations, production autonomy, flight software, certified robotics safety, validated life-support control, operational digital-twin performance, or connectivity to any aerospace company or agency.

## Production evolution

A real implementation would require a server-side architecture with authenticated data and tool adapters, durable state, signed audit events, tested policy enforcement, independent evaluation, cybersecurity, fault-tolerant infrastructure, simulation and hardware-in-the-loop validation, domain-qualified engineering review, and organization-specific command authority.

A production path would resemble:

```text
Mission UI
  -> authenticated API
  -> F36-style orchestrator
  -> typed specialist services
  -> read-only telemetry and model services
  -> policy-enforced tool gateway
  -> durable state + event ledger
  -> evaluation + safety services
  -> explicit command-authority service
  -> separately engineered operational control systems
```

The analytical multi-agent layer should remain separable from any system capable of commanding physical equipment.