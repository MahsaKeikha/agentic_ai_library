def pin_conflicts(pin_map: list[dict]) -> list[str]:
    seen, conflicts = set(), []
    for item in pin_map:
        pin = item.get("pin")
        if pin in seen:
            conflicts.append(str(pin))
        seen.add(pin)
    return conflicts
