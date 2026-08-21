def run(context: dict) -> dict:
    return {"data_quality": {"queries": context.get("data_queries", []), "missing": context.get("missing_data", [])}}
