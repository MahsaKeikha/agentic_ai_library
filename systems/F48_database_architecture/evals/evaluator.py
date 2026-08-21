"""Evaluation rules for F48 Database Architecture."""

def evaluate(result: dict) -> dict:
    required = ["schema", "performance", "migration", "resilience"]
    missing = [key for key in required if key not in result]
    return {"passed": not missing, "missing": missing}
