from AGENTS.venture_intake_agent import VentureIntakeAgent
from AGENTS.market_agent import MarketAgent
from AGENTS.product_agent import ProductAgent
from AGENTS.growth_agent import GrowthAgent
from AGENTS.investor_readiness_agent import InvestorReadinessAgent


def run_workflow(context):
    agents = [VentureIntakeAgent(), MarketAgent(), ProductAgent(), GrowthAgent(), InvestorReadinessAgent()]
    return [agent.run(context) for agent in agents]
