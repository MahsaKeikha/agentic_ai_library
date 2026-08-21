class SchemaAgent:
    name = "Schema Agent"
    def run(self, context: dict) -> dict:
        return {"schema": context.get("schema", {}), "status": "reviewed"}
