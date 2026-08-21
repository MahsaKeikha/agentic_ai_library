def run(context: dict) -> dict:
    return {"education": {"topics": context.get("education_topics", []), "clinical_advice": False}}
