def index_candidates(queries: list[dict]) -> list[str]:
    return sorted({field for q in queries for field in q.get("filter_fields", [])})
