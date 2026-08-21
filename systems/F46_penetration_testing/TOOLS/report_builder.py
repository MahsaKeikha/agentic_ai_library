def build_report(scope: dict, findings: list[dict]) -> dict:
    return {"scope": scope, "findings": findings, "human_approval_required": True}
