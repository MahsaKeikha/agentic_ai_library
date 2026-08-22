# Multi-Agent Benchmark Standard

A reference multi-agent system should be evaluated as a system, not only as a collection of individual model responses.

## Evaluation layers

### 1. Agent-level correctness
Measure whether each specialized agent produces the artifact its role requires, uses supplied evidence correctly, exposes unknowns, and stays within its authority.

### 2. Coordination quality
Measure whether agents receive the right context, hand off useful artifacts, avoid duplicated work, surface disagreements, and preserve traceability across transitions.

### 3. Evidence integrity
Measure provenance completeness, unsupported-claim rate, conflict detection, citation/grounding behavior where relevant, and whether missing evidence remains explicitly missing.

### 4. Gate integrity
Test whether unresolved blockers prevent progression even when an approval flag is supplied. Consequential gates must fail closed in reference workflows.

### 5. Robustness
Test malformed inputs, missing fields, contradictory evidence, stale evidence, prompt injection embedded in case data, repeated execution, partial agent failure, and unexpected tool/provider errors.

### 6. Domain performance
Each F-system must define domain-specific metrics. A universal benchmark cannot substitute for clinical, legal, financial, robotics, educational, scientific, software, or other domain evaluation.

### 7. Reproducibility
Offline fixtures should yield deterministic structural results. Provider-backed examples should record model/provider/configuration metadata and should not be used as the sole acceptance criterion.

### 8. Cost and latency
When external models or tools are enabled, measure end-to-end latency, calls per run, token/tool consumption where observable, and failure/retry behavior.

## Minimum benchmark report

A release benchmark should identify:

- repository and F-number
- release version and commit
- evaluation dataset/fixtures
- execution mode (offline or provider-backed)
- configuration
- metrics and definitions
- pass/fail thresholds
- known limitations
- failed/adversarial cases
- date of evaluation

## Cross-library metrics

The umbrella project may report comparable engineering metrics across systems, including:

- evidence completeness rate
- unsupported-claim rate
- blocker bypass rate
- conflict-detection rate
- deterministic test pass rate
- workflow completion rate
- trace completeness
- reproducibility status

These metrics are engineering signals, not proof that a system is safe or effective in real-world deployment.

## Benchmark integrity

Do not tune hidden test cases into demonstrations, discard failed cases without reporting them, or claim superiority without a documented comparison protocol. External benchmark contributions should be welcomed when their methodology and licensing allow reproduction.
