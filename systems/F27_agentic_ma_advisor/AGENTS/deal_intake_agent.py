class DealIntakeAgent:
    name = "deal_intake_agent"

    def run(self, context):
        return {"agent": self.name, "deal_context": context, "status": "structured"}
