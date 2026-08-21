class RiskAgent:
    name = "risk_agent"

    def run(self, context):
        return {"agent": self.name, "risks": context.get("risks", []), "status": "assessed"}
