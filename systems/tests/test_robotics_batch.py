from systems.robotics_batch import SYSTEMS, run_system


def test_all_robotics_systems_registered():
    assert list(SYSTEMS) == [f"F{i}" for i in range(71, 81)]


def test_missing_evidence_remains_explicit():
    result = run_system("F71", {"cell": "assembly cell A"})
    assert result.risks
    assert result.analyses["safety"]["input"] == "Unknown / evidence required"
    assert result.status == "DRAFT - QUALIFIED HUMAN REVIEW REQUIRED"


def test_unresolved_hazard_blocks_physical_deployment():
    case = {role: "evidence" for role in SYSTEMS["F74"][1]}
    case["unresolved_safety_hazard"] = "braking validation failure"
    result = run_system("F74", case, approve=True)
    assert "STOP" in result.recommendation
    assert result.status == "DRAFT - QUALIFIED HUMAN REVIEW REQUIRED"


def test_approval_cannot_override_missing_evidence():
    result = run_system("F75", {"mission": "inspection"}, approve=True)
    assert result.status == "APPROVAL REQUESTED BUT BLOCKED BY OPEN RISKS"


def test_complete_case_can_reach_controlled_next_step():
    case = {role: f"verified evidence for {role}" for role in SYSTEMS["F77"][1]}
    result = run_system("F77", case, approve=True)
    assert not result.risks
    assert result.status.startswith("QUALIFIED HUMAN REVIEW RECORDED")
