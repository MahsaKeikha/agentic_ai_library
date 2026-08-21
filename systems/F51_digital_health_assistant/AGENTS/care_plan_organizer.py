def run(context: dict) -> dict:
    return {"care_plan_organization": {"goals": context.get("goals", []), "actions": context.get("approved_actions", [])}}
