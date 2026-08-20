from systems.legal_compliance_batch import SYSTEMS, run_system


def test_all_legal_compliance_systems_registered():
    assert list(SYSTEMS) == [f"F{i}" for i in range(101, 111)]


def test_missing_jurisdiction_blocks_clean_review():
    result = run_system("F101", {})
    assert any("Jurisdiction" in issue for issue in result.issues)
    assert result.status == "DRAFT - PROFESSIONAL REVIEW REQUIRED"


def test_binding_action_is_blocked():
    case = {"jurisdiction": "example", "binding_action_requested": True}
    result = run_system("F110", case, approve=True)
    assert any("Binding legal/regulatory action" in issue for issue in result.issues)
    assert result.status == "APPROVAL REQUESTED BUT BLOCKED BY OPEN ISSUES"


def test_missing_evidence_is_explicit():
    result = run_system("F103", {"jurisdiction": "example", "data_map": "inventory"})
    assert result.analyses["retention"]["input"] == "Unknown / evidence required"
    assert result.issues


def test_complete_package_can_move_to_controlled_review_step():
    roles = SYSTEMS["F102"][1]
    case = {"jurisdiction": "example", **{role: f"evidence for {role}" for role in roles}}
    result = run_system("F102", case, approve=True)
    assert not result.issues
    assert result.status.startswith("PROFESSIONAL REVIEW RECORDED")
