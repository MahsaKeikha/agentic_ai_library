class QueryPerformanceAgent:
    name = "Query Performance Agent"
    def run(self, context: dict) -> dict:
        return {"queries_reviewed": len(context.get("queries", [])), "index_review_required": True}
