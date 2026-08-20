import importlib.util
from pathlib import Path


def load_module():
    path = Path(__file__).resolve().parents[1] / "run.py"
    spec = importlib.util.spec_from_file_location("f28_run", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_required_workstreams_exist():
    result = load_module().run()
    required = {"problem", "customer_discovery", "market", "product", "mvp", "gtm", "metrics", "experiments", "fundraising"}
    assert required.issubset(result)


def test_experiment_and_evidence_discipline():
    result = load_module().run()
    assert "falsifiable" in result["experiments"]
    assert "evidence gaps" in result["fundraising"]
