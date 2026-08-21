def rank_findings(findings: list[dict]) -> list[dict]:
    return sorted(findings, key=lambda item: item.get("severity", 0), reverse=True)
