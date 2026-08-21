def unit_economics(inputs):
    cac = float(inputs.get("cac", 0) or 0)
    ltv = float(inputs.get("ltv", 0) or 0)
    return {"cac": cac, "ltv": ltv, "ltv_cac_ratio": (ltv / cac) if cac else None}
