def auth_policy(context: dict) -> dict:
    return {"scheme": context.get("auth_scheme", "unspecified"), "least_privilege": True}
