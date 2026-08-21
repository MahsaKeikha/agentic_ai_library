def summarize(data: dict) -> dict:
    return {"screened": data.get("screened", 0), "enrolled": data.get("enrolled", 0)}
