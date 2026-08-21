def fleet_health_summary(devices: list[dict]) -> dict:
    healthy = sum(1 for d in devices if d.get("healthy"))
    return {"total": len(devices), "healthy": healthy, "attention": len(devices) - healthy}
