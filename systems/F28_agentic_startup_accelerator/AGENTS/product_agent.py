class ProductAgent:
    name = "product_agent"

    def run(self, context):
        return {"agent": self.name, "product": context.get("product", {}), "status": "reviewed"}
