"""Agentic AI Gold Standard enterprise readiness assessment engine.

Deterministic, evidence-first scoring for the 10-pillar framework.
No external dependencies are required.
"""
from __future__ import annotations

import json
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any

PILLARS = {
    "specialization": 10,
    "orchestration": 12,
    "deterministic_controls": 10,
    "memory_governance": 8,
    "evaluation": 15,
    "observability": 10,
    "safety_security_privacy": 12,
    "human_authority": 10,
    "provenance_auditability": 7,
    "lifecycle_governance": 6,
}

BANDS = (
    (90, "Gold Standard Candidate"),
    (75, "Production Candidate"),
    (60, "Managed"),
    (40, "Emerging"),
    (0, "Experimental"),
)

CRITICAL_BLOCKER_TYPES = {
    "uncontrolled_consequential_action",
    "missing_authorization_boundary",
    "critical_security_exposure",
    "fabricated_or_unverifiable_evidence",
    "sensitive_data_exposure",
    "no_fail_closed_behavior",
    "unbounded_external_side_effect",
    "no_incident_or_rollback_path",
}

PRIORITY_ORDER = {"P0": 0, "P1": 1, "P2": 2, "P3": 3}


@dataclass
class Finding:
    id: str
    pillar: str
    title: str
    evidence: str
    risk: str
    recommendation: str
    priority: str = "P2"
    blocker_type: str | None = None
    status: str = "open"

    @property
    def is_critical_blocker(self) -> bool:
        return self.priority == "P0" or self.blocker_type in CRITICAL_BLOCKER_TYPES


class AssessmentError(ValueError):
    pass


def _validate(data: dict[str, Any]) -> None:
    if not isinstance(data, dict):
        raise AssessmentError("assessment input must be a JSON object")
    if not str(data.get("organization", "")).strip():
        raise AssessmentError("organization is required")
    if not str(data.get("system", "")).strip():
        raise AssessmentError("system is required")
    scores = data.get("scores")
    if not isinstance(scores, dict):
        raise AssessmentError("scores must be an object keyed by Gold Standard pillar")
    missing = [p for p in PILLARS if p not in scores]
    extra = [p for p in scores if p not in PILLARS]
    if missing:
        raise AssessmentError(f"missing pillar scores: {', '.join(missing)}")
    if extra:
        raise AssessmentError(f"unknown pillar scores: {', '.join(extra)}")
    for pillar, value in scores.items():
        if not isinstance(value, (int, float)) or isinstance(value, bool):
            raise AssessmentError(f"score for {pillar} must be numeric")
        if value < 0 or value > 100:
            raise AssessmentError(f"score for {pillar} must be between 0 and 100")

    findings = data.get("findings", [])
    if not isinstance(findings, list):
        raise AssessmentError("findings must be a list")
    for item in findings:
        if not isinstance(item, dict):
            raise AssessmentError("each finding must be an object")
        if item.get("pillar") not in PILLARS:
            raise AssessmentError(f"finding has unknown pillar: {item.get('pillar')}")
        if item.get("priority", "P2") not in PRIORITY_ORDER:
            raise AssessmentError("finding priority must be P0, P1, P2, or P3")
        blocker = item.get("blocker_type")
        if blocker is not None and blocker not in CRITICAL_BLOCKER_TYPES:
            raise AssessmentError(f"unknown blocker_type: {blocker}")


def _band(score: int) -> str:
    for threshold, name in BANDS:
        if score >= threshold:
            return name
    return "Experimental"


def _weighted_score(scores: dict[str, float]) -> tuple[int, dict[str, float]]:
    contributions: dict[str, float] = {}
    total = 0.0
    for pillar, weight in PILLARS.items():
        contribution = scores[pillar] / 100 * weight
        contributions[pillar] = round(contribution, 2)
        total += contribution
    return round(total), contributions


def _evidence_completeness(data: dict[str, Any]) -> int:
    evidence = data.get("evidence", {})
    if not evidence:
        return 0
    expected = (
        "architecture",
        "agent_inventory",
        "tool_inventory",
        "permission_map",
        "memory_policy",
        "evaluation_results",
        "observability_traces",
        "security_review",
        "protected_actions",
        "incident_rollback",
    )
    present = sum(bool(evidence.get(key)) for key in expected)
    return round(present / len(expected) * 100)


def assess(data: dict[str, Any]) -> dict[str, Any]:
    _validate(data)
    score, contributions = _weighted_score(data["scores"])
    findings = [Finding(**item) for item in data.get("findings", [])]
    blockers = [f for f in findings if f.status == "open" and f.is_critical_blocker]
    band = _band(score)
    evidence_pct = _evidence_completeness(data)

    production_recommendation = "Proceed to controlled production review"
    if blockers:
        production_recommendation = "Not production-ready until P0 blockers are remediated and verified"
    elif score < 75:
        production_recommendation = "Continue supervised pilot and remediate maturity gaps before consequential production use"
    elif evidence_pct < 70:
        production_recommendation = "Conditional: maturity score is promising but evidence completeness is insufficient for production assurance"

    gold_candidate = score >= 90 and not blockers and evidence_pct >= 80
    if score >= 90 and not gold_candidate:
        band = "Production Candidate"

    sorted_findings = sorted(findings, key=lambda f: (PRIORITY_ORDER[f.priority], f.pillar, f.id))
    pillar_ranking = sorted(data["scores"].items(), key=lambda pair: pair[1])

    return {
        "framework": "Agentic AI Gold Standard v1.0",
        "organization": data["organization"],
        "system": data["system"],
        "assessment_date": data.get("assessment_date", "not specified"),
        "overall_score": score,
        "maturity_band": band,
        "gold_standard_candidate": gold_candidate,
        "evidence_completeness": evidence_pct,
        "production_recommendation": production_recommendation,
        "pillar_scores": data["scores"],
        "weighted_contributions": contributions,
        "strongest_pillars": [p for p, _ in sorted(data["scores"].items(), key=lambda pair: pair[1], reverse=True)[:3]],
        "weakest_pillars": [p for p, _ in pillar_ranking[:3]],
        "critical_blockers": [asdict(f) for f in blockers],
        "findings": [asdict(f) | {"critical_blocker": f.is_critical_blocker} for f in sorted_findings],
        "remediation": {
            priority: [asdict(f) for f in sorted_findings if f.priority == priority and f.status == "open"]
            for priority in ("P0", "P1", "P2", "P3")
        },
        "evidence": data.get("evidence", {}),
        "limitations": data.get("limitations", []),
    }


def executive_markdown(result: dict[str, Any]) -> str:
    blockers = result["critical_blockers"]
    strengths = ", ".join(p.replace("_", " ").title() for p in result["strongest_pillars"])
    weaknesses = ", ".join(p.replace("_", " ").title() for p in result["weakest_pillars"])
    blocker_text = "None identified." if not blockers else "\n".join(
        f"- **{b['id']} | {b['title']}**: {b['risk']}" for b in blockers
    )
    return f"""# Agentic AI Enterprise Readiness Executive Report

**Organization:** {result['organization']}  
**System:** {result['system']}  
**Framework:** {result['framework']}  
**Assessment date:** {result['assessment_date']}  
**Overall score:** **{result['overall_score']} / 100**  
**Maturity:** **{result['maturity_band']}**  
**Evidence completeness:** **{result['evidence_completeness']}%**  
**Production recommendation:** **{result['production_recommendation']}**

## Executive interpretation

The assessment evaluates engineering maturity across the ten pillars of the Agentic AI Gold Standard. The strongest areas are **{strengths}**. The largest maturity gaps are **{weaknesses}**.

The numerical score never overrides critical blockers. A system is not treated as Gold Standard Candidate unless it scores at least 90, has no unresolved critical blockers, and has sufficient assessment evidence.

## Critical blockers

{blocker_text}

## Priority roadmap

| Priority | Open findings |
|---|---:|
| P0 | {len(result['remediation']['P0'])} |
| P1 | {len(result['remediation']['P1'])} |
| P2 | {len(result['remediation']['P2'])} |
| P3 | {len(result['remediation']['P3'])} |

## Decision

**{result['production_recommendation']}**

## Important limitation

This is an engineering readiness assessment under the Agentic AI Gold Standard. It is not a regulatory certification, legal opinion, security guarantee, medical determination, or substitute for required domain-specific review.
"""


def technical_markdown(result: dict[str, Any]) -> str:
    rows = "\n".join(
        f"| {p.replace('_',' ').title()} | {result['pillar_scores'][p]} | {PILLARS[p]} | {result['weighted_contributions'][p]} |"
        for p in PILLARS
    )
    findings = []
    for f in result["findings"]:
        findings.append(
            f"### {f['id']} | {f['priority']} | {f['title']}\n\n"
            f"**Pillar:** {f['pillar'].replace('_',' ').title()}  \n"
            f"**Evidence:** {f['evidence']}  \n"
            f"**Risk:** {f['risk']}  \n"
            f"**Recommendation:** {f['recommendation']}  \n"
            f"**Critical blocker:** {'Yes' if f['critical_blocker'] else 'No'}\n"
        )
    finding_text = "\n".join(findings) if findings else "No findings recorded."
    return f"""# Agentic AI Enterprise Readiness Technical Report

**Organization:** {result['organization']}  
**System:** {result['system']}  
**Framework:** {result['framework']}  
**Overall score:** **{result['overall_score']} / 100**  
**Maturity:** **{result['maturity_band']}**

## Pillar scorecard

| Pillar | Raw score / 100 | Weight | Weighted points |
|---|---:|---:|---:|
{rows}
| **Total** |  | **100** | **{result['overall_score']}** |

## Assessment evidence completeness

**{result['evidence_completeness']}%** of the standard evidence categories were represented in the assessment input.

## Findings

{finding_text}

## Remediation order

Remediate **P0** blockers first, then **P1** production-readiness gaps, **P2** maturity improvements, and **P3** optimizations. Closure should require evidence, not only an assertion that a change was made.

## Production recommendation

**{result['production_recommendation']}**

## Limitations

{chr(10).join('- ' + item for item in result['limitations']) if result['limitations'] else '- No additional assessment limitations were supplied.'}
"""


def run(input_path: str, output_dir: str) -> dict[str, Any]:
    data = json.loads(Path(input_path).read_text(encoding="utf-8"))
    result = assess(data)
    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)
    (out / "assessment.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    (out / "executive_report.md").write_text(executive_markdown(result), encoding="utf-8")
    (out / "technical_report.md").write_text(technical_markdown(result), encoding="utf-8")
    return result


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Score an Agentic AI system against the Gold Standard")
    parser.add_argument("input", help="assessment input JSON")
    parser.add_argument("--output", default="assessment_output", help="output directory")
    args = parser.parse_args()
    result = run(args.input, args.output)
    print(f"{result['organization']} | {result['system']} | {result['overall_score']}/100 | {result['maturity_band']}")
