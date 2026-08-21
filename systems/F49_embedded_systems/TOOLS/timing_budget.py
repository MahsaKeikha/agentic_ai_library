def timing_budget(tasks: list[dict]) -> dict:
    return {"total_wcet_ms": sum(t.get("wcet_ms", 0) for t in tasks)}
