from AGENTS import research_agent,audience_agent,editorial_agent,distribution_agent,review_agent
def run(c): return {'research':research_agent.run(c),'audience':audience_agent.run(c),'editorial':editorial_agent.run(c),'distribution':distribution_agent.run(c),'review':review_agent.run(c)}
