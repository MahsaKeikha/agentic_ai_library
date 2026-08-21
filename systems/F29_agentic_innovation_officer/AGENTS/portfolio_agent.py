class PortfolioAgent:
    name = "portfolio_agent"

    def run(self, context):
        return {"agent": self.name, "portfolio": context.get("portfolio", []), "status": "prioritized"}
