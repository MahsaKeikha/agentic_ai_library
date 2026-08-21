def minimize(payload: dict, allowed: set[str]) -> dict:
    return {k: v for k, v in payload.items() if k in allowed}
