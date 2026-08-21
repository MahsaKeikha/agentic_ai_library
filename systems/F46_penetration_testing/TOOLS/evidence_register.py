def build_evidence_register(items: list[dict]) -> list[dict]:
    return [{"id": i + 1, **item} for i, item in enumerate(items)]
