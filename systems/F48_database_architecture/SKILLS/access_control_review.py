def access_control_review(context: dict) -> dict:
    return {"roles": context.get("roles", []), "least_privilege": True}
