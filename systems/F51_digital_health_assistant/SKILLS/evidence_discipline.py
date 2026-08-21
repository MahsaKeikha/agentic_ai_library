def apply(items: list[dict]) -> dict:
    return {"verified": [x for x in items if x.get("source")], "missing_evidence": [x for x in items if not x.get("source")]}
