from systems.software_engineering_batch import SYSTEMS, run_system


def test_all_ten_systems_registered():
    assert list(SYSTEMS) == [f"F{i}" for i in range(41, 51)]


def test_missing_evidence_stays_explicit():
    result = run_system("F42", {"requirements": "multi-region service"})
    assert result.status == "DRAFT - HUMAN REVIEW REQUIRED"
    assert result.risks
    assert result.analyses["security"]["input"] == "Unknown / evidence required"


def test_approval_does_not_remove_risk():
    result = run_system("F49", {}, approve=True)
    assert result.status.startswith("HUMAN APPROVAL RECORDED")
    assert result.risks


def test_penetration_testing_requires_authorization():
    result = run_system("F46", {"scope": "staging web app"})
    assert any("authorization" in risk.lower() for risk in result.risks)
    assert result.recommendation.startswith("Stop")


def test_complete_case_moves_to_validation():
    case = {role: f"evidence for {role}" for role in SYSTEMS["F47"][1]}
    result = run_system("F47", case)
    assert not result.risks
    assert "expert review" in result.recommendation
