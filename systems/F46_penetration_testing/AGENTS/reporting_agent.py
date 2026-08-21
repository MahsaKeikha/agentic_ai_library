from dataclasses import dataclass

@dataclass
class ReportingAgent:
    name: str = "Reporting Agent"

    def run(self, context: dict) -> dict:
        return {
            "summary": context.get("summary", "Assessment completed within authorized scope."),
            "finding_count": len(context.get("findings", [])),
            "requires_human_review": True,
        }
