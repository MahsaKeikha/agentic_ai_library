from orchestration.orchestrator import run
def test_smoke(): assert run({})['status']=='tutored'
