class DocumentationAgent:
    name = "Documentation Agent"
    def run(self, context: dict) -> dict:
        return {"documented_endpoints": list(context.get("api_contract", {}).keys()), "status": "drafted"}
