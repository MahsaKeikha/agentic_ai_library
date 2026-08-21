STAGES=["worklist","metadata","prior_studies","report_completeness","safety_escalation","human_review"]
def run(context:dict)->dict:return {"stages":STAGES,"context":context,"requires_human_review":True}
