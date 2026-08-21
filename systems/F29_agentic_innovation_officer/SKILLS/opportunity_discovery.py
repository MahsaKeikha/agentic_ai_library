def discover_opportunities(signals):
    return {"signals": signals, "opportunities": [s for s in signals if s.get("evidence") is not None]}
