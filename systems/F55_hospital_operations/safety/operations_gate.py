def allow(action:str,approved:bool=False)->bool:
    blocked={"make_clinical_decision","override_emergency_process","autonomously_assign_clinical_priority"}
    return action not in blocked and bool(approved)
