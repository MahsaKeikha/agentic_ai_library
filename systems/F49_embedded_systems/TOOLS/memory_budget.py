def memory_budget(components: list[dict]) -> dict:
    return {"flash_bytes": sum(c.get("flash_bytes", 0) for c in components), "ram_bytes": sum(c.get("ram_bytes", 0) for c in components)}
