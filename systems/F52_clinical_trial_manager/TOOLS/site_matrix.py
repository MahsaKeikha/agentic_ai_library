def build(sites: list[dict]) -> list[dict]:
    return [{"site": s.get("name"), "status": s.get("status", "unknown")} for s in sites]
