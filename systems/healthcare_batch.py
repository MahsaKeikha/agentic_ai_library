"""Offline-first healthcare workflow references for F51-F60.

These systems support organization, documentation, coordination, and research workflows.
They do not diagnose, prescribe, authorize treatment, or replace qualified clinicians.
"""
from dataclasses import dataclass, field
from typing import Any, Dict, List


@dataclass
class HealthcareResult:
    system_id: str
    system_name: str
    analyses: Dict[str, Any] = field(default_factory=dict)
    escalations: List[str] = field(default_factory=list)
    recommendation: str = ""
    status: str = "DRAFT - QUALIFIED HUMAN REVIEW REQUIRED"


SYSTEMS = {
    "F51": ("Agentic Digital Health Assistant", ["intake", "data_quality", "care_plan", "education", "risk_escalation"]),
    "F52": ("Agentic Clinical Trial Manager", ["protocol", "sites", "recruitment", "data_quality", "deviations", "reporting"]),
    "F53": ("Agentic Medical Device Development", ["requirements", "risk_management", "systems", "verification", "human_factors", "regulatory_docs"]),
    "F54": ("Agentic FDA Documentation", ["document_intake", "requirements_mapping", "evidence_gaps", "traceability", "review", "submission_gate"]),
    "F55": ("Agentic Hospital Operations", ["capacity", "flow", "staffing", "quality", "safety_escalation", "briefing"]),
    "F56": ("Agentic Radiology Workflow", ["worklist", "metadata", "prior_studies", "reporting_completeness", "safety_escalation", "human_review"]),
    "F57": ("Agentic Pathology Review", ["specimen_workflow", "metadata", "case_completeness", "quality", "escalation", "human_review"]),
    "F58": ("Agentic Nursing Assistant", ["tasks", "documentation", "education", "handoff", "escalation", "human_gate"]),
    "F59": ("Agentic Caregiver Support", ["routine", "observations", "resources", "communication", "escalation", "human_gate"]),
    "F60": ("Agentic Rehabilitation Planning", ["goals", "sessions", "progress", "equipment_environment", "escalation", "human_review"]),
}


def _present(case: Dict[str, Any], key: str) -> bool:
    return case.get(key) not in (None, "", [], {})


def run_system(system_id: str, case: Dict[str, Any], approve: bool = False) -> HealthcareResult:
    if system_id not in SYSTEMS:
        raise ValueError(f"Unknown healthcare system: {system_id}")

    name, roles = SYSTEMS[system_id]
    result = HealthcareResult(system_id=system_id, system_name=name)

    for role in roles:
        supplied = _present(case, role)
        result.analyses[role] = {
            "input": case.get(role) if supplied else "Unknown / evidence required",
            "evidence_status": "supplied" if supplied else "missing",
            "agent": role,
        }

    missing = [role for role in roles if result.analyses[role]["evidence_status"] == "missing"]
    if missing:
        result.escalations.append("Missing or incomplete information: " + ", ".join(missing))

    if case.get("urgent_safety_concern") is True:
        result.escalations.append(
            "Urgent safety concern flagged: route to the organization's qualified clinical/emergency process; do not rely on this system for triage."
        )

    result.recommendation = (
        "Route the draft to the designated qualified human reviewer. Do not use this output as a diagnosis, prescription, treatment authorization, or compliance certification."
    )

    if approve:
        result.status = "QUALIFIED HUMAN REVIEW RECORDED - ELIGIBLE FOR NEXT CONTROLLED WORKFLOW STEP"

    return result
