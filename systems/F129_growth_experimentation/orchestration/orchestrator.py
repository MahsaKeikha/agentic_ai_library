from AGENTS import hypothesis_agent,experiment_agent,measurement_agent,risk_agent,review_agent
def run(c): return {'hypothesis':hypothesis_agent.run(c),'experiment':experiment_agent.run(c),'measurement':measurement_agent.run(c),'risk':risk_agent.run(c),'review':review_agent.run(c)}
