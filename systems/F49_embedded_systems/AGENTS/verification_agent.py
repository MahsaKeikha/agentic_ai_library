class VerificationAgent:
    name = "Verification Agent"
    def run(self, context: dict) -> dict:
        return {"test_count": len(context.get("tests", [])), "hardware_in_loop_review": True}
