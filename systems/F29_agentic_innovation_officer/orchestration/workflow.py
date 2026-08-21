from AGENTS.opportunity_agent import OpportunityAgent
from AGENTS.portfolio_agent import PortfolioAgent
from AGENTS.experiment_agent import ExperimentAgent
from AGENTS.adoption_agent import AdoptionAgent
from AGENTS.governance_agent import GovernanceAgent


def run_workflow(context):
    agents = [OpportunityAgent(), PortfolioAgent(), ExperimentAgent(), AdoptionAgent(), GovernanceAgent()]
    return [agent.run(context) for agent in agents]
