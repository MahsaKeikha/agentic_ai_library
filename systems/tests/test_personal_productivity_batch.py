from systems.personal_productivity_batch import SYSTEMS, run_system


def test_all_personal_systems_registered():
    assert list(SYSTEMS) == [f"F{i}" for i in range(161, 171)]


def test_missing_context_is_explicit():
    result = run_system("F161", {"goals": "improve work-life balance"})
    assert result.risks
    assert result.analyses["values"]["input"] == "Unknown / user context required"


def test_high_stakes_decision_blocks_generic_approval():
    case = {role: "supplied" for role in SYSTEMS["F163"][1]}
    case["high_stakes_decision"] = True
    result = run_system("F163", case, approve=True)
    assert result.status == "APPROVAL REQUESTED BUT BLOCKED BY OPEN RISKS"


def test_external_action_requires_explicit_authorization():
    case = {role: "supplied" for role in SYSTEMS["F169"][1]}
    case["external_action_requested"] = True
    result = run_system("F169", case, approve=True)
    assert any("External action" in risk for risk in result.risks)


def test_complete_case_can_reach_user_controlled_step():
    case = {role: f"user context for {role}" for role in SYSTEMS["F170"][1]}
    result = run_system("F170", case, approve=True)
    assert not result.risks
    assert result.status.startswith("HUMAN REVIEW RECORDED")
