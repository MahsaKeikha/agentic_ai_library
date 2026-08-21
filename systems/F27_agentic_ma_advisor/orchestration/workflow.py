from AGENTS.deal_intake_agent import DealIntakeAgent
from AGENTS.due_diligence_agent import DueDiligenceAgent
from AGENTS.valuation_agent import ValuationAgent
from AGENTS.risk_agent import RiskAgent
from AGENTS.integration_agent import IntegrationAgent


def run_workflow(context):
    agents = [DealIntakeAgent(), DueDiligenceAgent(), ValuationAgent(), RiskAgent(), IntegrationAgent()]
    return [agent.run(context) for agent in agents]
