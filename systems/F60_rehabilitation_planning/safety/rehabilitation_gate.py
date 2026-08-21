def allow(action:str,approved:bool=False)->bool:
    blocked={"prescribe_treatment","diagnose","authorize_clinical_goal","replace_emergency_process"}
    return action not in blocked and bool(approved)
