from dataclasses import dataclass

@dataclass
class ScopeAgent:
    name: str = "Scope Agent"

    def run(self, context: dict) -> dict:
        allowed = set(context.get("authorized_assets", []))
        requested = set(context.get("requested_assets", []))
        return {"authorized": sorted(requested & allowed), "blocked": sorted(requested - allowed)}
