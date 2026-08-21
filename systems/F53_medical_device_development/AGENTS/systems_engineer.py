def run(context: dict) -> dict: return {"system_architecture": context.get("architecture", {}), "interfaces": context.get("interfaces", [])}
