from AGENTS import brief_agent,concept_agent,layout_agent,brand_agent,review_agent
def run(c): return {'brief':brief_agent.run(c),'concepts':concept_agent.run(c),'layout':layout_agent.run(c),'brand':brand_agent.run(c),'review':review_agent.run(c)}
