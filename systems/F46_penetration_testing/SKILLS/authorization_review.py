def authorization_review(context: dict) -> dict:
    return {
        "has_written_authorization": bool(context.get("written_authorization")),
        "authorized_assets": context.get("authorized_assets", []),
        "stop_on_scope_violation": True,
    }
