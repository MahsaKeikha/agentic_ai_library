def fleet_lifecycle(context: dict) -> dict:
    return {"fleet_size": context.get("fleet_size", 0), "secure_update_process_required": True}
