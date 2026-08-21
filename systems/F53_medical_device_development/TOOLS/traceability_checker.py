def check(items: list[dict]) -> dict: return {"unlinked": [x for x in items if not x.get("source_id")]}
