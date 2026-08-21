STAGES=["document_intake","requirements_mapping","evidence_gaps","traceability","review","submission_gate"]
def run(context:dict)->dict:return {"stages":STAGES,"context":context,"requires_human_review":True}
