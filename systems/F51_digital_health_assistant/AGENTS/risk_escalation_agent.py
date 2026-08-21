def run(context: dict) -> dict:
    flags = context.get("urgent_flags", [])
    return {"escalation": {"required": bool(flags), "flags": flags, "route": "qualified_human"}}
