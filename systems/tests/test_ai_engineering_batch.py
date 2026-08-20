from systems.ai_engineering_batch import SYSTEMS, run_system


def test_all_ten_systems_registered():
    assert list(SYSTEMS) == [f"F{i}" for i in range(31, 41)]


def test_missing_evidence_is_explicit():
    result = run_system("F35", {"corpus": "docs"})
    assert result.status == "DRAFT - HUMAN REVIEW REQUIRED"
    assert result.risks
    assert result.analyses["retrieval"]["input"] == "Unknown / evidence required"


def test_human_approval_changes_gate_not_evidence():
    result = run_system("F40", {}, approve=True)
    assert result.status.startswith("HUMAN APPROVAL RECORDED")
    assert result.risks


def test_complete_case_reaches_expert_review_recommendation():
    case = {role: f"evidence for {role}" for role in SYSTEMS["F31"][1]}
    result = run_system("F31", case)
    assert not result.risks
    assert "expert review" in result.recommendation
