def finding_prioritization(context: dict) -> dict:
    findings = context.get("findings", [])
    ranked = sorted(findings, key=lambda item: item.get("severity", 0), reverse=True)
    return {"prioritized_findings": ranked}
