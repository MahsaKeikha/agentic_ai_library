def evaluate(result:dict)->dict:return {"passed":bool(result.get("requires_human_review")),"criteria":["observation_integrity","non_diagnostic_scope","escalation","human_review"]}
