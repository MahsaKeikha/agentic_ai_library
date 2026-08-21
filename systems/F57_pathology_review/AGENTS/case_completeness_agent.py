def run(context:dict)->dict:return {"case_elements":context.get("case_elements",[]),"complete":not bool(context.get("missing_case_elements",[]))}
