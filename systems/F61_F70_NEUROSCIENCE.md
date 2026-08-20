# F61 to F70: Neuroscience Systems

This batch extends the unified Agentic AI Library with neuroscience research and planning workflows. These systems are designed for research, monitoring, documentation, analysis, and decision support. They do not diagnose disease or replace licensed clinical judgment.

| ID | System | Core multi-agent roles | Primary output |
|---|---|---|---|
| F61 | Agentic Parkinson Research | Literature Analyst, Biomarker Analyst, Trial Analyst, Digital Phenotyping Agent, Evidence Reviewer, Research Planner | Parkinson research brief and evidence map |
| F62 | Agentic Dementia Care Planning | Needs Analyst, Routine Planner, Safety Reviewer, Caregiver Support Agent, Escalation Agent, Plan Writer | Human-reviewed care planning package |
| F63 | Agentic Hallucination Monitoring | Signal Intake Agent, Context Analyst, Pattern Analyst, Safety Escalation Agent, Caregiver Briefing Agent, Evidence Reviewer | Observation summary and escalation package |
| F64 | Agentic EEG Analysis | Data Quality Agent, Preprocessing Planner, Feature Analyst, Artifact Reviewer, Statistical Reviewer, Report Writer | EEG analysis plan and findings summary |
| F65 | Agentic Sleep Research | Protocol Analyst, Signal Analyst, Sleep Metrics Agent, Confounder Reviewer, Literature Agent, Report Writer | Sleep research analysis package |
| F66 | Agentic Neurotechnology Design | User Needs Agent, Sensor Architect, Signal Pipeline Agent, Human Factors Agent, Safety Reviewer, Verification Planner | Neurotechnology design package |
| F67 | Agentic Brain Computer Interface | Signal Analyst, Decoder Designer, Calibration Agent, Human Factors Agent, Safety Reviewer, Evaluation Agent | BCI design and evaluation plan |
| F68 | Agentic Cognitive Assessment | Assessment Planner, Data Quality Agent, Scoring Support Agent, Bias Reviewer, Longitudinal Analyst, Human Review Gate | Assessment support summary, not diagnosis |
| F69 | Agentic Aging Research | Literature Analyst, Cohort Analyst, Biomarker Agent, Intervention Evidence Reviewer, Statistics Agent, Research Planner | Aging research evidence and study plan |
| F70 | Agentic Biomarker Discovery | Data Curator, Candidate Generator, Statistical Analyst, Replication Reviewer, Confounder Agent, Evidence Gatekeeper | Biomarker candidate evidence package |

## Shared safety and engineering contract

1. Research and decision-support scope only.
2. No diagnosis, treatment prescription, or autonomous clinical action.
3. Missing or uncertain evidence must remain explicit.
4. Potential urgent safety signals must be escalated to a qualified human rather than interpreted autonomously.
5. Clinical, participant, caregiver, and research data should be treated as sensitive and minimized in production deployments.
6. Human review is required before any output is used in care, trial, participant, or device decisions.
7. Every production implementation should add provenance, audit logs, access control, validation, version tracking, and organization-specific policies.

Status: **In development on `feature/unified-f61-f70`**.
