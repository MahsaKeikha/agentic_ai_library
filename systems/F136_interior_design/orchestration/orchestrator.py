from AGENTS import requirements_agent,space_planning_agent,materials_agent,lighting_agent,review_agent
def run(c): return {'requirements':requirements_agent.run(c),'space_plan':space_planning_agent.run(c),'materials':materials_agent.run(c),'lighting':lighting_agent.run(c),'review':review_agent.run(c)}
