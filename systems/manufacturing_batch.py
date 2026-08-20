"""Deterministic offline reference workflows for F111-F120 Manufacturing."""
from dataclasses import dataclass, field
from typing import Any, Dict, List


@dataclass
class ManufacturingResult:
    system_id: str
    system_name: str
    analyses: Dict[str, Any] = field(default_factory=dict)
    risks: List[str] = field(default_factory=list)
    recommendation: str = ""
    status: str = "DRAFT - AUTHORIZED HUMAN REVIEW REQUIRED"


SYSTEMS = {
    "F111": ("Agentic Manufacturing Engineer", ["process", "equipment", "quality", "safety", "cost", "change"]),
    "F112": ("Agentic Production Planner", ["demand", "capacity", "schedule", "constraints", "inventory", "plan"]),
    "F113": ("Agentic Quality Engineer", ["requirements", "inspection", "spc", "nonconformance", "capa", "release"]),
    "F114": ("Agentic Predictive Maintenance", ["assets", "condition", "failure_modes", "maintenance", "reliability", "work_order"]),
    "F115": ("Agentic Supply Chain Planner", ["demand", "suppliers", "inventory", "logistics", "risk", "sourcing"]),
    "F116": ("Agentic Lean Manufacturing", ["value_stream", "waste", "flow", "kaizen", "metrics", "change"]),
    "F117": ("Agentic Digital Twin Engineer", ["model", "interfaces", "calibration", "simulation", "validation", "deployment"]),
    "F118": ("Agentic Factory Automation", ["requirements", "controls", "integration", "safety", "verification", "commissioning"]),
    "F119": ("Agentic Industrial Safety", ["hazards", "risk", "controls", "procedures", "training", "approval"]),
    "F120": ("Agentic Sustainability Engineer", ["resources", "energy", "waste_emissions", "lifecycle", "economics", "improvement"]),
}


def run_system(system_id: str, case: Dict[str, Any], approve: bool = False) -> ManufacturingResult:
    if system_id not in SYSTEMS:
        raise ValueError(f"Unknown system: {system_id}")
    name, roles = SYSTEMS[system_id]
    result = ManufacturingResult(system_id=system_id, system_name=name)

    for role in roles:
        supplied = case.get(role) not in (None, "", [], {})
        result.analyses[role] = {
            "agent": role,
            "input": case.get(role) if supplied else "Unknown / evidence required",
            "evidence_status": "supplied" if supplied else "missing",
        }

    missing = [r for r in roles if result.analyses[r]["evidence_status"] == "missing"]
    if missing:
        result.risks.append("Missing manufacturing evidence for: " + ", ".join(missing))

    if case.get("unresolved_safety_hazard"):
        result.risks.append("Unresolved industrial safety hazard")
        result.recommendation = "STOP. Resolve and verify the hazard before equipment or process change."
        return result

    if case.get("quality_hold"):
        result.risks.append("Quality hold remains open")

    result.recommendation = (
        "Resolve open evidence, safety, and quality risks before production change or release."
        if result.risks else
        "Proceed to site-specific verification and authorized engineering/operations review."
    )

    if approve and not result.risks:
        result.status = "AUTHORIZED HUMAN REVIEW RECORDED - ELIGIBLE FOR NEXT CONTROLLED STEP"
    elif approve:
        result.status = "APPROVAL REQUESTED BUT BLOCKED BY OPEN RISKS"
    return result
