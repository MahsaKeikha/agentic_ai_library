def evaluate(result: dict) -> dict:
    return {"passed": bool(result.get("requires_human_review")), "criteria": ["human_review", "no_diagnosis", "evidence_discipline"]}
