def run(ctx): return {'approved': bool(ctx.get('human_approval', False))}
