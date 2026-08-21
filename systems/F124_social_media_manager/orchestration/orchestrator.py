from AGENTS import strategy_agent,content_agent,community_agent,measurement_agent,review_agent
def run(c): return {'strategy':strategy_agent.run(c),'content':content_agent.run(c),'community':community_agent.run(c),'measurement':measurement_agent.run(c),'review':review_agent.run(c)}
