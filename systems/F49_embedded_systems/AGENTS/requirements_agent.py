class RequirementsAgent:
    name = "Requirements Agent"
    def run(self, context: dict) -> dict:
        return {"requirements": context.get("requirements", []), "status": "reviewed"}
