def assess_investor_readiness(context):
    return {"story": context.get("story"), "metrics": context.get("metrics", {}), "gaps": context.get("fundraising_gaps", [])}
