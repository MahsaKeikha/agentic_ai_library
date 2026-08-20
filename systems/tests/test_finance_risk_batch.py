from systems.finance_risk_batch import SYSTEMS, run_system


def test_all_finance_risk_systems_registered():
    assert list(SYSTEMS) == [f"F{i}" for i in range(151, 161)]


def test_missing_evidence_is_explicit():
    result = run_system("F151", {"thesis": "research thesis"})
    assert result.risks
    assert result.analyses["valuation"]["input"] == "Unknown / evidence required"


def test_binding_action_is_blocked():
    case = {role: "verified" for role in SYSTEMS["F158"][1]}
    case["binding_action_requested"] = True
    result = run_system("F158", case, approve=True)
    assert any("Binding financial action" in risk for risk in result.risks)
    assert result.status == "APPROVAL REQUESTED BUT BLOCKED BY OPEN RISKS"


def test_unverified_material_claim_blocks_approval():
    case = {role: "verified" for role in SYSTEMS["F159"][1]}
    case["unverified_material_claim"] = True
    result = run_system("F159", case, approve=True)
    assert result.status == "APPROVAL REQUESTED BUT BLOCKED BY OPEN RISKS"


def test_complete_case_can_reach_controlled_step():
    case = {role: f"verified evidence for {role}" for role in SYSTEMS["F157"][1]}
    result = run_system("F157", case, approve=True)
    assert not result.risks
    assert result.status.startswith("AUTHORIZED HUMAN REVIEW RECORDED")
