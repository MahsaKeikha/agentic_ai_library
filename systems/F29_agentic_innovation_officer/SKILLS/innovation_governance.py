def review_governance(constraints, approvals):
    return {"constraints": constraints, "approvals": approvals, "ready": bool(approvals) and not any(c.get("blocking") for c in constraints)}
