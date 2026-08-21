def control_assessment(context: dict) -> dict:
    controls = context.get("controls", [])
    gaps = [c for c in controls if not c.get("verified", False)]
    return {"reviewed": len(controls), "gaps": gaps}
