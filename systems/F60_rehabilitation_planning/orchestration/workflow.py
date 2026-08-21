STAGES=["goals","sessions","progress","equipment_environment","escalation","human_review"]
def run(context:dict)->dict:return {"stages":STAGES,"context":context,"requires_human_review":True}
