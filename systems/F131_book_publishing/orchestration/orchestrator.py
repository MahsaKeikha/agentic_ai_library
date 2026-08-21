from AGENTS import manuscript_agent,editorial_agent,production_agent,metadata_agent,review_agent
def run(c): return {'manuscript':manuscript_agent.run(c),'editorial':editorial_agent.run(c),'production':production_agent.run(c),'metadata':metadata_agent.run(c),'review':review_agent.run(c)}
