def change_gate(context: dict) -> None:
    if context.get("production_change") and not context.get("approved"):
        raise PermissionError("Production API changes require human approval.")
