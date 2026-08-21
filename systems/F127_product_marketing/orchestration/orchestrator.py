from AGENTS import evidence_agent,audience_agent,positioning_agent,launch_agent,review_agent
def run(c): return {'evidence':evidence_agent.run(c),'audience':audience_agent.run(c),'positioning':positioning_agent.run(c),'launch':launch_agent.run(c),'review':review_agent.run(c)}
