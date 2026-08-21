def verification_matrix(requirements: list[dict]) -> list[dict]:
    return [{"requirement": r.get("id"), "test": r.get("test_id"), "covered": bool(r.get("test_id"))} for r in requirements]
