def prioritize(items):
    return sorted(items, key=lambda x: (float(x.get("impact", 0) or 0), float(x.get("feasibility", 0) or 0)), reverse=True)
