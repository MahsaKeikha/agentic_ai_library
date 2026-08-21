class MigrationAgent:
    name = "Migration Agent"
    def run(self, context: dict) -> dict:
        return {"migration_steps": context.get("migration_steps", []), "rollback_required": True}
