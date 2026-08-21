"""Evaluation rules for F50 IoT Engineering."""

def evaluate(result: dict) -> dict:
    required = ["device", "telemetry", "connectivity", "fleet"]
    missing = [key for key in required if key not in result]
    return {"passed": not missing, "missing": missing}
