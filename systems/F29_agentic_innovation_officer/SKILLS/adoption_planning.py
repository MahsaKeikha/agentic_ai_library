def plan_adoption(stakeholders, barriers):
    return {"stakeholders": stakeholders, "barriers": barriers, "actions": [{"barrier": b, "status": "planned"} for b in barriers]}
