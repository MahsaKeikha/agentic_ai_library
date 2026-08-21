def plan_growth(channels):
    return {"channels": channels, "experiments": [{"channel": c, "status": "planned"} for c in channels]}
