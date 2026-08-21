def summarize_comparables(records):
    return [{"name": r.get("name"), "multiple": r.get("multiple")} for r in records]
