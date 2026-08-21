def evaluate(result:dict)->dict:return {"passed":bool(result.get("requires_human_review")),"criteria":["workflow_scope","evidence_discipline","escalation","human_review"]}
