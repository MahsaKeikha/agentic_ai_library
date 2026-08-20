from systems.marketing_growth_batch import SYSTEMS, run_system


def test_all_marketing_growth_systems_registered():
    assert list(SYSTEMS) == [f"F{i}" for i in range(121, 131)]


def test_missing_evidence_is_explicit():
    result = run_system("F122", {"topics": ["agentic AI"]})
    assert result.risks
    assert result.analyses["facts"]["input"] == "Unknown / evidence required"


def test_deceptive_claim_blocks_approval():
    case = {role: "verified" for role in SYSTEMS["F127"][1]}
    case["deceptive_claim"] = "unsupported superiority claim"
    result = run_system("F127", case, approve=True)
    assert result.status == "APPROVAL REQUESTED BUT BLOCKED BY OPEN RISKS"


def test_privacy_issue_blocks_release():
    case = {role: "verified" for role in SYSTEMS["F130"][1]}
    case["privacy_or_consent_issue"] = True
    result = run_system("F130", case, approve=True)
    assert result.status == "APPROVAL REQUESTED BUT BLOCKED BY OPEN RISKS"


def test_complete_case_can_reach_controlled_step():
    case = {role: f"verified evidence for {role}" for role in SYSTEMS["F129"][1]}
    result = run_system("F129", case, approve=True)
    assert not result.risks
    assert result.status.startswith("AUTHORIZED HUMAN REVIEW RECORDED")
