class TestingAgent:
    name = "Testing Agent"
    def run(self, context: dict) -> dict:
        cases = context.get("test_cases", [])
        return {"test_case_count": len(cases), "coverage_status": "planned" if cases else "missing"}
