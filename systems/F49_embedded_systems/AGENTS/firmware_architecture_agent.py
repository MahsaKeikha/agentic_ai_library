class FirmwareArchitectureAgent:
    name = "Firmware Architecture Agent"
    def run(self, context: dict) -> dict:
        return {"modules": context.get("modules", []), "dependency_review": True}
