def allow(action: str, approved: bool = False) -> bool:
    blocked = {"change_protocol_without_approval", "make_clinical_decision", "certify_compliance"}
    return action not in blocked and bool(approved)
