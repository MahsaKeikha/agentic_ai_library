def evaluate(result:dict)->dict:return {"passed":bool(result.get("requires_human_review")),"criteria":["traceability","risk_review","verification","human_authority"]}
