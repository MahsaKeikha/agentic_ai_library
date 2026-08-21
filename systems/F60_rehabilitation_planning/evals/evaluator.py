def evaluate(result:dict)->dict:return {"passed":bool(result.get("requires_human_review")),"criteria":["non_prescriptive_scope","progress_integrity","safety_escalation","human_review"]}
