def analyze_schema(schema: dict) -> dict:
    return {"entity_count": len(schema), "entities": sorted(schema)}
