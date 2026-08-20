"""Deterministic offline reference workflows for F141-F150 Government and Public Sector.

These systems support planning, policy, public information, resilience, and governance.
They do not exercise public authority, conduct operational surveillance, or issue tactical commands.
"""
from dataclasses import dataclass, field
from typing import Any, Dict, List


@dataclass
class PublicSectorResult:
    system_id: str
    system_name: str
    analyses: Dict[str, Any] = field(default_factory=dict)
    risks: List[str] = field(default_factory=list)
    recommendation: str = ""
    status: str = "DRAFT - AUTHORIZED HUMAN REVIEW REQUIRED"


SYSTEMS = {
    "F141": ("Agentic Smart City Planner", ["needs", "infrastructure", "mobility", "accessibility", "data_governance", "public_value"]),
    "F142": ("Agentic Emergency Management", ["situation", "resources", "communications", "vulnerability", "coordination", "decision_gate"]),
    "F143": ("Agentic Disaster Response", ["impact", "logistics", "shelter_services", "equity", "recovery", "coordination_gate"]),
    "F144": ("Agentic Public Health Planner", ["population_needs", "program", "data_quality", "equity", "communications", "public_health_review"]),
    "F145": ("Agentic Transportation Planner", ["demand", "network", "safety", "accessibility", "environment", "investment"]),
    "F146": ("Agentic Environmental Compliance", ["requirements", "evidence", "monitoring", "impact", "corrective_action", "compliance_review"]),
    "F147": ("Agentic Defense Policy Analyst", ["policy", "capability", "budget", "governance", "risk", "civilian_oversight"]),
    "F148": ("Agentic Public-Sector Intelligence Analyst", ["sources", "evidence", "alternatives", "confidence", "bias", "oversight"]),
    "F149": ("Agentic Election Information Reviewer", ["sources", "process", "misinformation", "neutrality", "accessibility", "publication"]),
    "F150": ("Agentic Policy Analyst", ["problem", "evidence", "stakeholders", "options", "impact", "decision_memo"]),
}


BLOCKING_FLAGS = {
    "individual_targeting_requested": "Individual targeting is outside this reference system.",
    "operational_surveillance_requested": "Operational surveillance is outside this reference system.",
    "tactical_military_action_requested": "Tactical military planning or action is outside this reference system.",
    "voter_persuasion_requested": "Targeted voter persuasion is outside this neutral election-information workflow.",
    "binding_public_decision_requested": "Binding public-authority decisions require authorized officials and applicable process.",
}


def run_system(system_id: str, case: Dict[str, Any], approve: bool = False) -> PublicSectorResult:
    if system_id not in SYSTEMS:
        raise ValueError(f"Unknown system: {system_id}")

    name, roles = SYSTEMS[system_id]
    result = PublicSectorResult(system_id=system_id, system_name=name)

    for role in roles:
        supplied = case.get(role) not in (None, "", [], {})
        result.analyses[role] = {
            "agent": role,
            "input": case.get(role) if supplied else "Unknown / evidence required",
            "evidence_status": "supplied" if supplied else "missing",
        }

    missing = [r for r in roles if result.analyses[r]["evidence_status"] == "missing"]
    if missing:
        result.risks.append("Missing public-sector evidence/context for: " + ", ".join(missing))

    for flag, message in BLOCKING_FLAGS.items():
        if case.get(flag):
            result.risks.append(message)

    if case.get("privacy_review_failed"):
        result.risks.append("Privacy review is unresolved")
    if case.get("source_provenance_incomplete"):
        result.risks.append("Source provenance is incomplete")
    if system_id == "F149" and case.get("partisan_positioning"):
        result.risks.append("Election-information workflow requires neutral process information")

    if result.risks:
        result.recommendation = "Resolve evidence, rights, governance, neutrality, and oversight risks before official use or publication."
    else:
        result.recommendation = "Proceed to authorized human review, applicable public process, and domain-specific validation."

    if approve and not result.risks:
        result.status = "AUTHORIZED HUMAN REVIEW RECORDED - ELIGIBLE FOR NEXT CONTROLLED PUBLIC-SECTOR STEP"
    elif approve:
        result.status = "APPROVAL REQUESTED BUT BLOCKED BY OPEN RISKS"

    return result
