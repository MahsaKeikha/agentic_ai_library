"""Deterministic offline reference workflows for F151-F160 Finance and Risk."""
from dataclasses import dataclass, field
from typing import Any, Dict, List


@dataclass
class FinanceRiskResult:
    system_id: str
    system_name: str
    analyses: Dict[str, Any] = field(default_factory=dict)
    risks: List[str] = field(default_factory=list)
    recommendation: str = ""
    status: str = "DRAFT - AUTHORIZED HUMAN REVIEW REQUIRED"


SYSTEMS = {
    "F151": ("Agentic Investment Research", ["thesis", "financials", "industry", "valuation", "risk", "evidence"]),
    "F152": ("Agentic Portfolio Manager", ["allocation", "exposure", "scenarios", "risk", "constraints", "rebalance"]),
    "F153": ("Agentic Quantitative Trading Research", ["data", "signal", "backtest", "bias_leakage", "risk", "research_gate"]),
    "F154": ("Agentic Insurance Operations", ["intake", "coverage_workflow", "claims_triage", "fraud_risk", "compliance", "decision_gate"]),
    "F155": ("Agentic Banking Assistant", ["service", "product_info", "transaction_review", "fraud_escalation", "compliance", "human_gate"]),
    "F156": ("Agentic Tax Planning", ["facts", "jurisdiction", "scenarios", "documentation", "risk", "professional_review"]),
    "F157": ("Agentic Enterprise Risk Manager", ["identify", "quantify", "controls", "scenarios", "aggregate", "executive_gate"]),
    "F158": ("Agentic Treasury Operations", ["cash", "liquidity", "forecast", "counterparty", "controls", "payment_gate"]),
    "F159": ("Agentic Credit Analyst", ["borrower", "financials", "cash_flow", "structure", "risk", "credit_committee"]),
    "F160": ("Agentic ESG Reporting", ["boundary", "data_quality", "metrics", "disclosure", "assurance", "publication_gate"]),
}


def run_system(system_id: str, case: Dict[str, Any], approve: bool = False) -> FinanceRiskResult:
    if system_id not in SYSTEMS:
        raise ValueError(f"Unknown system: {system_id}")
    name, roles = SYSTEMS[system_id]
    result = FinanceRiskResult(system_id=system_id, system_name=name)

    for role in roles:
        supplied = case.get(role) not in (None, "", [], {})
        result.analyses[role] = {
            "agent": role,
            "input": case.get(role) if supplied else "Unknown / evidence required",
            "evidence_status": "supplied" if supplied else "missing",
        }

    missing = [r for r in roles if result.analyses[r]["evidence_status"] == "missing"]
    if missing:
        result.risks.append("Missing finance/risk evidence for: " + ", ".join(missing))

    if case.get("unverified_material_claim"):
        result.risks.append("Material financial claim remains unverified")
    if case.get("binding_action_requested"):
        result.risks.append("Binding financial action requested but reference workflow is analysis-only")

    result.recommendation = (
        "Resolve evidence gaps and obtain authorized professional review before any binding financial action."
        if result.risks else
        "Proceed to authorized human review and organization-specific policy/compliance controls."
    )

    if approve and not result.risks:
        result.status = "AUTHORIZED HUMAN REVIEW RECORDED - ELIGIBLE FOR NEXT CONTROLLED STEP"
    elif approve:
        result.status = "APPROVAL REQUESTED BUT BLOCKED BY OPEN RISKS"
    return result
