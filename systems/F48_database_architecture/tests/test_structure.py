from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def test_required_layers_exist():
    for name in ["AGENTS", "TOOLS", "SKILLS", "orchestration", "memory", "state", "prompts", "config", "safety", "observability", "evals"]:
        assert (ROOT / name).exists(), name
