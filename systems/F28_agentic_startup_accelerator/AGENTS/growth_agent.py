class GrowthAgent:
    name = "growth_agent"

    def run(self, context):
        return {"agent": self.name, "growth": context.get("growth", {}), "status": "planned"}
