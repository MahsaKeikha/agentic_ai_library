def device_identity_planning(context: dict) -> dict:
    return {"device_types": context.get("device_types", []), "unique_identity_required": True}
