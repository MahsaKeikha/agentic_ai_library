from AGENTS import story_agent,storyboard_agent,character_agent,motion_agent,review_agent
def run(c): return {'story':story_agent.run(c),'storyboard':storyboard_agent.run(c),'characters':character_agent.run(c),'motion':motion_agent.run(c),'review':review_agent.run(c)}
