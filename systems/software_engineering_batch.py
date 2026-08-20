"""Offline-first workflows for F41-F50 software engineering systems."""
from dataclasses import dataclass, field
from typing import Any, Dict, List


@dataclass
class WorkflowResult:
    system_id: str
    system_name: str
    analyses: Dict[str, Any] = field(default_factory=dict)
    risks: List[str] = field(default_factory=list)
    recommendation: str = ""
    status: str = "DRAFT - HUMAN REVIEW REQUIRED"


SYSTEMS = {
    "F41": ("Agentic Mobile App Engineering", ["product", "architecture", "ux", "api", "testing", "release"]),
    "F42": ("Agentic Cloud Architecture", ["requirements", "cloud", "network", "reliability", "security", "cost"]),
    "F43": ("Agentic DevOps", ["build", "cicd", "environment", "reliability", "security", "release"]),
    "F44": ("Agentic Kubernetes Operations", ["cluster", "workloads", "policy", "observability", "reliability", "change"]),
    "F45": ("Agentic Cybersecurity SOC", ["alerts", "logs", "incident", "containment", "evidence", "escalation"]),
    "F46": ("Agentic Penetration Testing", ["authorization", "scope", "surface", "tests", "evidence", "remediation"]),
    "F47": ("Agentic API Engineering", ["contract", "schema", "security", "integration", "reliability", "documentation"]),
    "F48": ("Agentic Database Architecture", ["workload", "model", "queries", "reliability", "security", "migration"]),
    "F49": ("Agentic Embedded Systems", ["requirements", "architecture", "firmware", "interfaces", "testing", "safety"]),
    "F50": ("Agentic IoT Engineering", ["devices", "connectivity", "edge", "cloud", "security", "fleet"]),
}


def _normalize(value: Any) -> Any:
    return value if value not in (None, "", [], {}) else "Unknown / evidence required"


def run_system(system_id: str, case: Dict[str, Any], approve: bool = False) -> WorkflowResult:
    if system_id not in SYSTEMS:
        raise ValueError(f"Unknown system: {system_id}")
    name, roles = SYSTEMS[system_id]
    result = WorkflowResult(system_id=system_id, system_name=name)

    for role in roles:
        value = case.get(role)
        result.analyses[role] = {
            "agent": role,
            "input": _normalize(value),
            "evidence_status": "supplied" if value not in (None, "", [], {}) else "missing",
        }

    missing = [r for r in roles if result.analyses[r]["evidence_status"] == "missing"]
    if missing:
        result.risks.append("Missing evidence for: " + ", ".join(missing))
        result.recommendation = "Resolve evidence gaps before implementation or deployment."
    else:
        result.recommendation = "Proceed to expert review and system-specific validation."

    if system_id == "F46" and _normalize(case.get("authorization")) == "Unknown / evidence required":
        result.risks.append("No explicit authorization evidence supplied; do not perform security testing.")
        result.recommendation = "Stop until written authorization and scope are verified."

    if approve:
        result.status = "HUMAN APPROVAL RECORDED - ELIGIBLE FOR NEXT CONTROLLED STEP"
    return result
