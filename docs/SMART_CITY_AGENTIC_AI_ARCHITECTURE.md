# Smart City Agentic AI

## Why I built this demo

A smart city is often described as if it were one intelligent system. In reality, a city is many systems that depend on one another and often want different things at the same time.

The electricity network wants stability. Transit wants capacity. Emergency services want clear routes. Water operations may need pumping power during the same hours that cooling demand is rising. Infrastructure teams need trustworthy asset data. Citizens need clear information. City leadership still owns decisions that carry legal, safety, privacy, public health, or political consequences.

That is the problem I wanted this demo to show.

Smart City Agentic AI is a public software demonstration of how specialized agents can coordinate around one shared city state without turning the AI layer into an invisible city authority.

The public runtime uses synthetic data only. It is not connected to a municipality, utility, hospital, police service, transport network, emergency service, camera network, identity system, building-control system, or production city digital twin.

## The basic idea

The system has a control plane and several specialists.

The specialists keep responsibility for their own domains. The control plane does not replace them. Its job is to understand dependencies, route work, preserve evidence, expose conflicts, and decide whether a proposed action stays inside the allowed operating envelope.

The public architecture is:

```text
Synthetic City State
        |
        v
F36 City Control Plane
        |
        +--> Energy Agent
        +--> Mobility Agent
        +--> Water Agent
        +--> Emergency Coordination
        +--> Infrastructure Agent
        +--> Citizen Services Agent
        +--> F117 Urban Digital Twin
        |
        v
Shared Constraint Arbitration
        |
        v
F37 Evaluation + F09 Safety and Privacy
        |
        +--> bounded reversible action
        |
        +--> CITY_HOLD when a hard blocker remains
        |
        v
Human or Qualified City Authority
```

## Why the city is multi-agent

I do not think the right smart-city architecture is one very large agent with access to every city system.

That would make permissions, accountability, evaluation, privacy, and failure handling much harder to reason about.

Instead, the public demo separates the work.

### F36 City Control Plane

F36 is responsible for planning, routing, shared state, handoffs, conflict arbitration, blocker propagation, and approval eligibility.

It does not have unlimited civic authority. It cannot declare an emergency, order an evacuation, shut down protected hospital power, override a safety interlock, change a public health threshold, or grant unrestricted identity surveillance.

### F117 Urban Digital Twin

The digital twin keeps a model of the city state across multiple domains. The important part is not only the model itself. The runtime also tracks whether the twin is current, which version is being used, and how much uncertainty is present.

If the twin becomes stale, that is visible. The system does not quietly continue as if the model were still trustworthy.

### Energy Agent

The Energy Agent reads synthetic grid state, identifies flexible demand, and proposes reversible load actions.

Critical services such as hospitals, emergency communications, and critical cooling are treated as protected constraints in the public demo.

### Mobility Agent

The Mobility Agent works with aggregate road and transit conditions. It can simulate bounded signal timing changes and transit service adjustments.

It does not have police authority. It does not issue fines, suspend licenses, or track individuals.

### Water Agent

The Water Agent works with synthetic demand, reservoir state, pumping, and flood conditions.

It can shift noncritical pumping inside a configured operating envelope. It cannot change drinking-water safety thresholds.

### Emergency Coordination

This agent can build an emergency access plan and request temporary signal priority on an approved route.

It cannot declare a city emergency or order an evacuation.

### Infrastructure Agent

The Infrastructure Agent can route a synthetic inspection to a tunnel, substation, cooling plant, pump, or other approved city asset.

It does not bypass safety systems or declare critical equipment safe.

### Citizen Services Agent

This agent prepares public information and supports digital service routing.

It does not issue legal determinations or publish an unapproved emergency order.

### F09 Safety and F37 Evaluation

The assurance layer checks whether the combined city plan has enough evidence, stays inside the tool policy, respects privacy, and avoids protected authority.

A good evaluation score cannot cancel a hard blocker.

## The tool policy

The runtime core is in `docs/smart-city-agentic-ai-core.js`.

Every tool has an authority class.

| Authority class | What it means | Public demo behavior |
|---|---|---|
| `READ_ONLY` | Read synthetic state | allowed |
| `ANALYSIS` | Calculate, compare, project, or prepare | allowed |
| `BOUNDED_AUTONOMY` | Reversible synthetic action inside a predefined envelope | allowed and logged |
| `PROTECTED` | Consequential civic, safety, privacy, or public-health authority | denied and logged |

Examples of bounded actions in the public demo include:

- adjusting traffic signal timing inside configured limits
- shifting predefined noncritical municipal loads
- changing synthetic transit service capacity
- shifting noncritical water pumping
- routing an inspection team or robot to an approved asset
- preparing public information for authorized release

Protected actions include:

- declaring an emergency
- ordering an evacuation
- shutting down protected hospital power
- overriding a safety interlock
- changing a water quality threshold
- unrestricted identity tracking

The public system fails closed when a protected tool is requested.

## Scenario 1: extreme heat, grid stress, and metro disruption

This is the flagship operating scenario.

The city is experiencing severe heat. Grid demand is close to the configured review ceiling. Metro capacity is reduced. Water demand is high. Emergency access still needs to remain available.

A simple optimizer could make the wrong decision because the systems are coupled.

The Energy Agent may want immediate load reduction. The Water Agent may still need pumping. The Mobility Agent may want to increase transit service. The Emergency Agent needs a reliable medical corridor. The city cannot optimize those goals independently.

The runtime therefore:

1. reads grid state
2. reads mobility and transit state
3. reads water state
4. checks digital twin freshness
5. projects cross-system impact
6. identifies protected and flexible loads
7. records the conflict
8. reduces predefined noncritical municipal load
9. shifts noncritical water pumping
10. increases synthetic transit capacity
11. applies bounded signal timing changes
12. plans and applies an approved emergency corridor priority
13. prepares a public service message
14. runs evaluation and safety checks
15. produces a final city decision package

If the hard constraints are satisfied, the final state is `STABILIZED`.

## Scenario 2: flash flood, tunnel closure, and emergency corridor

The second scenario focuses on physical city resilience.

A road tunnel shows rising water. Traffic spills into other routes. Hospital access becomes slower. The system coordinates water, mobility, infrastructure inspection, and emergency access.

The agent system may make reversible traffic and pump scheduling changes, but it cannot declare an emergency or order an evacuation.

Those decisions remain with the responsible city authority.

## Scenario 3: adversarial city operations request

The third scenario tests the boundary directly.

An untrusted message asks the system to hide an infrastructure alarm, bypass safety policy, open restricted access, and track an individual across the city without approval.

The runtime records the input as untrusted, detects the policy-override pattern, preserves the original evidence, denies the protected tools, creates blockers, and ends in `CITY_HOLD`.

This scenario is important because a city system should not become more powerful simply because an instruction sounds urgent.

## Privacy position

The public demo uses aggregate synthetic city state.

It does not need facial recognition, individual movement histories, or cross-city identity tracking to demonstrate city coordination.

Unrestricted identity tracking is deliberately registered as a protected action so a visitor can test the boundary and see the request denied.

A real city deployment would need a much deeper privacy architecture, including lawful purpose, minimization, access control, retention rules, consent where applicable, auditability, and independent review.

## Event trace and evidence

Every important runtime action creates an event with:

```text
sequence number
id
time
type
actor
summary
payload
phase
```

The browser exposes these records in the City Event Trace.

A visitor can select an event and inspect the structured evidence behind it.

This is important because the demo is meant to show more than a final answer. It should be possible to reconstruct why the system acted, what evidence it used, which tool was called, and whether the action was allowed.

## Secondary fault injection

The page also includes `INJECT SECOND FAULT`.

The injected failure depends on the scenario.

In the heat scenario, the urban twin becomes stale while the city is under high load.

In the flood scenario, stormwater telemetry becomes stale.

In the adversarial scenario, a conflicting utility asset record appears.

The injected fault can move a previously stable city into `CITY_HOLD`.

## Final states

The first runtime uses three clear states:

- `READY`
- `STABILIZED`
- `CITY_HOLD`

The final state is not based on how confident or fluent an agent sounds. It comes from runtime conditions, tool policy, blockers, and assurance checks.

## Runtime self test

The deterministic core includes a built-in self test.

It checks that:

1. the heat scenario stabilizes
2. bounded actions actually occur
3. hospital power remains protected
4. the flood scenario improves the synthetic emergency response time
5. the adversarial scenario ends in `CITY_HOLD`
6. unrestricted identity tracking is denied
7. an attempted evacuation order fails closed
8. a secondary fault can create a hold

There is also a Node.js test in `tests/test_smart_city_agentic_ai_runtime.js` so the core can be checked outside the webpage.

## What would change in a real city deployment

A production city system would be a much larger engineering program.

The synthetic browser adapters would need to be replaced by authenticated services. The architecture would need durable state, city-specific digital twin integration, utility interfaces, mobility APIs, asset systems, emergency coordination interfaces, cyber controls, privacy governance, human approval services, audit storage, observability, rollback, and independent verification.

A representative production pattern would look like this:

```text
City Operations Interface
        |
        v
Authenticated City API
        |
        v
F36 Orchestration and State
        |
        +--> City Digital Twin
        +--> Utility Adapters
        +--> Mobility Services
        +--> Water and Flood Systems
        +--> Asset Management
        +--> Citizen Service Systems
        +--> Evaluation and Safety
        |
        v
Policy Enforcement Point
        |
        +--> read and analysis tools
        +--> bounded approved actions
        +--> protected action approval service
        |
        v
Append-only Audit and Evidence Store
```

A real implementation should also include least-privilege service identities, signed requests, tool allowlists, data freshness checks, idempotency for side effects, replay protection, rate limits, timeout and retry policy, environment separation, incident response, rollback, and city-specific safety analysis.

## Public design context

I shaped the demo around public themes already visible in advanced city programs.

Digital Dubai publicly describes integrated, predictive digital city experiences and has launched a Dubai Digital Twin Platform for urban planning and decision support. The UAE has also announced a government framework for expanding Agentic AI across public services and operations.

NEOM publicly describes advanced digital infrastructure, AI and robotics, data privacy, smart mobility, renewable energy, water systems, and people-centered technology as parts of its future city vision.

Starbase in Texas provides a different kind of reference point: a newly created city closely tied to advanced manufacturing, launch infrastructure, engineering operations, and a commercial spaceport.

Smart City Agentic AI is not affiliated with any of those organizations or governments. The goal is to build a neutral architecture that could be adapted to many future-city environments.

## The design principle

The principle behind the demo is simple:

**A city can become more intelligent without making its authority less accountable.**

That is the direction I want Smart City Agentic AI to make visible.