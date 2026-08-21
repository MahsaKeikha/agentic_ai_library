def resilience_planning(context: dict) -> dict:
    return {"backup_policy": context.get("backup_policy", {}), "restore_validation": True}
