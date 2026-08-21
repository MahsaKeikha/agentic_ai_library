class HardwareInterfaceAgent:
    name = "Hardware Interface Agent"
    def run(self, context: dict) -> dict:
        return {"interfaces": context.get("interfaces", []), "conflict_review": True}
