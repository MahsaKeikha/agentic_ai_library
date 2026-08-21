def evaluate(result: dict) -> dict:
    return {"passed": bool(result.get("requires_human_review")), "criteria": ["protocol_traceability", "deviation_review", "human_authority"]}
