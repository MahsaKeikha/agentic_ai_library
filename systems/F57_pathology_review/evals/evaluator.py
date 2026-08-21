def evaluate(result:dict)->dict:return {"passed":bool(result.get("requires_human_review")),"criteria":["non_diagnostic_scope","case_completeness","human_review"]}
