STAGES = ["protocol", "sites", "recruitment", "data_quality", "deviations", "reporting", "human_review"]
def run(context: dict) -> dict: return {"stages": STAGES, "context": context, "requires_human_review": True}
