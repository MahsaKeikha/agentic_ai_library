from AGENTS import research_agent,narrative_agent,stakeholder_agent,risk_agent,review_agent
def run(c): return {'research':research_agent.run(c),'narrative':narrative_agent.run(c),'stakeholder':stakeholder_agent.run(c),'risk':risk_agent.run(c),'review':review_agent.run(c)}
