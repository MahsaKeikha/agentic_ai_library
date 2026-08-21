def evaluate(outputs):
    required = {"opportunity_agent", "portfolio_agent", "experiment_agent", "adoption_agent", "governance_agent"}
    seen = {item.get("agent") for item in outputs}
    return {"agent_coverage": len(required & seen) / len(required), "missing_agents": sorted(required - seen)}
