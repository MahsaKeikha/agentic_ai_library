class FleetOperationsAgent:
    name = "Fleet Operations Agent"
    def run(self, context: dict) -> dict:
        return {"fleet_size": context.get("fleet_size", 0), "update_policy_review": True}
