class AuthAgent:
    name = "Auth Agent"
    def run(self, context: dict) -> dict:
        return {"auth_scheme": context.get("auth_scheme", "unspecified"), "requires_review": True}
