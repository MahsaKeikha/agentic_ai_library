"""Deterministic offline reference workflows for F121-F130 Marketing and Growth."""
from dataclasses import dataclass, field
from typing import Any, Dict, List


@dataclass
class MarketingResult:
    system_id: str
    system_name: str
    analyses: Dict[str, Any] = field(default_factory=dict)
    risks: List[str] = field(default_factory=list)
    recommendation: str = ""
    status: str = "DRAFT - AUTHORIZED HUMAN REVIEW REQUIRED"


SYSTEMS = {
    "F121": ("Agentic Brand Strategist", ["brand", "audience", "positioning", "messaging", "consistency", "approval"]),
    "F122": ("Agentic Content Marketing", ["topics", "content_plan", "draft", "seo", "facts", "publish"]),
    "F123": ("Agentic SEO Growth", ["keywords", "technical", "content_gaps", "internal_links", "metrics", "change"]),
    "F124": ("Agentic Social Media Manager", ["channels", "content_plan", "copy", "community_risk", "calendar", "publish"]),
    "F125": ("Agentic Lifecycle Marketing", ["journey", "segments", "messaging", "experiments", "metrics", "launch"]),
    "F126": ("Agentic Paid Acquisition", ["channels", "audience", "creative", "budget", "attribution", "spend"]),
    "F127": ("Agentic Product Marketing", ["market", "personas", "positioning", "launch", "sales_enablement", "release"]),
    "F128": ("Agentic PR and Communications", ["narrative", "media", "draft", "risk", "spokesperson", "release"]),
    "F129": ("Agentic Growth Experimentation", ["funnel", "hypothesis", "experiment", "statistics", "learning", "rollout"]),
    "F130": ("Agentic Customer Insights", ["research", "feedback", "interviews", "segments", "insights", "action"]),
}


def run_system(system_id: str, case: Dict[str, Any], approve: bool = False) -> MarketingResult:
    if system_id not in SYSTEMS:
        raise ValueError(f"Unknown system: {system_id}")
    name, roles = SYSTEMS[system_id]
    result = MarketingResult(system_id=system_id, system_name=name)

    for role in roles:
        supplied = case.get(role) not in (None, "", [], {})
        result.analyses[role] = {
            "agent": role,
            "input": case.get(role) if supplied else "Unknown / evidence required",
            "evidence_status": "supplied" if supplied else "missing",
        }

    missing = [r for r in roles if result.analyses[r]["evidence_status"] == "missing"]
    if missing:
        result.risks.append("Missing marketing evidence for: " + ", ".join(missing))

    if case.get("deceptive_claim"):
        result.risks.append("Potential deceptive or unsupported claim")
    if case.get("privacy_or_consent_issue"):
        result.risks.append("Privacy or consent issue remains unresolved")
    if case.get("unapproved_spend_change"):
        result.risks.append("Paid-spend change lacks authorization")

    result.recommendation = (
        "Resolve evidence, claim, privacy, consent, and authorization risks before public release or spend changes."
        if result.risks else
        "Proceed to channel-specific review and authorized human approval."
    )

    if approve and not result.risks:
        result.status = "AUTHORIZED HUMAN REVIEW RECORDED - ELIGIBLE FOR NEXT CONTROLLED STEP"
    elif approve:
        result.status = "APPROVAL REQUESTED BUT BLOCKED BY OPEN RISKS"
    return result
