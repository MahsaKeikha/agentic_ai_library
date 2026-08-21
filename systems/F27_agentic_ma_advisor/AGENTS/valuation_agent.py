class ValuationAgent:
    name = "valuation_agent"

    def run(self, context):
        return {"agent": self.name, "valuation_inputs": context.get("valuation_inputs", {}), "status": "analyzed"}
