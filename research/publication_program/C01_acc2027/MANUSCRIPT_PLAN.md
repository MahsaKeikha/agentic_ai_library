# C01 Research Plan
## Supervisory Control of Protected Actions in Agentic Task Graphs

### Intended venue
American Control Conference 2027, contributed paper.

### Scope discipline
This conference paper is intentionally narrower than J01. It focuses on discrete-event supervisory control of protected actions in an agentic task graph. It does not claim the full compositional runtime-assurance theory planned for J01.

### Research question
Given a finite task graph generated or traversed by an agent team, can a deterministic supervisor disable unsafe or unauthorized transitions while preserving the maximally permissive portion of behavior that still reaches either a legitimate task completion or a defined human-review state?

### Formal model
Let
- G = (X, Sigma, delta, x0, Xm) be a deterministic task automaton,
- Sigma = Sigma_c union Sigma_uc be controllable and uncontrollable events,
- P subset Sigma be protected action events,
- H subset X be human-review states,
- E(x) encode evidence validity/freshness,
- A(x, sigma) encode authority for event sigma in state x.

Define a forbidden-state predicate F(x) that becomes true when a protected action has executed without the required authority/evidence conditions, or when a hard blocker has been bypassed.

The supervisor V restricts enabled controllable events such that:
1. forbidden states are unreachable;
2. uncontrollable unsafe reachability is detected as a blocking condition;
3. where a legal completion or human-review route exists, the supervisor seeks a nonblocking sublanguage;
4. protected actions are enabled only when their guard predicates are satisfied.

### Candidate control contribution
Construct a protected-action specification automaton and compute the supremal controllable nonblocking sublanguage of the composed task/specification model. Extend the specification with evidence-freshness expiration events and an explicit human-review transition.

The paper's potential new element is not standard supervisory control theory itself. The contribution must be the formal mapping of agentic task execution into a controllable event model in which protected actions, evidence expiry, and human review are first-class events/states, followed by an experimentally validated supervisor for heterogeneous agentic workflows.

### Proof obligations
P1. Safety: every trace admitted by the supervisor satisfies the protected-action authorization invariant.

P2. Nonblocking: if the synthesized controlled language is nonempty and the modeled human-review transition is reachable when required, every reachable controlled state can reach an accepted terminal or review state.

P3. Monotonic authority restriction: removing an authority credential cannot introduce a newly enabled protected trace.

P4. Evidence-expiry response: after a freshness-expiry event, any transition requiring that evidence remains disabled until refresh or authorized review.

These are research obligations and must not be written as established theorems before the formal derivation and model checks are complete.

### Experimental systems
Use small formal abstractions of at least three existing Atlas workflows:
- software/release or tool orchestration
- industrial digital-twin/factory workflow
- AGEWELL CITY or Smart City protected-action workflow

Each abstraction should expose:
- nominal task path
- protected events
- evidence-expiry event
- authority grant/revoke event
- human-review state
- at least one uncontrollable fault/event

### Baselines
- no supervisor
- prompt-only instruction
- hand-coded guard rules
- synthesized supervisory controller

### Metrics
- forbidden traces admitted
- task completion
- percentage of controllable behavior preserved
- deadlock/blocking states
- unnecessary human escalations
- supervisor synthesis/runtime overhead
- response to authority revocation
- response to evidence expiry

### Deadline gate
ACC 2027 regular papers are due 2026-09-25 and must describe finished work. Submit C01 in this cycle only if the formal models, synthesis, experiments, plots, manuscript, and independent self-checks are complete before the deadline. Otherwise retain C01 as a finished research asset and send it to the next appropriate controls venue rather than weakening the work.

### Relationship to J01
C01: finite-state/discrete-event protected-action supervisory control, compact experiments.

J01: broader heterogeneous agentic runtime-assurance architecture, compositional contracts, state/evidence/authority dynamics, asynchronous composition, safe degradation, stronger proof package, larger benchmark.

Any journal manuscript derived from this lineage must cite C01 if C01 becomes archival and explicitly identify the substantial extensions.
