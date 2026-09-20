# Formal Model Notebook for J01/C01

## 1. Agentic closed loop

Let the agentic system consist of an advanced decision layer A, a verified supervisory layer S, a tool/environment layer P, and a human authority channel H.

At decision index k,

x_{k+1} = f(x_k, u_k, w_k)

where x_k is the auditable system state, u_k is the executed action after supervision, and w_k contains exogenous events such as tool failure, evidence expiration, delayed approval, or state desynchronization.

The advanced agent team proposes

u^A_k ~ pi_A(. | o_k, m_k)

where the policy may be stochastic, model-dependent, and not formally verified.

The supervisor executes

u_k = S(x_k, u^A_k).

The safety argument must depend on S and the modeled transition semantics, not on assuming pi_A is correct.

## 2. State decomposition

Use

x_k = (q_k, e_k, a_k, z_k, h_k, b_k)

with:
- q_k: workflow/task state;
- e_k: evidence ledger state;
- a_k: authority/credential state;
- z_k: tool and environment state;
- h_k: human review state;
- b_k: blockers, hazards, and unresolved conflicts.

For each evidence item j define a timestamp tau_j and freshness horizon Delta_j. At time t_k,

fresh_j(k) = 1[t_k - tau_j <= Delta_j].

For a proposed action u define ReqE(u) as its required evidence set and ReqA(u) as its required authority predicate.

Evidence admissibility is

E_ok(x_k,u) = AND_{j in ReqE(u)} fresh_j(k) AND complete_j(k).

Authority admissibility is

A_ok(x_k,u) = ReqA(u)(a_k) = true.

## 3. Action classes

Partition candidate actions into:
- U_read
- U_analysis
- U_bounded
- U_protected

A protected action may execute only if both evidence and authority predicates hold and no hard blocker is active.

Define

adm(x,u) = policy_ok(x,u) AND E_ok(x,u) AND A_ok(x,u) AND not hard_blocker(x,u).

## 4. Supervisor

A minimal supervisor is

S(x,uA) =
  EXECUTE(uA), if adm(x,uA)
  SAFE_FALLBACK(x), if not adm(x,uA) and a certified fallback exists
  HUMAN_REVIEW, if review is reachable/authorized
  ABSTAIN, otherwise.

For the controls contribution, this rule must be strengthened into a predictive or language-based supervisor that prevents transitions into states from which a future protected-action violation becomes unavoidable.

## 5. Authority-safe set

Define K as the set of states for which:
- no unauthorized protected action has occurred;
- every active evidence-dependent commitment is backed by fresh/complete evidence;
- effective tool permissions are a subset of delegated permissions;
- hard blockers remain visible and unresolved blockers have not been relabeled as success;
- an authorized safe continuation, fallback, review, or terminal abstention remains available according to the modeled assumptions.

## 6. Discrete-event specialization for C01

Construct G = (X,Sigma,delta,x0,Xm), with event partition Sigma_c and Sigma_uc.

For each protected event sigma_p define guard

g_p(x) = E_ok(x,sigma_p) AND A_ok(x,sigma_p) AND not hard_blocker(x,sigma_p).

The protected-action specification disables sigma_p whenever g_p(x)=0.

Evidence expiration is modeled as an uncontrollable event sigma_expire. Authority revocation may also be uncontrollable from the supervisor's perspective.

The target is a controlled language that is safe, controllable with respect to uncontrollable events, and nonblocking relative to accepted completion plus explicit human-review marked states.

## 7. Compositional extension for J01

For subsystem i use an assume-guarantee contract C_i=(Assume_i,Guarantee_i).

Local safety alone is insufficient when shared tools, shared evidence, or cross-agent authority dependencies exist. J01 should derive compatibility conditions under which

AND_i Guarantee_i  => K_global

for all interleavings permitted by the orchestration semantics.

Candidate coupling variables:
- shared evidence freshness;
- shared tool lock/permission;
- cross-agent approval token;
- unresolved conflict state;
- human reviewer availability;
- asynchronous message age.

## 8. Verification checklist

Before any theorem is promoted from candidate to established:
- define transition semantics without ambiguity;
- specify trusted computing base;
- state assumptions on uncontrollable events;
- prove invariance or language safety;
- prove/qualify nonblocking;
- construct counterexamples when assumptions fail;
- model-check finite abstractions;
- test randomized fault traces;
- compare with hand-coded guards and ungoverned execution.

## 9. Claim boundary

This notebook is a research specification. It contains definitions and proof targets, not completed proofs or experimental results.
