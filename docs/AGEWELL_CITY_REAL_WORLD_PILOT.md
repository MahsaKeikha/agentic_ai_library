# AGEWELL CITY Real World Pilot

## AGEWELL 01

The first real implementation should be small enough to understand and large enough to matter.

I would not begin by trying to connect an entire city or healthcare system. I would begin with one senior living community, mixed age residential development, retirement campus, assisted living campus, or age friendly neighborhood.

The first pilot can be called AGEWELL 01.

AGEWELL 01 is a deployable intelligence layer for independent and assisted living. It connects approved data, keeps a shared operating state, coordinates specialist agents, prepares support actions, and preserves a complete evidence trail.

The goal is to prove that several everyday systems can work together without turning the resident into a surveillance target or giving software authority it should not have.

## What the first pilot should connect

A practical first version could include:

- apartment or home temperature and environmental state
- building management data
- elevator and accessibility state
- resident call or check in systems
- community shuttle and transport availability
- maintenance requests and work orders
- community activity and service schedules
- selected door or access state where appropriate and authorized
- optional wearable signals when a resident chooses to connect them
- authorized caregiver and staff communication

The system should begin read only wherever possible.

The first milestone is not automation. It is proving that the shared state is accurate, consent is respected, stale data is visible, and operators find the coordination useful.

## Phase 1: Observe

Connect a small set of approved data sources.

Every connector should have an owner, purpose, access scope, retention rule, and freshness expectation.

The pilot should be able to answer basic questions such as:

- Is the home environment data current?
- Is an elevator available?
- Is an accessible shuttle available?
- Is a maintenance request open?
- Is a resident check in system working?
- Which support contacts are authorized for this purpose?

No agent should be allowed to guess when a source is missing or stale.

## Phase 2: Coordinate

Once the data can be trusted, the system can create one shared operating state.

That state should not become one unrestricted resident record.

Different roles should still see different information.

A mobility agent may need route and accessibility information. A building agent may need equipment state. A caregiver support agent may need authorized observations and routine context. None of those roles automatically need every other data category.

## Phase 3: Recommend

The system can then begin preparing recommendations.

Examples include:

- suggest an accessible route when an elevator is unavailable
- identify an alternate shuttle option
- request a resident preferred check in
- flag that a home sensor is stale
- coordinate a maintenance visit with a resident preference window
- identify an available cooling space during extreme heat
- prepare an authorized caregiver brief

Every recommendation should show why it was made and what evidence was used.

## Phase 4: Add bounded actions

Only after the team understands the data and recommendation quality should a small number of reversible actions be introduced.

Examples could include:

- submit an accessible shuttle request
- open a nonclinical staff support request
- send an approved resident check in message
- apply a resident approved comfort preset
- notify an authorized care circle contact

Each action should have a clear rollback or cancellation path where possible.

## Protected areas

The first pilot should not automate:

- medication changes
- diagnosis
- treatment decisions
- emergency dispatch
- consent override
- continuous identity tracking
- resident lockout
- legal capacity decisions
- high consequence clinical or safety decisions

These areas can appear in the system as protected boundaries so the runtime can demonstrate that it knows where to stop.

## A practical technical architecture

```text
Resident App + Staff Console + Family Portal
        |
        v
Authenticated AGEWELL API
        |
        v
F36 Orchestration Layer
        |
        +--> F59 Caregiver Support
        +--> Home Environment Agent
        +--> Accessible Mobility Agent
        +--> Assisted Living Agent
        +--> Community Services Agent
        +--> Consent and Privacy Service
        |
        v
F37 Evaluation + F09 Safety
        |
        v
Policy and Tool Gateway
        |
        +--> building systems
        +--> resident check in system
        +--> shuttle and transport systems
        +--> maintenance platform
        +--> community schedule
        +--> approved caregiver communication
        +--> optional wearable connectors
        |
        v
Event and Evidence Store
```

The Policy and Tool Gateway is one of the most important pieces.

Connecting a system does not mean every agent can use it.

The gateway decides which role may read which data, which action can be requested, which action can execute automatically, and which action requires a person.

## Data model

The pilot should separate at least four kinds of state.

### Resident preferences

Examples include communication preference, comfort range, accessibility needs, preferred support contacts, and consent choices.

### Operational state

Examples include elevator availability, shuttle status, maintenance state, home environment, community capacity, and service availability.

### Support state

Examples include whether a check in was requested, whether transport was arranged, whether a support request is open, and whether a caregiver notification was sent.

### Protected clinical state

Clinical information should remain inside the appropriate clinical system and role boundary. AGEWELL CITY should not casually duplicate or expand access to sensitive clinical records.

## What to measure

A first pilot should measure outcomes that people and operators can actually feel.

Useful measures include:

- time from issue detection to human awareness
- time from support request to resolution
- accessible shuttle reliability
- maintenance response time
- number of stale data conditions detected
- number of recommendations accepted or rejected
- false alert rate
- resident satisfaction with support and control
- caregiver or staff coordination time
- unsafe or unauthorized actions blocked
- number of cases resolved without unnecessary escalation
- participation in community services

## Resident experience

The resident interface should be simple.

It should make clear:

- what the system knows
- why it knows it
- who can see it
- what support is being offered
- what will happen next
- how to say no
- how to pause or change preferences

The resident should not need to understand agent architecture to remain in control.

## Staff experience

Staff should receive a coordinated picture rather than another stream of disconnected alerts.

A good operator view should show:

- what changed
- which systems are involved
- what has already been checked
- what action is proposed
- what evidence is missing
- which resident preference matters
- what needs human judgment

## Family and caregiver experience

Authorized family or caregivers should receive only the information appropriate to their role and the resident consent.

The goal is to reduce uncertainty and coordination burden, not to create a constant surveillance feed.

## Security and privacy

The real system should include:

- authenticated users and services
- role based access control
- purpose based data access where practical
- encrypted transport and storage
- consent records
- connector level permissions
- append only audit events
- data retention rules
- incident handling
- key rotation
- environment separation
- monitoring for unusual access

## Pilot team

A small first pilot can be built by a focused team.

Core roles include:

- product and systems lead
- software developer
- integration engineer
- UX designer with accessibility experience
- senior living or caregiving domain advisor
- privacy and security reviewer
- operator representative from the pilot site

The team does not need to build everything at once.

The first useful product can begin with a few connectors, one shared state, one operator console, several specialist agents, a clear consent model, and two or three bounded support workflows.

## The first three workflows I would build

### Workflow 1: Independent living support

Environment state + missed preferred check in + accessible mobility option + authorized care circle notification.

### Workflow 2: Assisted living access disruption

Elevator or facility access problem + resident mobility need + staff support request + transport coordination.

### Workflow 3: Heat resilience

Community heat + cooling space capacity + accessible transport + home comfort support + consent based check ins.

These three workflows are understandable, measurable, and broad enough to prove the architecture without crossing into autonomous clinical decision making.

## What the pilot should prove

AGEWELL 01 should prove five things.

1. Independent and assisted living systems can share a useful operating picture.
2. Consent and privacy can remain visible inside the architecture.
3. Specialist agents can coordinate without one agent receiving every permission.
4. Small reversible support actions can reduce coordination friction.
5. The system can stop when evidence is weak or human authority is required.

If those five things work reliably, the platform can expand carefully into a larger community and eventually become one layer of a broader age friendly smart city.