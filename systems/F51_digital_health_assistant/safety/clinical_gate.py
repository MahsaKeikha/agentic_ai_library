def allow(action: str, approved: bool = False) -> bool:
    blocked = {"diagnose", "prescribe", "authorize_treatment", "replace_emergency_triage"}
    return action not in blocked and bool(approved)
