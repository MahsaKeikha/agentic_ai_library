class SecurityAgent:
    name = "Database Security Agent"
    def run(self, context: dict) -> dict:
        return {"roles": context.get("roles", []), "least_privilege_review": True}
