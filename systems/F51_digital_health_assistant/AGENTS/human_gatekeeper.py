def approve(output: dict, approved: bool) -> dict:
    return {"approved_for_use": bool(approved), "output": output}
