from AGENTS.contract_agent import ContractAgent
from AGENTS.auth_agent import AuthAgent
from AGENTS.reliability_agent import ReliabilityAgent
from AGENTS.testing_agent import TestingAgent
from AGENTS.documentation_agent import DocumentationAgent

class APIEngineeringWorkflow:
    def __init__(self) -> None:
        self.agents = [ContractAgent(), AuthAgent(), ReliabilityAgent(), TestingAgent(), DocumentationAgent()]
    def run(self, context: dict) -> list[dict]:
        return [{"agent": a.name, "result": a.run(context)} for a in self.agents]
