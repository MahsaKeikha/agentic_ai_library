def run(context:dict)->dict:return {"metadata_complete":not bool(context.get("missing_metadata",[])),"missing":context.get("missing_metadata",[])}
