def run(context: dict) -> dict:
    observations = context.get("observations", [])
    return {"data_quality": {"observation_count": len(observations), "source_required": True}}
