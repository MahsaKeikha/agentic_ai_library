def contract_design(context: dict) -> dict:
    return {"contract": context.get("api_contract", {}), "versioned": True}
