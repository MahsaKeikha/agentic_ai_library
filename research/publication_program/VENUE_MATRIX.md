# Venue and Submission Matrix

Updated: 2026-09-19

This matrix is operational, not a promise of acceptance. Final submission decisions depend on completed results, venue fit, page limits, originality review, and the state of each manuscript at the deadline.

| Paper | Primary venue | Why it fits | Submission posture |
|---|---|---|---|
| J01 | IEEE Transactions on Automatic Control | Formal control-theoretic guarantees for runtime supervision, compositional safety, and liveness | Target only after theorem/proof package is strong enough for a controls audience |
| J02 | Automatica | Event-triggered oversight as a control problem with risk and intervention-load analysis | Develop after C03 establishes compact core result |
| J03 | IEEE Transactions on Control Systems Technology | Receding-horizon orchestration with practical cost/latency/risk constraints | Requires realistic systems experiments, not only abstract theory |
| J04 | IEEE Transactions on Automation Science and Engineering | Evidence freshness, provenance, workflow automation, deterministic fallback | Strong fit if evaluated as automation methodology across multiple workflows |
| J05 | IEEE Transactions on Systems, Man, and Cybernetics: Systems | Graph observability, diagnosability, multi-agent decision systems | Requires formal systems analysis plus broad experiments |
| J06 | IEEE Transactions on Human-Machine Systems | Human oversight, workload, escalation, intervention timing | Human-subject claims require approved study; simulation-only version must be labeled accordingly |
| J07 | IEEE Transactions on Artificial Intelligence | Agentic delegation, authority allocation, uncertainty-aware tool use | Needs comparison against current agent-safety/delegation baselines |
| J08 | Autonomous Agents and Multi-Agent Systems | Correlated failures, orchestration, coordination, resilience | Natural journal home for expanded C02 line |
| J09 | IEEE Transactions on Industrial Informatics | Agentic control planes, digital twins, industrial CPS, safe tooling | Requires industrially credible fault-injection and recovery evaluation |
| J10 | Artificial Intelligence | General decision-theoretic model for act/ask/abstain/escalate | Highest burden on conceptual novelty and broad validation |
| C01 | American Control Conference 2027 | Supervisory control of discrete protected-action task graphs | Deadline 2026-09-25; submit only if a complete, finished result is achieved and validated |
| C02 | AAMAS 2027 | Correlated/common-mode failures in agent teams and recovery benchmarking | Abstract 2026-10-01; paper 2026-10-08; current strongest near-term agentic-AI target |
| C03 | IEEE CDC | Event-triggered human intervention and takeover | Build as a compact control-theoretic result for a later cycle |
| C04 | Future AAAI/ICLR cycle | Evidence-aware delegation for tool-using generative agents | Do not force into a closed/near-closed 2027 cycle |
| C05 | IEEE CASE / later ICRA-aligned cycle | Agentic digital twins and industrial automation with human supervision | Develop after industrial testbed is mature |

## Near-term decision

ACC 2027 requires a complete description of finished work. Because the regular-paper deadline is 2026-09-25, C01 is a high-risk deadline and must not be submitted with invented, preliminary, or unverified results.

AAMAS 2027 is the more realistic immediate target for a new agentic-AI contribution. Its Generative and Agentic AI area explicitly includes orchestration, runtime support, failure handling, resilience, human-agent delegation, controllability, assurance, verification, safety, benchmarks, and evaluation.

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
