def telemetry_schema_validator(signals: list[dict]) -> dict:
    missing = [s.get("name", "unnamed") for s in signals if "unit" not in s]
    return {"valid": not missing, "missing_units": missing}
