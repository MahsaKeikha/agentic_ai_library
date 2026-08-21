class TelemetryAgent:
    name = "Telemetry Agent"
    def run(self, context: dict) -> dict:
        return {"signals": context.get("signals", []), "schema_review": True}
