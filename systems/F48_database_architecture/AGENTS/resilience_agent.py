class ResilienceAgent:
    name = "Resilience Agent"
    def run(self, context: dict) -> dict:
        return {"backup_policy": context.get("backup_policy", {}), "restore_test_required": True}
