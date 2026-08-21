def check(required:list[str],present:list[str])->dict:return {"missing":[x for x in required if x not in present]}
