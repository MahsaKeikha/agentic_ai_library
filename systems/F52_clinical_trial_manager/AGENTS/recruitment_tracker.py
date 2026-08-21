def run(context: dict) -> dict:
    return {"recruitment": context.get("recruitment", {}), "forecast_only": True}
