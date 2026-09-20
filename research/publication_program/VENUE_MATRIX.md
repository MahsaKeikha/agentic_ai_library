# Venue and Submission Matrix

Updated: 2026-09-19

This matrix is operational, not a promise of acceptance. Final submission decisions depend on completed results, venue fit, page limits, originality review, and the state of each manuscript at the deadline.

| Paper | Primary venue | Why it fits | Submission posture |
|---|---|---|---|
| J01 | IEEE Transactions on Automatic Control | Formal control-theoretic guarantees for compositional runtime supervision, dynamic authority, evidence state, and liveness | Develop only after C01 is submitted and frozen; journal version must add substantial new theory and validation beyond C01 |
| J02 | Automatica | Event-triggered oversight as a control problem with risk and intervention-load analysis | Develop after C03 establishes compact core result |
| J03 | IEEE Transactions on Control Systems Technology | Receding-horizon orchestration with practical cost/latency/risk constraints | Requires realistic systems experiments, not only abstract theory |
| J04 | IEEE Transactions on Automation Science and Engineering | Evidence freshness, provenance, workflow automation, deterministic fallback | Strong fit if evaluated as automation methodology across multiple workflows |
| J05 | IEEE Transactions on Systems, Man, and Cybernetics: Systems | Graph observability, diagnosability, multi-agent decision systems | Requires formal systems analysis plus broad experiments |
| J06 | IEEE Transactions on Human-Machine Systems | Human oversight, workload, escalation, intervention timing | Human-subject claims require approved study; simulation-only version must be labeled accordingly |
| J07 | IEEE Transactions on Artificial Intelligence | Agentic delegation, authority allocation, uncertainty-aware tool use | Needs comparison against current agent-safety/delegation baselines |
| J08 | Autonomous Agents and Multi-Agent Systems | Correlated failures, orchestration, coordination, resilience | Natural journal home for expanded C02 line |
| J09 | IEEE Transactions on Industrial Informatics | Agentic control planes, digital twins, industrial CPS, safe tooling | Requires industrially credible fault-injection and recovery evaluation |
| J10 | Artificial Intelligence | General decision-theoretic model for act/ask/abstain/escalate | Highest burden on conceptual novelty and broad validation |
| C01 | American Control Conference 2027 | Anticipatory supervisory control of protected actions using AETA, AESC, precursor vulnerability, exact reachability, and reproducible finite-state validation | First publication target for Research Family 1; freeze and submit before journal expansion |
| C02 | AAMAS 2027 | Correlated/common-mode failures in agent teams and recovery benchmarking | Abstract 2026-10-01; paper 2026-10-08; current strongest near-term agentic-AI target |
| C03 | IEEE CDC | Event-triggered human intervention and takeover | Build as a compact control-theoretic result for a later cycle |
| C04 | Future AAAI/ICLR cycle | Evidence-aware delegation for tool-using generative agents | Do not force into a closed/near-closed 2027 cycle |
| C05 | IEEE CASE / later ICRA-aligned cycle | Agentic digital twins and industrial automation with human supervision | Develop after industrial testbed is mature |

## Near-term decision

Research Family 1 follows a conference-first path.

C01 is the immediate submission target. Its purpose is to establish the compact control-theoretic result: AETA, AESC, precursor vulnerability, pointwise insufficiency, exact safe and nonblocking synthesis, and finite-state validation.

J01 is not a simultaneous duplicate submission. It begins only from the frozen C01 baseline and must add substantial new material such as compositional contracts, partial observation, asynchronous handoffs, dynamic authority grant and revocation, evidence-age dynamics, delayed human review, correlated failures, richer real-agent integrations, and expanded proofs.

Other conference and journal pairs should follow the same lineage discipline unless a venue explicitly supports a different journal-plus-conference presentation route.

## Submission package standard

Each submission folder should eventually contain:
- manuscript source
- rendered PDF
- anonymized variant if required
- supplementary material
- reproducibility README
- code commit/tag
- raw result manifest
- figure-generation scripts
- venue checklist
- overlap/prior-publication statement
- cover letter when the venue accepts or requires one
