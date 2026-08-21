"""Evaluation rules for F49 Embedded Systems."""

def evaluate(result: dict) -> dict:
    required = ["requirements", "interfaces", "timing", "verification"]
    missing = [key for key in required if key not in result]
    return {"passed": not missing, "missing": missing}
