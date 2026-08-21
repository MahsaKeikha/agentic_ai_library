def allow(action:str,approved:bool=False)->bool:
    blocked={"interpret_image","diagnose","override_radiologist","replace_emergency_process"}
    return action not in blocked and bool(approved)
