"""Deterministic offline science decision-support workflows for F81-F90."""
from dataclasses import dataclass, field
from typing import Any, Dict, List


@dataclass
class ScienceResult:
    system_id: str
    system_name: str
    analyses: Dict[str, Any] = field(default_factory=dict)
    risks: List[str] = field(default_factory=list)
    recommendation: str = ""
    status: str = "DRAFT - HUMAN REVIEW REQUIRED"


SYSTEMS = {
    "F81": ("Agentic Physics Research Assistant", ["problem", "literature", "model", "math", "experiment", "critique"]),
    "F82": ("Agentic Quantum Computing", ["algorithm", "circuit", "hardware", "error", "benchmark", "critique"]),
    "F83": ("Agentic Materials Science", ["requirements", "literature", "properties", "candidates", "validation", "risk"]),
    "F84": ("Agentic Chemistry Planning", ["question", "literature", "properties", "simulation", "safety", "evidence"]),
    "F85": ("Agentic Climate Science", ["dataset", "model", "scenario", "uncertainty", "validation", "report"]),
    "F86": ("Agentic Space Mission Design", ["mission", "systems", "trajectory", "payload", "risk", "verification"]),
    "F87": ("Agentic Astronomy Research", ["observation", "catalog", "signal", "model", "uncertainty", "publication"]),
    "F88": ("Agentic Energy Systems", ["demand", "generation", "storage", "grid", "economics", "reliability"]),
    "F89": ("Agentic Nuclear Engineering", ["requirements", "systems", "safety", "verification", "regulatory", "human_gate"]),
    "F90": ("Agentic Scientific Literature Review", ["search", "screening", "extraction", "synthesis", "bias", "citations"]),
}


def run_system(system_id: str, case: Dict[str, Any], approve: bool = False) -> ScienceResult:
    if system_id not in SYSTEMS:
        raise ValueError(f"Unknown system: {system_id}")
    name, roles = SYSTEMS[system_id]
    result = ScienceResult(system_id=system_id, system_name=name)

    for role in roles:
        supplied = case.get(role) not in (None, "", [], {})
        result.analyses[role] = {
            "agent": role,
            "input": case.get(role) if supplied else "Unknown / evidence required",
            "evidence_status": "supplied" if supplied else "missing",
        }

    missing = [r for r in roles if result.analyses[r]["evidence_status"] == "missing"]
    if missing:
        result.risks.append("Missing evidence for: " + ", ".join(missing))

    if case.get("hazardous_experimental_request"):
        result.risks.append("Hazardous experimental execution request is outside this reference workflow")
        result.recommendation = "Keep the workflow at literature, simulation, documentation, or qualified institutional review level."
        return result

    result.recommendation = (
        "Resolve evidence gaps and document assumptions before publication or experiment execution."
        if missing else
        "Proceed to expert review, reproducibility checks, and domain-specific validation."
    )

    if approve and not result.risks:
        result.status = "HUMAN REVIEW RECORDED - ELIGIBLE FOR NEXT CONTROLLED RESEARCH STEP"
    elif approve:
        result.status = "APPROVAL REQUESTED BUT BLOCKED BY OPEN RISKS"
    return result
