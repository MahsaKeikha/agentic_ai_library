from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def test_layers():
    for name in ["AGENTS","TOOLS","SKILLS","orchestration","memory","state","schemas","prompts","config","safety","observability","evals","benchmarks","examples","docs"]: assert (ROOT/name).exists(), name
