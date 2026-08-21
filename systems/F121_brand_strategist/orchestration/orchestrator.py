from AGENTS import research_agent,audience_agent,positioning_agent,messaging_agent,review_agent
def run(c): return {'research':research_agent.run(c),'audience':audience_agent.run(c),'positioning':positioning_agent.run(c),'messaging':messaging_agent.run(c),'review':review_agent.run(c)}
