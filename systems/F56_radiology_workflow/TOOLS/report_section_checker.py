def check(required:list[str],sections:list[str])->dict:return {"missing_sections":[x for x in required if x not in sections]}
