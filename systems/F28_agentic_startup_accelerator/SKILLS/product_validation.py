def validate_product(context):
    return {"hypotheses": context.get("hypotheses", []), "tests": context.get("tests", []), "evidence": context.get("evidence", [])}
