def run(context: dict) -> dict:
    return {"protocol_plan": context.get("protocol", {}), "version": context.get("protocol_version")}
