def real_time_analysis(context: dict) -> dict:
    return {"deadlines": context.get("deadlines", []), "worst_case_timing_required": True}
