def allow(action:str,approved:bool=False)->bool:
    blocked={"certify_safety","authorize_clinical_use","certify_regulatory_compliance"}
    return action not in blocked and bool(approved)
