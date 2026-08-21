def build_financial_snapshot(inputs):
    return {"revenue": inputs.get("revenue"), "ebitda": inputs.get("ebitda"), "debt": inputs.get("debt")}
