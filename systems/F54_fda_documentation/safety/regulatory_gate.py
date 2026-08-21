def allow(action:str,approved:bool=False)->bool:
    blocked={"certify_compliance","certify_approval_readiness","submit_without_authorization"}
    return action not in blocked and bool(approved)
