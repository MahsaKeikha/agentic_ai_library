STAGES=["requirements","risk","systems","verification","human_factors","regulatory_docs","human_review"]
def run(context: dict)->dict:return {"stages":STAGES,"context":context,"requires_human_review":True}
