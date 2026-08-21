def authorization_gate(context: dict) -> None:
    if not context.get("written_authorization"):
        raise PermissionError("Written authorization is required before assessment planning.")
