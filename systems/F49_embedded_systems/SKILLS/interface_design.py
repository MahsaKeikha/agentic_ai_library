def interface_design(context: dict) -> dict:
    return {"interfaces": context.get("interfaces", []), "electrical_review_required": True}
