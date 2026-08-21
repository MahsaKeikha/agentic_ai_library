from AGENTS import evidence_agent,qualitative_agent,quantitative_agent,insight_agent,review_agent
def run(c): return {'evidence':evidence_agent.run(c),'qualitative':qualitative_agent.run(c),'quantitative':quantitative_agent.run(c),'insight':insight_agent.run(c),'review':review_agent.run(c)}
