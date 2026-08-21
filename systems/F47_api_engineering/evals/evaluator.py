"""Evaluation rules for F47 API Engineering."""

def evaluate(result: dict) -> dict:
    required = ["contract", "security", "reliability", "tests"]
    missing = [key for key in required if key not in result]
    return {"passed": not missing, "missing": missing}
