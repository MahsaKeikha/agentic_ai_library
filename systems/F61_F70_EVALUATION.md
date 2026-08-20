# F61-F70 Evaluation Framework

These neuroscience systems are evaluated as research and decision-support workflows, not autonomous clinical systems.

## Common evaluation criteria

- Evidence provenance is preserved and material unknowns remain explicit.
- No system converts an observation or score into a diagnosis.
- Urgent safety signals trigger escalation rather than autonomous interpretation.
- Human review status is separate from evidence completeness.
- Outputs clearly distinguish supplied facts, derived summaries, uncertainties, and recommendations.
- Production deployments include privacy controls, access control, audit logs, data retention policies, and model/version provenance.

## System-specific focus

| ID | Evaluation focus |
|---|---|
| F61 | literature quality, trial evidence coverage, biomarker evidence strength, reproducibility |
| F62 | care-plan completeness, safety escalation, caregiver usability, uncertainty handling |
| F63 | observation fidelity, context capture, false-alarm handling, escalation sensitivity |
| F64 | signal quality, preprocessing traceability, artifact handling, statistical validity |
| F65 | protocol adherence, signal completeness, confounder handling, metric reproducibility |
| F66 | user needs traceability, sensor rationale, verification coverage, human factors and safety |
| F67 | calibration quality, decoding evaluation, usability, safety, repeatability |
| F68 | assessment completeness, scoring traceability, bias review, longitudinal consistency |
| F69 | cohort definition, confounder control, intervention evidence quality, statistical validity |
| F70 | candidate provenance, multiple-testing control, replication readiness, confounder coverage |

## Red-team cases

Test incomplete records, contradictory observations, noisy sensor data, missing timestamps, demographic bias, stale evidence, prompt-like instructions embedded in source material, outlier-heavy datasets, uncertain labels, and attempts to bypass the qualified-human review gate.
