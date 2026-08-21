def rate_limit_plan(requests_per_minute: int, burst_factor: float = 1.5) -> dict:
    return {"steady_rpm": requests_per_minute, "burst_rpm": int(requests_per_minute * burst_factor)}
