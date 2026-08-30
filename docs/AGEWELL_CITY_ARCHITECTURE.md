# AGEWELL CITY Architecture

## Why I built this flagship

AGEWELL CITY started from a simple question: what would a smart city look like if it were designed around a longer human life?

Most smart city concepts focus on traffic, energy, buildings, public safety, logistics, and economic growth. Those systems matter, but a city also has to work for someone who is 75, 85, or 95. It has to work for someone who wants to stay in their own home. It has to work for someone who uses a walker, needs an accessible shuttle, depends on a caregiver, or lives in an assisted living community.

The goal of AGEWELL CITY is not to automate aging. The goal is to make the systems around an older person coordinate better while protecting independence, consent, dignity, privacy, and human judgment.

This public implementation is a synthetic runtime. It does not diagnose, prescribe, change medication, control a real residence, dispatch emergency services, or replace a qualified professional.

## The operating idea

AGEWELL CITY treats daily life as a coordinated system.

The resident stays at the center. Around that person are the home, mobility, caregivers, assisted living services, community resources, building infrastructure, health access, and city services.

Each part has different data and different authority. The system should not collapse all of those boundaries into one large AI agent.

The architecture therefore uses specialist agents and a shared control plane.

```text
Resident preferences and consent
        |
        v
F36 AgeWell Control Plane
        |
        +--> F59 Caregiver Support
        +--> Home Environment Agent
        +--> Accessible Mobility Agent
        +--> Assisted Living Agent
        +--> Community Services Agent
        +--> Consent and Privacy Agent
        |
        v
F37 Evaluation + F09 Safety
        |
        v
Policy and Tool Gateway
        |
        +--> read only data
        +--> bounded support actions
        +--> protected human authority
        |
        v
Evidence and event history
```

## What the control plane does

F36 is the coordination layer. It receives the operating goal, resident preferences, consent state, current environment, service constraints, and unresolved blockers.

It does not become the caregiver, clinician, building manager, transportation provider, or resident.

Its job is to break the situation into smaller tasks, route those tasks to the right specialists, keep one shared state, expose conflicts, and decide whether the next step is eligible for a bounded support action or requires a person.

## The specialist agents

### F59 Caregiver Support

F59 turns authorized observations, routines, caregiver concerns, and support resources into a structured brief. It can help organize what is happening and what needs attention. It does not issue treatment instructions or replace clinical judgment.

### Home Environment Agent

The Home Environment Agent works with approved environmental state such as temperature, sensor freshness, and resident comfort presets. It can support small reversible actions in the simulation. If evidence becomes stale, the runtime is designed to stop relying on it.

### Accessible Mobility Agent

The Mobility Agent plans accessible routes, checks transport availability, and coordinates timing. It is not a tracking or enforcement system.

### Assisted Living Agent

The Assisted Living Agent coordinates nonclinical support, facility routes, staff requests, shared resources, and resident preferences. Care plans, medication, diagnosis, and resident rights remain outside its autonomous authority.

### Community Services Agent

The Community Services Agent works with age friendly public and community resources. It can find cooling spaces, community services, and accessible options using aggregate or consent based information.

### Consent and Privacy Agent

The Consent and Privacy Agent applies purpose, role, and minimum necessary access. Another agent cannot silently expand consent just because a task is urgent.

### F37 Evaluation and F09 Safety

These systems challenge the combined plan. They look for weak evidence, unsafe permissions, privacy overreach, unsupported clinical conclusions, and protected actions.

A high evaluation score does not cancel a hard blocker.

## Authority classes

The public runtime uses four authority classes.

### READ_ONLY

The system may inspect approved synthetic state.

Examples include reading the home environment or checking consent.

### ANALYSIS

The system may calculate or plan without changing state.

Examples include planning an accessible route.

### BOUNDED_AUTONOMY

The system may perform a small reversible synthetic action inside an approved envelope.

Examples include requesting an accessible shuttle, asking for a resident preferred check in, notifying an authorized care circle contact, or applying a resident approved comfort preset.

### PROTECTED

The runtime must deny autonomous execution.

Protected actions in the public demo include medication changes, emergency dispatch, consent override, lock override, and unrestricted identity tracking.

## Three public scenarios

### Independent living

A synthetic resident misses a usual morning check in during a hot day. The home is warmer than the resident preferred range and the mobility pattern is slower than usual.

The system does not diagnose anything.

It coordinates a gentle wellness check, a resident approved comfort adjustment, accessible transport options, and an authorized care circle notification.

The main design point is that a change in routine can justify support without becoming a medical conclusion.

### Assisted living

One elevator becomes unavailable while several residents need accessible movement and one resident has an external appointment.

The agents coordinate facility routes, support requests, and transport options.

They do not change a care plan or make a clinical decision.

### Age friendly district heat response

A synthetic neighborhood experiences extreme heat. Cooling access, transport, home comfort, and community check ins all become more important at the same time.

The response uses aggregate demand plus consent based household support. Continuous identity tracking is not part of the operating model.

## Failure handling

The public runtime includes secondary faults because a useful system must show what happens when the evidence gets worse after a plan has already started.

The independent living scenario can lose fresh home sensor evidence.

The assisted living scenario can lose accessible transport availability.

The district scenario can reach cooling center capacity.

In each case the runtime moves to human review rather than pretending that the original plan is still valid.

## The human centered rule set

AGEWELL CITY is built around six rules.

1. Consent before sensing.
2. Support without surveillance.
3. Human relationships remain real.
4. Clinical authority stays clinical.
5. Accessibility is infrastructure.
6. Independence is a measurable outcome.

These are not marketing statements. They change what tools exist, what information agents can use, what actions are protected, and when the runtime must stop.

## What success should mean

A mature AGEWELL CITY pilot should not be judged only by model accuracy.

Useful measures include resident choice, response time, accessible transport reliability, maintenance response, caregiver coordination, false alarms, stale data detected, unsafe actions blocked, resident participation in community life, and time that people are able to live in the setting they prefer.

## Production direction

A real implementation would replace the synthetic browser adapters with authenticated connectors and durable services.

A practical production shape would include:

```text
Resident and Operator Interfaces
        |
        v
Authenticated AgeWell API
        |
        v
F36 Orchestration + Durable Shared State
        |
        +--> specialist model services where useful
        +--> deterministic policy and safety logic
        +--> consent and role service
        +--> digital building and community state
        |
        v
Policy and Tool Gateway
        |
        +--> home and building systems
        +--> transport and shuttle systems
        +--> staff and caregiver communication
        +--> community services
        +--> optional wearables with explicit consent
        |
        v
Append only event and evidence store
```

The first real deployment should begin read only wherever possible. The team should prove data quality, identity boundaries, consent, and operator usefulness before introducing automated actions.

## What this public flagship is not

It is not a medical device.

It is not a diagnostic system.

It is not an emergency dispatch system.

It is not a surveillance platform.

It is not a replacement for caregivers, clinicians, family, staff, or residents themselves.

It is an executable design study for a human centered multi-agent coordination layer that could support independent living, assisted living, and age friendly communities.