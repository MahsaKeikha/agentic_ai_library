import importlib.util
from pathlib import Path


def load_module():
    path = Path(__file__).resolve().parents[1] / "run.py"
    spec = importlib.util.spec_from_file_location("f29_run", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_required_workstreams_exist():
    result = load_module().run()
    required = {"opportunities", "technology", "alignment", "experiments", "portfolio", "risk", "resources", "executive_brief"}
    assert required.issubset(result)


def test_human_control_language_exists():
    result = load_module().run()
    assert "without committing budget or people" in result["resources"]
    assert "human review" in result["executive_brief"]
