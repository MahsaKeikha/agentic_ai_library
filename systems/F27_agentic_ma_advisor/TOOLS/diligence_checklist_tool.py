def missing_items(required, supplied):
    supplied_set = set(supplied)
    return [item for item in required if item not in supplied_set]
