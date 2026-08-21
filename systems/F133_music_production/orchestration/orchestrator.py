from AGENTS import composition_agent,arrangement_agent,sound_design_agent,mixing_agent,review_agent
def run(c): return {'composition':composition_agent.run(c),'arrangement':arrangement_agent.run(c),'sound_design':sound_design_agent.run(c),'mixing':mixing_agent.run(c),'review':review_agent.run(c)}
