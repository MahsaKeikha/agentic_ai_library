def run(context:dict)->dict:
    flags=context.get("escalation_flags",[])
    return {"escalation":{"required":bool(flags),"flags":flags,"route":"qualified_human"}}
