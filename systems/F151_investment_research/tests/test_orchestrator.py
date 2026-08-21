from orchestration.orchestrator import run
def test_gate(): assert run({})['final_action']=='human_review'
