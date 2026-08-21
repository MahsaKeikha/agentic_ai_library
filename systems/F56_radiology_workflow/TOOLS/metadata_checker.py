def check(required:list[str],metadata:dict)->dict:return {"missing":[k for k in required if not metadata.get(k)]}
