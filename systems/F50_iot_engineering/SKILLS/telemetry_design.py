def telemetry_design(context: dict) -> dict:
    return {"signals": context.get("signals", []), "units_and_frequency_required": True}
