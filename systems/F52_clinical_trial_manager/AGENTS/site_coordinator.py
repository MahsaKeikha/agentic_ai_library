def run(context: dict) -> dict:
    return {"sites": context.get("sites", []), "open_actions": context.get("site_actions", [])}
