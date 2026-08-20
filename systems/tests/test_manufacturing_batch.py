from systems.manufacturing_batch import SYSTEMS, run_system


def test_all_manufacturing_systems_registered():
    assert list(SYSTEMS) == [f"F{i}" for i in range(111, 121)]


def test_missing_evidence_is_explicit():
    result = run_system("F111", {"process": "assembly"})
    assert result.risks
    assert result.analyses["safety"]["input"] == "Unknown / evidence required"


def test_safety_hazard_blocks_progression():
    case = {role: "verified" for role in SYSTEMS["F118"][1]}
    case["unresolved_safety_hazard"] = "unguarded motion"
    result = run_system("F118", case, approve=True)
    assert "STOP" in result.recommendation
    assert result.status == "DRAFT - AUTHORIZED HUMAN REVIEW REQUIRED"


def test_quality_hold_blocks_approval():
    case = {role: "verified" for role in SYSTEMS["F113"][1]}
    case["quality_hold"] = True
    result = run_system("F113", case, approve=True)
    assert result.status == "APPROVAL REQUESTED BUT BLOCKED BY OPEN RISKS"


def test_complete_case_can_reach_controlled_step():
    case = {role: f"verified evidence for {role}" for role in SYSTEMS["F120"][1]}
    result = run_system("F120", case, approve=True)
    assert not result.risks
    assert result.status.startswith("AUTHORIZED HUMAN REVIEW RECORDED")
