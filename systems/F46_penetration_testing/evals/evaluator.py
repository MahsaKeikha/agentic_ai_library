"""Evaluation rules for F46 Penetration Testing."""

def evaluate(result: dict) -> dict:
    required = ["authorization", "scope", "findings", "remediation"]
    missing = [key for key in required if key not in result]
    return {"passed": not missing, "missing": missing}
