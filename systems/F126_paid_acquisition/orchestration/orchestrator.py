from AGENTS import audience_agent,creative_agent,budget_agent,measurement_agent,review_agent
def run(c): return {'audience':audience_agent.run(c),'creative':creative_agent.run(c),'budget':budget_agent.run(c),'measurement':measurement_agent.run(c),'review':review_agent.run(c)}
