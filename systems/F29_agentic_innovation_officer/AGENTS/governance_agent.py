class GovernanceAgent:
    name = "governance_agent"

    def run(self, context):
        return {"agent": self.name, "constraints": context.get("constraints", []), "status": "reviewed"}
