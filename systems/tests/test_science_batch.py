from systems.science_batch import SYSTEMS, run_system


def test_all_science_systems_registered():
    assert list(SYSTEMS) == [f"F{i}" for i in range(81, 91)]


def test_missing_evidence_is_explicit():
    result = run_system("F81", {"problem": "test hypothesis"})
    assert result.risks
    assert result.analyses["literature"]["input"] == "Unknown / evidence required"
    assert result.status == "DRAFT - HUMAN REVIEW REQUIRED"


def test_hazardous_execution_request_is_blocked():
    case = {role: "evidence" for role in SYSTEMS["F84"][1]}
    case["hazardous_experimental_request"] = True
    result = run_system("F84", case, approve=True)
    assert result.risks
    assert "outside this reference workflow" in result.recommendation
    assert result.status == "DRAFT - HUMAN REVIEW REQUIRED"


def test_approval_cannot_override_open_risks():
    result = run_system("F89", {"requirements": "high-level system requirements"}, approve=True)
    assert result.status == "APPROVAL REQUESTED BUT BLOCKED BY OPEN RISKS"


def test_complete_case_reaches_controlled_next_step():
    case = {role: f"verified evidence for {role}" for role in SYSTEMS["F90"][1]}
    result = run_system("F90", case, approve=True)
    assert not result.risks
    assert result.status.startswith("HUMAN REVIEW RECORDED")
