def evaluate(result:dict)->dict:return {"passed":bool(result.get("requires_human_review")),"criteria":["source_control","evidence_gaps","traceability","human_authority"]}
