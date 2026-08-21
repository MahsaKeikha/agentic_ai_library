class AdoptionAgent:
    name = "adoption_agent"

    def run(self, context):
        return {"agent": self.name, "adoption": context.get("adoption", {}), "status": "planned"}
