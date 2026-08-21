def migration_planning(context: dict) -> dict:
    return {"steps": context.get("migration_steps", []), "rollback_plan_required": True}
