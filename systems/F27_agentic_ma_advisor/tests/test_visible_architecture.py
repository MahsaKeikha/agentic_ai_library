from pathlib import Path


def test_visible_architecture():
    root = Path(__file__).resolve().parents[1]
    for folder in ["AGENTS", "TOOLS", "SKILLS", "orchestration", "memory", "schemas", "prompts", "config", "safety", "observability", "evals", "benchmarks", "docs"]:
        assert (root / folder).exists(), folder
    assert len(list((root / "AGENTS").glob("*_agent.py"))) >= 5
    assert len(list((root / "TOOLS").glob("*.py"))) >= 5
    assert len(list((root / "SKILLS").glob("*.py"))) >= 5
