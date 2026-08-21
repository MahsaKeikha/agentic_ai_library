def compare(old: dict, new: dict) -> dict:
    return {"changed_keys": sorted(set(old) ^ set(new) | {k for k in old if k in new and old[k] != new[k]})}
