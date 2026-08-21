def requirements_traceability(context: dict) -> dict:
    return {"requirements": context.get("requirements", []), "traceability_required": True}
