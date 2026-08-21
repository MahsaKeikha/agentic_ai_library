def check(required:list[str],metadata:dict)->dict:return {"missing":[x for x in required if not metadata.get(x)]}
