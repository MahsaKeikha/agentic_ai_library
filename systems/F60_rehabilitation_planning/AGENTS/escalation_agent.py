def run(context:dict)->dict:
    flags=context.get("safety_flags",[])
    return {"escalation":{"required":bool(flags),"flags":flags,"route":"qualified_human"}}
