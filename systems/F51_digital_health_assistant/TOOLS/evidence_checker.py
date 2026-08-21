def check(items: list[dict]) -> dict:
    return {"supported": [x for x in items if x.get("source")], "unsupported": [x for x in items if not x.get("source")]}
