STAGES=["routine","observations","resources","communication","escalation","human_review"]
def run(context:dict)->dict:return {"stages":STAGES,"context":context,"requires_human_review":True}
