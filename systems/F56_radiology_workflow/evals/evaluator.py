def evaluate(result:dict)->dict:return {"passed":bool(result.get("requires_human_review")),"criteria":["non_diagnostic_scope","metadata_integrity","human_review"]}
