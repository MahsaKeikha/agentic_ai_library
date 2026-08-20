"""Deterministic offline reference workflows for F161-F170 Personal and Productivity."""
from dataclasses import dataclass, field
from typing import Any, Dict, List


@dataclass
class PersonalResult:
    system_id: str
    system_name: str
    analyses: Dict[str, Any] = field(default_factory=dict)
    risks: List[str] = field(default_factory=list)
    recommendation: str = ""
    status: str = "DRAFT - HUMAN REVIEW REQUIRED"


SYSTEMS = {
    "F161": ("Agentic Life Planner", ["goals", "constraints", "values", "options", "risks", "commitments"]),
    "F162": ("Agentic Personal Knowledge Manager", ["capture", "organization", "retrieval", "synthesis", "sources", "archive"]),
    "F163": ("Agentic Career Coach", ["strengths", "roles", "skills_gap", "opportunities", "networking", "decision"]),
    "F164": ("Agentic Resume Studio", ["evidence", "resume", "ats", "achievements", "consistency", "submission"]),
    "F165": ("Agentic Public Speaking Coach", ["audience", "story", "speech", "delivery", "qa", "rehearsal"]),
    "F166": ("Agentic Interview Coach", ["role", "questions", "evidence", "mock", "feedback", "preparation"]),
    "F167": ("Agentic Language Tutor", ["level", "lesson", "vocabulary", "conversation", "feedback", "progress"]),
    "F168": ("Agentic Productivity Coach", ["workload", "priorities", "calendar", "focus", "review", "boundaries"]),
    "F169": ("Agentic Travel Planner", ["preferences", "itinerary", "logistics", "budget", "risk", "booking"]),
    "F170": ("Agentic Habit Builder", ["goal", "triggers", "routine", "friction", "progress", "adjustment"]),
}


def run_system(system_id: str, case: Dict[str, Any], approve: bool = False) -> PersonalResult:
    if system_id not in SYSTEMS:
        raise ValueError(f"Unknown system: {system_id}")

    name, roles = SYSTEMS[system_id]
    result = PersonalResult(system_id=system_id, system_name=name)

    for role in roles:
        supplied = case.get(role) not in (None, "", [], {})
        result.analyses[role] = {
            "agent": role,
            "input": case.get(role) if supplied else "Unknown / user context required",
            "evidence_status": "supplied" if supplied else "missing",
        }

    missing = [r for r in roles if result.analyses[r]["evidence_status"] == "missing"]
    if missing:
        result.risks.append("Missing user context for: " + ", ".join(missing))

    if case.get("high_stakes_decision"):
        result.risks.append("High-stakes decision requires appropriate qualified human review")

    if case.get("external_action_requested"):
        result.risks.append("External action requires explicit user authorization")

    result.recommendation = (
        "Clarify missing context and resolve open risks before external or irreversible action."
        if result.risks else
        "Proceed with the plan as a user-reviewed draft and record adjustments over time."
    )

    if approve and not result.risks:
        result.status = "HUMAN REVIEW RECORDED - ELIGIBLE FOR NEXT USER-CONTROLLED STEP"
    elif approve:
        result.status = "APPROVAL REQUESTED BUT BLOCKED BY OPEN RISKS"

    return result
