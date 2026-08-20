"""Deterministic offline reference workflows for F71-F80 Robotics.

No workflow here controls a physical robot. Outputs are engineering review artifacts
that require qualified-human authorization before real-world deployment.
"""
from dataclasses import dataclass, field
from typing import Any, Dict, List


@dataclass
class RoboticsResult:
    system_id: str
    system_name: str
    analyses: Dict[str, Any] = field(default_factory=dict)
    risks: List[str] = field(default_factory=list)
    recommendation: str = ""
    status: str = "DRAFT - QUALIFIED HUMAN REVIEW REQUIRED"


SYSTEMS = {
    "F71": ("Agentic Industrial Robotics", ["cell", "motion", "integration", "safety", "reliability", "commissioning"]),
    "F72": ("Agentic Service Robotics", ["task", "interaction", "navigation", "perception", "safety", "deployment"]),
    "F73": ("Agentic Medical Robotics", ["clinical_workflow", "systems", "human_factors", "verification", "risk", "regulatory"]),
    "F74": ("Agentic Autonomous Vehicles", ["odd", "perception", "planning", "validation", "safety_case", "release"]),
    "F75": ("Agentic Drone Operations", ["mission", "airspace", "payload", "environment", "compliance", "go_no_go"]),
    "F76": ("Agentic Humanoid Robot Design", ["requirements", "mechanical", "controls", "perception_hri", "safety", "verification"]),
    "F77": ("Agentic Robot Safety Validation", ["hazards", "tests", "faults", "metrics", "evidence", "approval"]),
    "F78": ("Agentic Human-Robot Interaction", ["context", "interaction", "accessibility", "human_factors", "trust_safety", "study"]),
    "F79": ("Agentic Swarm Robotics", ["mission", "coordination", "communications", "resilience", "simulation", "safety"]),
    "F80": ("Agentic Robotics Ethics", ["stakeholders", "rights_impact", "bias", "safety_ethics", "governance", "decision_record"]),
}


def _present(case: Dict[str, Any], key: str) -> bool:
    return case.get(key) not in (None, "", [], {})


def run_system(system_id: str, case: Dict[str, Any], approve: bool = False) -> RoboticsResult:
    if system_id not in SYSTEMS:
        raise ValueError(f"Unknown system: {system_id}")
    name, roles = SYSTEMS[system_id]
    result = RoboticsResult(system_id=system_id, system_name=name)

    for role in roles:
        supplied = _present(case, role)
        result.analyses[role] = {
            "agent": role,
            "input": case.get(role) if supplied else "Unknown / evidence required",
            "evidence_status": "supplied" if supplied else "missing",
        }

    missing = [r for r in roles if result.analyses[r]["evidence_status"] == "missing"]
    if missing:
        result.risks.append("Missing engineering evidence for: " + ", ".join(missing))

    if case.get("unresolved_safety_hazard"):
        result.risks.append("Unresolved safety hazard: physical deployment blocked")
        result.recommendation = "STOP. Resolve and verify the safety hazard before any physical operation."
        return result

    result.recommendation = (
        "Resolve evidence gaps and complete domain-specific verification before physical deployment."
        if missing else
        "Proceed to domain-specific verification, validation, and qualified-human deployment review."
    )

    if approve and not result.risks:
        result.status = "QUALIFIED HUMAN REVIEW RECORDED - ELIGIBLE FOR NEXT CONTROLLED ENGINEERING STEP"
    elif approve:
        result.status = "APPROVAL REQUESTED BUT BLOCKED BY OPEN RISKS"
    return result
