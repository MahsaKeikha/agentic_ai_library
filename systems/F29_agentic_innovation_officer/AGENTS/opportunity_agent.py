class OpportunityAgent:
    name = "opportunity_agent"

    def run(self, context):
        return {"agent": self.name, "opportunities": context.get("opportunities", []), "status": "scanned"}
