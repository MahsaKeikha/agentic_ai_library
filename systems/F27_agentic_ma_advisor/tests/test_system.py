import importlib.util
from pathlib import Path


def load_module():
    path = Path(__file__).resolve().parents[1] / "run.py"
    spec = importlib.util.spec_from_file_location("f27_run", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_required_workstreams_exist():
    result = load_module().run()
    required = {"target_intake", "strategic_fit", "financial_review", "synergy", "integration_risk", "diligence", "deal_memo"}
    assert required.issubset(result)


def test_evidence_discipline_is_explicit():
    result = load_module().run()
    assert "without inventing missing facts" in result["financial_review"]
    assert "hypotheses" in result["synergy"]
