from systems.creative_media_batch import SYSTEMS, run_system


def test_all_creative_systems_registered():
    assert list(SYSTEMS) == [f"F{i}" for i in range(131, 141)]


def test_missing_inputs_are_explicit():
    result = run_system("F131", {"manuscript": "draft", "rights_status": "original"})
    assert result.risks
    assert result.analyses["metadata"]["input"] == "Unknown / creative input required"


def test_uncleared_rights_block_release():
    case = {role: "ready" for role in SYSTEMS["F133"][1]}
    case["rights_status"] = "unknown"
    result = run_system("F133", case, approve=True)
    assert "Rights/provenance" in result.risks[0]
    assert result.status == "APPROVAL REQUESTED BUT BLOCKED BY OPEN RISKS"


def test_accessibility_blocker_prevents_release():
    case = {role: "ready" for role in SYSTEMS["F135"][1]}
    case["rights_status"] = "original"
    case["accessibility_blocker"] = True
    result = run_system("F135", case, approve=True)
    assert result.status == "APPROVAL REQUESTED BUT BLOCKED BY OPEN RISKS"


def test_complete_case_can_reach_controlled_release():
    case = {role: f"reviewed {role}" for role in SYSTEMS["F140"][1]}
    case["rights_status"] = "cleared"
    result = run_system("F140", case, approve=True)
    assert not result.risks
    assert result.status.startswith("HUMAN REVIEW RECORDED")
