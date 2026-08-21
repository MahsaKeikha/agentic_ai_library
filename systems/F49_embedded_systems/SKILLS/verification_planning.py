def verification_planning(context: dict) -> dict:
    return {"tests": context.get("tests", []), "coverage_review": True}
