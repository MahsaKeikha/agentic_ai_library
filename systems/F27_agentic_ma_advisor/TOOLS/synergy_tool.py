def estimate_synergy(items):
    return {"items": items, "count": len(items), "total_estimate": sum(float(i.get("estimate", 0) or 0) for i in items)}
