def connectivity_matrix(protocols: list[str]) -> dict:
    return {p: {"supported": True, "review_required": True} for p in protocols}
