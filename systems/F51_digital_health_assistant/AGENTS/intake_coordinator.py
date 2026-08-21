def run(context: dict) -> dict:
    return {"intake": context, "missing": [k for k in ["goals", "observations"] if not context.get(k)]}
