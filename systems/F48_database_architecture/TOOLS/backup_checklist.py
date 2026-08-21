def backup_checklist(policy: dict) -> dict:
    return {"has_frequency": bool(policy.get("frequency")), "has_restore_test": bool(policy.get("restore_test"))}
