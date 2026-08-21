def evaluate(outputs):
    required = {"deal_intake_agent", "due_diligence_agent", "valuation_agent", "risk_agent", "integration_agent"}
    seen = {item.get("agent") for item in outputs}
    return {"agent_coverage": len(required & seen) / len(required), "missing_agents": sorted(required - seen)}
