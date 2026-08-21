class ConnectivityAgent:
    name = "Connectivity Agent"
    def run(self, context: dict) -> dict:
        return {"protocols": context.get("protocols", []), "resilience_review": True}
