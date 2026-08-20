import importlib.util
from pathlib import Path


def load_module():
    path = Path(__file__).resolve().parents[1] / "run.py"
    spec = importlib.util.spec_from_file_location("f30_run", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_required_workstreams_exist():
    result = load_module().run()
    required = {"intake", "calendar", "policy_register", "board_process", "decision_log", "actions", "risk", "brief"}
    assert required.issubset(result)


def test_governance_boundaries_are_explicit():
    result = load_module().run()
    assert "human/legal review" in result["risk"]
    assert "without certifying compliance" in result["brief"]
