def data_modeling(context: dict) -> dict:
    return {"schema": context.get("schema", {}), "normalization_review": True}
