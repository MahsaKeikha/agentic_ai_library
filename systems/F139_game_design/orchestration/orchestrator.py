from AGENTS import mechanics_agent,narrative_agent,systems_agent,balance_agent,review_agent
def run(c): return {'mechanics':mechanics_agent.run(c),'narrative':narrative_agent.run(c),'systems':systems_agent.run(c),'balance':balance_agent.run(c),'review':review_agent.run(c)}
