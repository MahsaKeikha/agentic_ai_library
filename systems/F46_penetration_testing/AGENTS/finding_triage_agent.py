from dataclasses import dataclass

@dataclass
class FindingTriageAgent:
    name: str = "Finding Triage Agent"

    def run(self, context: dict) -> dict:
        findings = context.get("findings", [])
        ranked = sorted(findings, key=lambda item: item.get("severity", 0), reverse=True)
        return {"ranked_findings": ranked}
