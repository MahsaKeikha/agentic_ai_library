STAGES=["capacity","flow","staffing","quality","safety_escalation","briefing","human_review"]
def run(context:dict)->dict:return {"stages":STAGES,"context":context,"requires_human_review":True}
