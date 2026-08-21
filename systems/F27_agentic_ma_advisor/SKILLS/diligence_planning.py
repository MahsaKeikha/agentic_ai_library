def plan_diligence(required, supplied):
    missing = [item for item in required if item not in set(supplied)]
    return {"required": required, "missing": missing, "complete": not missing}
