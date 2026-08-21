from AGENTS import trend_agent,concept_agent,garment_agent,materials_agent,review_agent
def run(c): return {'trends':trend_agent.run(c),'concepts':concept_agent.run(c),'garments':garment_agent.run(c),'materials':materials_agent.run(c),'review':review_agent.run(c)}
