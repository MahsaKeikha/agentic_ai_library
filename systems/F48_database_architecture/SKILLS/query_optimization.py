def query_optimization(context: dict) -> dict:
    return {"query_count": len(context.get("queries", [])), "measure_before_change": True}
