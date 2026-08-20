"""Deterministic offline reference workflows for F131-F140 Creative and Media."""
from dataclasses import dataclass, field
from typing import Any, Dict, List


@dataclass
class CreativeResult:
    system_id: str
    system_name: str
    analyses: Dict[str, Any] = field(default_factory=dict)
    risks: List[str] = field(default_factory=list)
    recommendation: str = ""
    status: str = "DRAFT - HUMAN CREATIVE/RIGHTS REVIEW REQUIRED"


SYSTEMS = {
    "F131": ("Agentic Book Publishing", ["manuscript", "structure", "copy", "metadata", "production", "publish"]),
    "F132": ("Agentic Screenwriting Studio", ["story", "characters", "scenes", "dialogue", "continuity", "draft"]),
    "F133": ("Agentic Music Production", ["creative_direction", "arrangement", "production", "rights", "mix_qa", "release"]),
    "F134": ("Agentic Graphic Design", ["brief", "visual_direction", "layout", "accessibility", "brand_qa", "export"]),
    "F135": ("Agentic UX Design", ["research", "journey", "interaction", "accessibility", "usability", "handoff"]),
    "F136": ("Agentic Interior Design", ["brief", "space", "materials", "lighting", "budget", "client_approval"]),
    "F137": ("Agentic Fashion Design", ["brief", "collection", "materials", "fit_construction", "sustainability", "production"]),
    "F138": ("Agentic Architecture Studio", ["program", "concept", "systems", "code_accessibility", "cost", "design_gate"]),
    "F139": ("Agentic Game Design", ["vision", "systems", "narrative", "economy_balance", "playtest", "release"]),
    "F140": ("Agentic Animation Studio", ["storyboard", "assets", "layout", "motion", "production", "delivery"]),
}


def run_system(system_id: str, case: Dict[str, Any], approve: bool = False) -> CreativeResult:
    if system_id not in SYSTEMS:
        raise ValueError(f"Unknown system: {system_id}")
    name, roles = SYSTEMS[system_id]
    result = CreativeResult(system_id=system_id, system_name=name)

    for role in roles:
        supplied = case.get(role) not in (None, "", [], {})
        result.analyses[role] = {
            "agent": role,
            "input": case.get(role) if supplied else "Unknown / creative input required",
            "evidence_status": "supplied" if supplied else "missing",
        }

    missing = [r for r in roles if result.analyses[r]["evidence_status"] == "missing"]
    if missing:
        result.risks.append("Missing creative/production context for: " + ", ".join(missing))

    rights = case.get("rights_status", "unknown")
    if rights not in {"original", "licensed", "public_domain", "cleared"}:
        result.risks.append("Rights/provenance not cleared for release")

    if case.get("accessibility_blocker"):
        result.risks.append("Accessibility blocker remains unresolved")

    result.recommendation = (
        "Resolve creative, rights, and accessibility gaps before public or commercial release."
        if result.risks else
        "Proceed to human creative review and controlled release approval."
    )

    if approve and not result.risks:
        result.status = "HUMAN REVIEW RECORDED - ELIGIBLE FOR CONTROLLED RELEASE"
    elif approve:
        result.status = "APPROVAL REQUESTED BUT BLOCKED BY OPEN RISKS"
    return result
