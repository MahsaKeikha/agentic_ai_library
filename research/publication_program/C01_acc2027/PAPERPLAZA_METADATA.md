# PaperPlaza metadata

## Title
Anticipatory Supervisory Control of Protected Actions in Tool-Using Multi-Agent AI

## Author
Mahsa Keikha

## Affiliation
Connected Care LLC, California, USA

## Abstract
Tool-using AI agents can obey a pointwise authorization rule and still enter workflow states from which later authority revocation, evidence expiry, or other uncontrollable changes leave no safe path to completion. This paper formulates that failure as a discrete-event control problem. We introduce an Authority and Evidence Task Automaton in which agent and tool choices are controllable events, authority and evidence invalidations are uncontrollable events, protected-action violations are forbidden states, and both successful completion and explicit human review are marked outcomes. An Authority and Evidence Supervisory Controller, AESC, computes the largest safe, uncontrollable-closed, nonblocking state set and disables only controllable transitions that leave it. We define precursor vulnerability as behavior admitted by an immediate-action gate but excluded from the synthesized winning set, and show that a pointwise gate is sufficient exactly when its reachable state set is contained in that winning set. Four synthetic Atlas-derived workflow abstractions were evaluated with 100,000 seeded rollouts per controller and case. Immediate-action gating removed direct protected-action violations but produced 6.26 percent to 10.53 percent deadlocked runs after invalidation. AESC produced zero modeled violations and zero deadlocks in the same abstractions while retaining safe completion or human review. Independent brute-force verification found zero winning-set mismatches on 5,000 random automata. Median synthesis time was 22.3 ms at 2,000 states. These results establish a finite-state engineering method for moving agent safety control upstream from the final commit boundary to the earliest controllable precursor that can create an unrecoverable authority or evidence exposure.

## Suggested keywords
Supervisory control; discrete-event systems; agentic AI; multi-agent systems; runtime safety; human-in-the-loop control; tool-using agents.

## Submission category
Contributed paper.

## Primary subject positioning
Safety and resilience; learning-enabled and autonomous systems; human-centered systems; multi-agent systems.

## Submission facts
- ACC 2027 regular manuscript deadline: September 25, 2026.
- Initial contributed-paper limit: 8 pages.
- PDF only, maximum 2 MB.
- Standard two-column ACC format through PaperPlaza.
- LLM use is disclosed and cited in the manuscript as required by ACC policy.

## Claim boundary
All experiments are synthetic finite-state studies. No clinical, infrastructure, production, or real-world deployment safety claim is made.

## Final form checks before submit
- Add the corresponding email only if desired and consistent with the PaperPlaza account.
- Run the final PDF through PaperPlaza PDF Test.
- Choose the final topic codes from the live ACC form.
- Confirm there are no additional coauthors before upload.
