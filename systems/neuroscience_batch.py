"""Offline-first reference workflows for F61-F70 neuroscience systems.

These workflows support research, monitoring, documentation, and planning. They do
not diagnose disease, prescribe treatment, or replace qualified clinical judgment.
"""
from dataclasses import dataclass, field
from typing import Any, Dict, List


@dataclass
class NeuroWorkflowResult:
    system_id: str
    system_name: str
    analyses: Dict[str, Any] = field(default_factory=dict)
    uncertainties: List[str] = field(default_factory=list)
    escalations: List[str] = field(default_factory=list)
    recommendation: str = ""
    status: str = "DRAFT - QUALIFIED HUMAN REVIEW REQUIRED"


SYSTEMS = {
    "F61": ("Agentic Parkinson Research", ["literature", "biomarkers", "trials", "digital_phenotyping", "evidence", "research_plan"]),
    "F62": ("Agentic Dementia Care Planning", ["needs", "routine", "safety", "caregiver_support", "escalation", "care_plan"]),
    "F63": ("Agentic Hallucination Monitoring", ["observations", "context", "patterns", "safety", "caregiver_brief", "evidence"]),
    "F64": ("Agentic EEG Analysis", ["data_quality", "preprocessing", "features", "artifacts", "statistics", "report"]),
    "F65": ("Agentic Sleep Research", ["protocol", "signals", "sleep_metrics", "confounders", "literature", "report"]),
    "F66": ("Agentic Neurotechnology Design", ["user_needs", "sensors", "signal_pipeline", "human_factors", "safety", "verification"]),
    "F67": ("Agentic Brain Computer Interface", ["signals", "decoder", "calibration", "human_factors", "safety", "evaluation"]),
    "F68": ("Agentic Cognitive Assessment", ["assessment", "data_quality", "scoring_support", "bias", "longitudinal", "human_review"]),
    "F69": ("Agentic Aging Research", ["literature", "cohort", "biomarkers", "intervention_evidence", "statistics", "research_plan"]),
    "F70": ("Agentic Biomarker Discovery", ["data", "candidates", "statistics", "replication", "confounders", "evidence_gate"]),
}


def _present(case: Dict[str, Any], key: str) -> bool:
    return case.get(key) not in (None, "", [], {})


def run_system(system_id: str, case: Dict[str, Any], approve: bool = False) -> NeuroWorkflowResult:
    if system_id not in SYSTEMS:
        raise ValueError(f"Unknown system: {system_id}")

    name, roles = SYSTEMS[system_id]
    result = NeuroWorkflowResult(system_id=system_id, system_name=name)

    for role in roles:
        supplied = _present(case, role)
        result.analyses[role] = {
            "agent": role,
            "input": case.get(role) if supplied else "Unknown / evidence required",
            "evidence_status": "supplied" if supplied else "missing",
        }
        if not supplied:
            result.uncertainties.append(f"Missing evidence for {role}")

    if case.get("urgent_safety_signal"):
        result.escalations.append(
            "Urgent safety signal supplied: escalate to the appropriate qualified human or emergency pathway; do not interpret autonomously."
        )

    if result.escalations:
        result.recommendation = "Prioritize human safety escalation before further automated analysis."
    elif result.uncertainties:
        result.recommendation = "Resolve material evidence gaps before clinical, participant, device, or research decisions."
    else:
        result.recommendation = "Proceed to domain-expert review and the system-specific evaluation gate."

    if approve:
        result.status = "QUALIFIED HUMAN REVIEW RECORDED - ELIGIBLE FOR NEXT CONTROLLED STEP"

    return result
