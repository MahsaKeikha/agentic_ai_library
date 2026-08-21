def flag(payload: dict) -> list[str]:
    return list(payload.get("urgent_flags", []))
