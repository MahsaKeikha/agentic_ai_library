class ContractAgent:
    name = "Contract Agent"
    def run(self, context: dict) -> dict:
        return {"contract": context.get("api_contract", {}), "status": "reviewed"}
