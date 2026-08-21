from AGENTS.scope_agent import ScopeAgent
from AGENTS.asset_review_agent import AssetReviewAgent
from AGENTS.control_validation_agent import ControlValidationAgent
from AGENTS.finding_triage_agent import FindingTriageAgent
from AGENTS.reporting_agent import ReportingAgent

class PenetrationTestingWorkflow:
    def __init__(self) -> None:
        self.agents = [
            ScopeAgent(),
            AssetReviewAgent(),
            ControlValidationAgent(),
            FindingTriageAgent(),
            ReportingAgent(),
        ]

    def run(self, context: dict) -> list[dict]:
        results = []
        working = dict(context)
        for agent in self.agents:
            result = agent.run(working)
            results.append({"agent": agent.name, "result": result})
            working.update(result)
        return results
