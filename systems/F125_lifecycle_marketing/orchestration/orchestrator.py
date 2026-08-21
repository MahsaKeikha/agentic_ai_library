from AGENTS import segmentation_agent,journey_agent,experiment_agent,measurement_agent,review_agent
def run(c): return {'segmentation':segmentation_agent.run(c),'journey':journey_agent.run(c),'experiment':experiment_agent.run(c),'measurement':measurement_agent.run(c),'review':review_agent.run(c)}
