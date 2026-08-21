def firmware_partitioning(context: dict) -> dict:
    return {"modules": context.get("modules", []), "coupling_review": True}
