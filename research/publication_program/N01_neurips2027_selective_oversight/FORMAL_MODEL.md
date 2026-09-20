# Formal Model
## Risk-Calibrated Selective Oversight

## 1. Sequential agent interaction

An episode is a trajectory

    z = (s_1, a_1, o_1, ..., s_T, a_T, o_T)

where s_t is the auditable agent state, a_t is a proposed tool action, and o_t is the resulting observation when the action executes.

A hard authority predicate

    H(s_t, a_t) in {0,1}

indicates whether the action is eligible for autonomous execution at all.

If H(s_t,a_t)=0, the learned controller cannot authorize the action.

## 2. Learned risk score

For actions that pass the hard authority layer, a risk model estimates

    r_t = r_phi(s_t,a_t) in [0,1].

Candidate features include:
- proposed tool identity and arguments;
- action reversibility;
- authority class;
- evidence completeness and age;
- provenance quality;
- model confidence;
- cross-agent disagreement;
- critic disagreement;
- state inconsistency;
- prompt-injection indicators;
- distance to a protected action;
- prior failures in the same trajectory.

The risk score is not assumed to be perfectly calibrated.

## 3. Selective oversight policy

For threshold tau,

    pi_tau(s_t,a_t) =
        ASK,      if H(s_t,a_t)=0 and a reviewer is available
        ABSTAIN,  if H(s_t,a_t)=0 and no reviewer is available
        ACT,      if H(s_t,a_t)=1 and r_t <= tau
        ASK,      if H(s_t,a_t)=1 and r_t > tau and a reviewer is available
        ABSTAIN,  otherwise.

Human review may approve, reject, or edit a proposed action.

## 4. Episode-level safety event

Let Y_i(tau)=1 when calibration episode i contains at least one unsafe action that pi_tau executes autonomously, and zero otherwise.

Define

    R(tau) = P(Y(tau)=1).

This is deliberately an episode-level quantity. Actions within an agent trajectory can be dependent. The independent sampling unit used by the first certificate is the episode, not the individual tool call.

## 5. Finite candidate set

Let Theta={tau_1,...,tau_M} be a threshold grid fixed before observing calibration outcomes.

For n independent calibration episodes,

    Rhat(tau) = (1/n) sum_i Y_i(tau).

Define

    U(tau) = min(1, Rhat(tau) + sqrt(log(M/delta)/(2n))).

By Hoeffding's inequality and a union bound,

    P(for all tau in Theta: R(tau) <= U(tau)) >= 1-delta.

Therefore selecting

    tau_star = argmax_tau Coverage(tau)
               subject to U(tau) <= alpha

gives

    P(R(tau_star) <= alpha) >= 1-delta

under the stated sampling assumptions.

This theorem is a direct application of standard concentration results. Novelty must not be claimed for Hoeffding's inequality or the union bound.

## 6. Review-budget formulation

Let C_review(tau) be the expected fraction of actions sent to review and C_abstain(tau) the expected fraction abstained.

A deployment can study the Pareto frontier among

    residual episode risk,
    task utility,
    review load,
    abstention.

A later method may solve

    maximize Utility(tau)
    subject to R(tau) <= alpha
               C_review(tau) <= beta.

The first implementation focuses on the risk constraint and reports the review load that results.

## 7. Reviewer imperfections

The main safety certificate concerns unsafe autonomous execution. It does not assume that every human decision is correct.

A separate experiment should model reviewer error and delay. If a reviewed action can still be approved incorrectly, report:
- autonomous risk;
- post-review residual risk;
- reviewer error rate;
- delay cost;
- abstention caused by reviewer unavailability.

Do not merge these quantities into one metric.

## 8. Research extensions

Potential stronger results:
- empirical-Bernstein or betting-based certificates;
- distribution shift detection;
- adaptive thresholds under changing review capacity;
- subgroup or action-class risk constraints;
- conformal risk control;
- online recalibration;
- counterfactual value-of-review estimation;
- multi-agent risk aggregation;
- intervention policies learned under explicit review cost.

Each extension requires a separate proof and empirical validation.
