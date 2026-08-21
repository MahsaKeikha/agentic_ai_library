def connectivity_planning(context: dict) -> dict:
    return {"protocols": context.get("protocols", []), "fallback_required": True}
