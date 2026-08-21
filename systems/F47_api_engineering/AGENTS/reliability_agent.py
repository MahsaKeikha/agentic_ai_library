class ReliabilityAgent:
    name = "Reliability Agent"
    def run(self, context: dict) -> dict:
        return {"timeouts": context.get("timeouts", {}), "retries": context.get("retries", {}), "status": "reviewed"}
