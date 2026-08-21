def prioritize_portfolio(items):
    return sorted(items, key=lambda x: float(x.get("priority", 0) or 0), reverse=True)
