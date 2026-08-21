from AGENTS import story_agent,character_agent,scene_agent,continuity_agent,review_agent
def run(c): return {'story':story_agent.run(c),'characters':character_agent.run(c),'scenes':scene_agent.run(c),'continuity':continuity_agent.run(c),'review':review_agent.run(c)}
