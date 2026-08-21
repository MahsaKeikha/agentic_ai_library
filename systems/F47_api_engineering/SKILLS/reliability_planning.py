def reliability_planning(context: dict) -> dict:
    return {"timeouts": context.get("timeouts", {}), "retries": context.get("retries", {}), "idempotency_review": True}
