class DueDiligenceAgent:
    name = "due_diligence_agent"

    def run(self, context):
        gaps = context.get("missing_evidence", []) if isinstance(context, dict) else []
        return {"agent": self.name, "evidence_gaps": gaps, "status": "reviewed"}
