from systems.healthcare_batch import SYSTEMS, run_system


def test_all_healthcare_systems_registered():
    assert list(SYSTEMS) == [f"F{i}" for i in range(51, 61)]


def test_missing_healthcare_evidence_is_explicit():
    result = run_system("F59", {"routine": "morning and evening routine"})
    assert result.status == "DRAFT - QUALIFIED HUMAN REVIEW REQUIRED"
    assert result.escalations
    assert result.analyses["observations"]["input"] == "Unknown / evidence required"


def test_urgent_safety_concern_forces_escalation_language():
    result = run_system("F58", {"urgent_safety_concern": True})
    assert any("emergency" in item.lower() or "clinical" in item.lower() for item in result.escalations)
    assert "do not rely" in result.escalations[-1].lower()


def test_human_review_gate_changes_status_only():
    result = run_system("F56", {}, approve=True)
    assert result.status.startswith("QUALIFIED HUMAN REVIEW RECORDED")
    assert result.escalations


def test_output_preserves_non_diagnostic_boundary():
    result = run_system("F60", {})
    text = result.recommendation.lower()
    assert "diagnosis" in text
    assert "prescription" in text
    assert "qualified human reviewer" in text
