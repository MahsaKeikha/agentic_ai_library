def validate_schema(schema: dict) -> dict:
    required = {"path", "method", "responses"}
    missing = sorted(required - set(schema))
    return {"valid": not missing, "missing": missing}
