def normalize_risks(risks):
    return [{"risk": r.get("risk"), "severity": r.get("severity", "unknown"), "owner": r.get("owner")} for r in risks]
