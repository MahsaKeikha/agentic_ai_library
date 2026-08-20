"""Offline-first multi-agent workflows for F31-F40.

These are deterministic reference implementations. They deliberately surface missing
inputs instead of fabricating evidence and require explicit human approval before
consequential release/deployment actions.
"""
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
    "F31": ("Agentic ML Engineer", ["requirements", "data", "features", "model", "evaluation", "risk"]),
    "F32": ("Agentic MLOps Team", ["release", "pipeline", "registry", "deployment", "observability", "rollback"]),
    "F33": ("Agentic Data Engineering", ["sources", "schema", "pipeline", "quality", "lineage", "reliability"]),
    "F34": ("Agentic Prompt Engineering", ["task", "prompt", "tests", "evaluation", "red_team", "version"]),
    "F35": ("Agentic RAG Engineering", ["corpus", "chunking", "retrieval", "ranking", "grounding", "safety"]),
    "F36": ("Agentic Multi-Agent Orchestrator", ["routing", "planning", "registry", "state", "conflicts", "gate"]),
    "F37": ("Agentic LLM Evaluator", ["evaluation_design", "dataset", "judges", "bias", "safety", "report"]),
    "F38": ("Agentic AI Benchmark Suite", ["benchmark", "dataset_validation", "runner", "metrics", "reproducibility", "report"]),
    "F39": ("Agentic AI Product Manager", ["problem", "users", "requirements", "priorities", "risk", "launch"]),
    "F40": ("Agentic AI Infrastructure Architect", ["workload", "gateway", "compute", "reliability", "security", "cost"]),
}


def _value(case: Dict[str, Any], key: str) -> Any:
    value = case.get(key)
    return value if value not in (None, "", [], {}) else "Unknown / evidence required"


def run_system(system_id: str, case: Dict[str, Any], approve: bool = False) -> WorkflowResult:
    if system_id not in SYSTEMS:
        raise ValueError(f"Unknown system: {system_id}")
    name, roles = SYSTEMS[system_id]
    result = WorkflowResult(system_id=system_id, system_name=name)

    for role in roles:
        result.analyses[role] = {
            "input": _value(case, role),
            "agent": role,
            "evidence_status": "supplied" if case.get(role) not in (None, "", [], {}) else "missing",
        }

    missing = [role for role in roles if result.analyses[role]["evidence_status"] == "missing"]
    if missing:
        result.risks.append("Missing evidence for: " + ", ".join(missing))
        result.recommendation = "Resolve material evidence gaps before consequential action."
    else:
        result.recommendation = "Proceed to expert review and system-specific evaluation gate."

    if approve:
        result.status = "HUMAN APPROVAL RECORDED - ELIGIBLE FOR NEXT CONTROLLED STEP"
    return result
