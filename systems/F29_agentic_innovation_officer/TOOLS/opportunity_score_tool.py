def score_opportunity(item):
    impact = float(item.get("impact", 0) or 0)
    feasibility = float(item.get("feasibility", 0) or 0)
    evidence = float(item.get("evidence", 0) or 0)
    return {"score": impact + feasibility + evidence, "inputs": item}
