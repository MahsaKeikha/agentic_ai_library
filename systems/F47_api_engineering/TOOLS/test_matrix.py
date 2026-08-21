def build_test_matrix(endpoints: list[str]) -> list[dict]:
    return [{"endpoint": e, "cases": ["success", "validation", "auth", "rate_limit"]} for e in endpoints]
