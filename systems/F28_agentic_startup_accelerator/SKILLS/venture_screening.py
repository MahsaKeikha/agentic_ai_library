def screen_venture(context):
    return {"problem": context.get("problem"), "customer": context.get("customer"), "evidence": context.get("evidence", [])}
