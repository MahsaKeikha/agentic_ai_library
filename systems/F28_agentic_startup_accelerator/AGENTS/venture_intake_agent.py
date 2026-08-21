class VentureIntakeAgent:
    name = "venture_intake_agent"

    def run(self, context):
        return {"agent": self.name, "venture": context.get("venture", {}), "status": "structured"}
