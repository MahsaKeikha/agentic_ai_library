class IntegrationAgent:
    name = "integration_agent"

    def run(self, context):
        return {"agent": self.name, "integration_priorities": context.get("integration_priorities", []), "status": "planned"}
