class InvestorReadinessAgent:
    name = "investor_readiness_agent"

    def run(self, context):
        return {"agent": self.name, "fundraising": context.get("fundraising", {}), "status": "assessed"}
