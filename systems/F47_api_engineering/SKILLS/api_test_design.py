def api_test_design(context: dict) -> dict:
    return {"test_cases": context.get("test_cases", []), "negative_cases_required": True}
