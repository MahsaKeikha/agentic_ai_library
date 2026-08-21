from AGENTS import research_agent,information_architecture_agent,interaction_agent,usability_agent,review_agent
def run(c): return {'research':research_agent.run(c),'ia':information_architecture_agent.run(c),'interaction':interaction_agent.run(c),'usability':usability_agent.run(c),'review':review_agent.run(c)}
