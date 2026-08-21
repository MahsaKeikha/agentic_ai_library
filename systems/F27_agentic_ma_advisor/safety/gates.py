def requires_human_approval(context):
    return bool(context.get("external_action") or context.get("binding_decision"))
