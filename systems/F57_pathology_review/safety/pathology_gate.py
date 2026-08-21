def allow(action:str,approved:bool=False)->bool:
    blocked={"diagnose","interpret_specimen","override_pathologist","certify_case"}
    return action not in blocked and bool(approved)
