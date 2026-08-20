"""Deterministic offline reference workflows for F101-F110.

These systems support legal/compliance process organization only. They do not provide
legal advice or make binding legal or regulatory determinations.
"""
from dataclasses import dataclass, field
from typing import Any, Dict, List


@dataclass
class LegalComplianceResult:
    system_id: str
    system_name: str
    analyses: Dict[str, Any] = field(default_factory=dict)
    issues: List[str] = field(default_factory=list)
    recommendation: str = ""
    status: str = "DRAFT - PROFESSIONAL REVIEW REQUIRED"


SYSTEMS = {
    "F101": ("Agentic Contract Review", ["intake", "clauses", "risk", "obligations", "deviations", "counsel_gate"]),
    "F102": ("Agentic Corporate Compliance", ["obligations", "policies", "controls", "evidence", "gaps", "compliance_gate"]),
    "F103": ("Agentic Privacy Compliance", ["data_map", "purpose", "notice_consent", "retention", "risk", "privacy_gate"]),
    "F104": ("Agentic Intellectual Property", ["assets", "ownership", "portfolio", "risk", "evidence", "counsel_gate"]),
    "F105": ("Agentic Patent Research", ["query", "prior_art", "classification", "evidence", "claim_mapping", "patent_gate"]),
    "F106": ("Agentic Employment Compliance", ["policy", "jurisdiction", "process", "documentation", "risk", "hr_counsel_gate"]),
    "F107": ("Agentic International Trade", ["transaction", "jurisdiction", "counterparty", "documentation", "risk", "trade_gate"]),
    "F108": ("Agentic Export Control", ["item_technology", "classification", "end_use", "counterparty", "evidence", "export_gate"]),
    "F109": ("Agentic Healthcare Compliance", ["requirements", "policy", "documentation", "privacy_security", "gaps", "compliance_gate"]),
    "F110": ("Agentic Regulatory Affairs", ["requirements", "submission_plan", "evidence", "change_control", "gaps", "regulatory_gate"]),
}


def _supplied(case: Dict[str, Any], key: str) -> bool:
    return case.get(key) not in (None, "", [], {})


def run_system(system_id: str, case: Dict[str, Any], approve: bool = False) -> LegalComplianceResult:
    if system_id not in SYSTEMS:
        raise ValueError(f"Unknown system: {system_id}")

    name, roles = SYSTEMS[system_id]
    result = LegalComplianceResult(system_id=system_id, system_name=name)

    jurisdiction = case.get("jurisdiction")
    if jurisdiction in (None, "", [], {}):
        result.issues.append("Jurisdiction or governing context is missing")

    for role in roles:
        supplied = _supplied(case, role)
        result.analyses[role] = {
            "agent": role,
            "input": case.get(role) if supplied else "Unknown / evidence required",
            "evidence_status": "supplied" if supplied else "missing",
        }

    missing = [r for r in roles if result.analyses[r]["evidence_status"] == "missing"]
    if missing:
        result.issues.append("Missing evidence/context for: " + ", ".join(missing))

    if case.get("binding_action_requested"):
        result.issues.append("Binding legal/regulatory action requested; autonomous action blocked")

    if result.issues:
        result.recommendation = "Resolve context/evidence gaps and route to qualified legal/compliance review."
    else:
        result.recommendation = "Package is ready for qualified professional review; no legal conclusion is implied."

    if approve and not result.issues:
        result.status = "PROFESSIONAL REVIEW RECORDED - READY FOR NEXT CONTROLLED STEP"
    elif approve:
        result.status = "APPROVAL REQUESTED BUT BLOCKED BY OPEN ISSUES"

    return result
