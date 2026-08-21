from AGENTS import research_agent,opportunity_agent,technical_agent,measurement_agent,review_agent
def run(c): return {'research':research_agent.run(c),'opportunity':opportunity_agent.run(c),'technical':technical_agent.run(c),'measurement':measurement_agent.run(c),'review':review_agent.run(c)}
