from systems.neuroscience_batch import SYSTEMS, run_system


def test_all_ten_neuroscience_systems_registered():
    assert list(SYSTEMS) == [f"F{i}" for i in range(61, 71)]


def test_missing_evidence_is_not_invented():
    result = run_system("F64", {"data_quality": "checked"})
    assert result.analyses["preprocessing"]["input"] == "Unknown / evidence required"
    assert result.uncertainties
    assert result.status == "DRAFT - QUALIFIED HUMAN REVIEW REQUIRED"


def test_urgent_safety_signal_forces_escalation():
    result = run_system("F63", {"observations": "new event", "urgent_safety_signal": True})
    assert result.escalations
    assert "safety escalation" in result.recommendation


def test_human_review_does_not_remove_uncertainty():
    result = run_system("F62", {}, approve=True)
    assert result.status.startswith("QUALIFIED HUMAN REVIEW RECORDED")
    assert result.uncertainties


def test_complete_research_case_reaches_expert_review():
    roles = SYSTEMS["F69"][1]
    case = {role: f"evidence for {role}" for role in roles}
    result = run_system("F69", case)
    assert not result.uncertainties
    assert "domain-expert review" in result.recommendation
