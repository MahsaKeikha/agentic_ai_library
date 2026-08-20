"""Deterministic offline reference workflows for F91-F100 Education.

These systems support educators, learners, committees, and institutions. They do not
replace instructor judgment, academic due process, or institutional approval.
"""
from dataclasses import dataclass, field
from typing import Any, Dict, List


@dataclass
class EducationResult:
    system_id: str
    system_name: str
    analyses: Dict[str, Any] = field(default_factory=dict)
    risks: List[str] = field(default_factory=list)
    recommendation: str = ""
    status: str = "DRAFT - HUMAN REVIEW REQUIRED"


SYSTEMS = {
    "F91": ("Agentic Professor Assistant", ["course", "lecture", "examples", "assessment", "accessibility", "publish"]),
    "F92": ("Agentic Curriculum Builder", ["standards", "outcomes", "sequence", "assessment", "inclusion", "approval"]),
    "F93": ("Agentic Student Tutor", ["learner_context", "explanation", "practice", "hints", "mastery", "escalation"]),
    "F94": ("Agentic Exam Generator", ["blueprint", "questions", "difficulty", "bias", "answer_key", "release"]),
    "F95": ("Agentic STEM Laboratory Planner", ["objectives", "procedure", "equipment", "safety", "assessment", "instructor_gate"]),
    "F96": ("Agentic University Research Office", ["intake", "funding", "compliance", "timeline", "budget", "submission"]),
    "F97": ("Agentic Academic Integrity Checker", ["evidence", "similarity", "citations", "context", "due_process", "human_decision"]),
    "F98": ("Agentic Grant Writer", ["opportunity", "narrative", "evidence", "budget_narrative", "compliance", "submission"]),
    "F99": ("Agentic Thesis Committee", ["scope", "methods", "literature", "analysis", "reproducibility", "committee_gate"]),
    "F100": ("Agentic Accreditation Manager", ["standards", "evidence", "gaps", "outcomes", "actions", "institutional_gate"]),
}


def _supplied(case: Dict[str, Any], key: str) -> bool:
    return case.get(key) not in (None, "", [], {})


def run_system(system_id: str, case: Dict[str, Any], approve: bool = False) -> EducationResult:
    if system_id not in SYSTEMS:
        raise ValueError(f"Unknown system: {system_id}")
    name, roles = SYSTEMS[system_id]
    result = EducationResult(system_id=system_id, system_name=name)

    for role in roles:
        supplied = _supplied(case, role)
        result.analyses[role] = {
            "agent": role,
            "input": case.get(role) if supplied else "Unknown / evidence required",
            "evidence_status": "supplied" if supplied else "missing",
        }

    missing = [r for r in roles if result.analyses[r]["evidence_status"] == "missing"]
    if missing:
        result.risks.append("Missing education evidence/context for: " + ", ".join(missing))

    if system_id == "F97" and case.get("automatic_misconduct_finding"):
        result.risks.append("Automatic misconduct finding is prohibited; human due process required")

    if system_id == "F95" and case.get("unresolved_lab_safety_issue"):
        result.risks.append("Unresolved laboratory safety issue")
        result.recommendation = "STOP. Instructor/safety review is required before lab use."
        return result

    result.recommendation = (
        "Resolve evidence gaps before publication, submission, grading, or institutional action."
        if result.risks else
        "Proceed to instructor, committee, or institutional review as applicable."
    )

    if approve and not result.risks:
        result.status = "HUMAN REVIEW RECORDED - ELIGIBLE FOR NEXT CONTROLLED STEP"
    elif approve:
        result.status = "APPROVAL REQUESTED BUT BLOCKED BY OPEN RISKS"
    return result
