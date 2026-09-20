# NeurIPS 2027 Research Program
## Act, Ask, or Abstain: Risk-Calibrated Human Oversight for Tool-Using AI Agents

## Research question

When should a tool-using AI agent act autonomously, when should it ask a person for review, and when should it abstain, if human attention is limited and the deployment requires an explicit bound on residual autonomous risk?

The paper studies selective autonomy as a safety problem rather than treating human approval as a fixed rule attached to a few tools.

## Core hypothesis

Static approval gates waste human attention on low-risk actions and can still miss risky behavior that falls outside a hand-written protected-action list. Pure confidence thresholds can also be misleading because agent trajectories are sequential and a single unsafe autonomous action may be enough to create an unacceptable episode.

The proposed method separates:

1. hard authority constraints that are never overridden by learning;
2. learned action-level risk scores;
3. an episode-level calibration layer that selects an autonomy threshold;
4. human review when risk exceeds that threshold;
5. abstention when review is required but unavailable.

## Proposed method

Working name: Risk-Calibrated Selective Oversight, RCSO.

For each candidate tool action a_t in trajectory state s_t, a risk model produces

    r_t = r(s_t, a_t) in [0,1].

A hard policy layer first removes actions that require nondelegable human authority.

For the remaining actions, a calibrated policy returns one of:

    ACT
    ASK
    ABSTAIN

The threshold is chosen on held-out calibration episodes to maximize autonomous coverage subject to a high-probability upper bound on the probability that an episode contains at least one unsafe autonomous action.

The first reference implementation uses a fixed threshold grid and a simultaneous Hoeffding certificate. The concentration inequality itself is not claimed as novel. The research contribution is its use as an episode-level selective-autonomy controller for sequential tool-using agents, together with the benchmark, risk signals, intervention protocol, and empirical analysis.

## Intended scientific contributions

1. A formal selective-autonomy problem for sequential tool-using AI agents with bounded human review.
2. An episode-level residual-risk certificate that does not assume independence among actions inside a trajectory.
3. A three-way intervention policy: act, ask, or abstain.
4. A benchmark protocol that measures safety and human-review burden jointly.
5. Evaluation under prompt injection, stale evidence, permission escalation, corrupted tool output, agent disagreement, and reviewer unavailability.
6. Risk-coverage and safety-review Pareto curves across multiple agent architectures and models.
7. Analysis of which risk signals actually predict when human intervention is useful.

## Main baselines

- never review;
- always review;
- static protected-action approval rules;
- action-risk threshold without calibration;
- model self-confidence threshold;
- LLM-as-judge safety gate;
- disagreement-based review;
- calibrated RCSO;
- RCSO ablations without authority, evidence, disagreement, or reversibility features.

## Primary metrics

- episode unsafe-autonomy rate;
- action unsafe-autonomy rate;
- task success;
- autonomous coverage;
- human review fraction;
- missed-escalation rate;
- unnecessary-review rate;
- intervention precision and recall;
- abstention rate;
- risk-coverage curve;
- task utility under a review budget;
- calibration error;
- time of intervention relative to the first harmful action.

## Evaluation environments

The evaluation should combine public agent benchmarks and Atlas-derived controlled environments.

Public candidates:
- AgentDojo for tool-using agents under prompt injection;
- AgentHarm for harmful multi-step agent behavior;
- WASP for realistic web-agent security;
- additional public tool-use environments selected after compatibility testing.

Atlas-derived controlled environments:
- F117 Digital Twin Engineer;
- AGEWELL CITY;
- Smart City Agentic AI;
- software and release orchestration.

Public benchmarks are important because the NeurIPS paper must not rely only on the author's own synthetic systems.

## Human-in-the-loop boundary

No human-subject performance claim will be made without an appropriate study protocol and ethics review when required.

The initial benchmark can use expert-defined correction labels and simulated reviewer availability to develop the method. A later human study may measure review time, fatigue, decision quality, and interface effects if it is approved and conducted properly.

## Venue

Primary target: NeurIPS 2027 Main Track, subject to the official 2027 call for papers when released.

Alternate target: NeurIPS Evaluations and Datasets Track if the final contribution is primarily an evaluation methodology and benchmark.

## Relationship to the ACC paper

This is not the ACC supervisory-control paper.

The ACC paper studies anticipatory supervisory synthesis over a finite-state task automaton.

This NeurIPS paper studies learned risk estimation, selective autonomy, finite-sample risk calibration, and allocation of scarce human attention in sequential tool-using agents.

The two papers may share high-level safety motivation, but their central research questions, methods, experiments, and primary figures must remain distinct.
