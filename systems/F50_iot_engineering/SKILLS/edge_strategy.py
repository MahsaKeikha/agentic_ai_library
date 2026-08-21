def edge_strategy(context: dict) -> dict:
    return {"edge_rules": context.get("edge_rules", []), "offline_behavior_required": True}
