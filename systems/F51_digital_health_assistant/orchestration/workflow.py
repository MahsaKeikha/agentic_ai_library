STAGES = ["intake", "data_quality", "care_plan", "education", "risk_escalation", "human_review"]

def run(context: dict) -> dict:
    return {"stages": STAGES, "context": context, "requires_human_review": True}
