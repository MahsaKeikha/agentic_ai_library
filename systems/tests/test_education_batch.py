from systems.education_batch import SYSTEMS, run_system


def test_all_education_systems_registered():
    assert list(SYSTEMS) == [f"F{i}" for i in range(91, 101)]


def test_missing_context_is_explicit():
    result = run_system("F93", {"learner_context": "calculus student"})
    assert result.risks
    assert result.analyses["practice"]["input"] == "Unknown / evidence required"
    assert result.status == "DRAFT - HUMAN REVIEW REQUIRED"


def test_integrity_system_blocks_automatic_misconduct_finding():
    case = {role: "evidence" for role in SYSTEMS["F97"][1]}
    case["automatic_misconduct_finding"] = True
    result = run_system("F97", case, approve=True)
    assert any("prohibited" in risk for risk in result.risks)
    assert result.status == "APPROVAL REQUESTED BUT BLOCKED BY OPEN RISKS"


def test_lab_safety_issue_blocks_progression():
    case = {role: "evidence" for role in SYSTEMS["F95"][1]}
    case["unresolved_lab_safety_issue"] = "chemical storage review incomplete"
    result = run_system("F95", case, approve=True)
    assert "STOP" in result.recommendation
    assert result.status == "DRAFT - HUMAN REVIEW REQUIRED"


def test_complete_case_can_reach_human_reviewed_next_step():
    case = {role: f"verified {role}" for role in SYSTEMS["F98"][1]}
    result = run_system("F98", case, approve=True)
    assert not result.risks
    assert result.status.startswith("HUMAN REVIEW RECORDED")
