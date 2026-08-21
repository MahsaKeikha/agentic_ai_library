from orchestration.orchestrator import run
def test_gate(): assert not run({})['review']['approved']
