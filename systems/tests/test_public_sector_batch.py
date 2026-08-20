from systems.public_sector_batch import SYSTEMS, run_system


def test_all_public_sector_systems_registered():
    assert list(SYSTEMS) == [f"F{i}" for i in range(141, 151)]


def test_missing_evidence_is_explicit():
    result = run_system("F141", {"needs": "transit access"})
    assert result.risks
    assert result.analyses["data_governance"]["input"] == "Unknown / evidence required"


def test_targeting_request_is_blocked():
    case = {role: "evidence" for role in SYSTEMS["F148"][1]}
    case["individual_targeting_requested"] = True
    result = run_system("F148", case, approve=True)
    assert any("targeting" in risk.lower() for risk in result.risks)
    assert result.status == "APPROVAL REQUESTED BUT BLOCKED BY OPEN RISKS"


def test_election_workflow_requires_neutrality():
    case = {role: "evidence" for role in SYSTEMS["F149"][1]}
    case["partisan_positioning"] = True
    result = run_system("F149", case, approve=True)
    assert any("neutral" in risk.lower() for risk in result.risks)


def test_complete_case_can_reach_controlled_step():
    case = {role: f"verified evidence for {role}" for role in SYSTEMS["F150"][1]}
    result = run_system("F150", case, approve=True)
    assert not result.risks
    assert result.status.startswith("AUTHORIZED HUMAN REVIEW RECORDED")
