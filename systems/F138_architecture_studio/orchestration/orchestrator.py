from AGENTS import site_agent,program_agent,concept_agent,systems_agent,review_agent
def run(c): return {'site':site_agent.run(c),'program':program_agent.run(c),'concept':concept_agent.run(c),'systems':systems_agent.run(c),'review':review_agent.run(c)}
