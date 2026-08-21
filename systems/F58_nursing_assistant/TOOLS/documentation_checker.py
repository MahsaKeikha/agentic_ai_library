def check(items:list[dict])->dict:return {"unsupported":[x for x in items if not x.get("source")]}
