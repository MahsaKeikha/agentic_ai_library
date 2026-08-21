class TimingAgent:
    name = "Timing Agent"
    def run(self, context: dict) -> dict:
        return {"deadlines": context.get("deadlines", []), "timing_analysis_required": True}
