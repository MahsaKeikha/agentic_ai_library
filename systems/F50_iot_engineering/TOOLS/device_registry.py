def device_registry(devices: list[dict]) -> dict:
    return {d.get("id", f"device_{i}"): d for i, d in enumerate(devices)}
