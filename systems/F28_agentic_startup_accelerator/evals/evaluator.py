def evaluate(outputs):
    required = {"venture_intake_agent", "market_agent", "product_agent", "growth_agent", "investor_readiness_agent"}
    seen = {item.get("agent") for item in outputs}
    return {"agent_coverage": len(required & seen) / len(required), "missing_agents": sorted(required - seen)}
