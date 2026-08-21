def assess_risks(risks):
    return {"risks": risks, "high_priority": [r for r in risks if r.get("severity") == "high"]}
