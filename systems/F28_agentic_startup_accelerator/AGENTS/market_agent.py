class MarketAgent:
    name = "market_agent"

    def run(self, context):
        return {"agent": self.name, "market": context.get("market", {}), "status": "analyzed"}
