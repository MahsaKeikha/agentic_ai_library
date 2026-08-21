from dataclasses import dataclass

@dataclass
class ControlValidationAgent:
    name: str = "Control Validation Agent"

    def run(self, context: dict) -> dict:
        controls = context.get("controls", [])
        findings = [c for c in controls if not c.get("verified", False)]
        return {"controls_reviewed": len(controls), "unverified_controls": findings}
