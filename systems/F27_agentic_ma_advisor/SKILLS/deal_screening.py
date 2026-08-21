def screen_deal(context):
    return {"strategic_fit": context.get("strategic_fit"), "red_flags": context.get("red_flags", [])}
