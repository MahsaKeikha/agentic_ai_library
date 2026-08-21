from orchestration.orchestrator import run
def test_mode(): assert run({})['final_action']=='research_only'
