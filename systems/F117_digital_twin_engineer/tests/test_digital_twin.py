from datetime import datetime, timedelta, timezone

import pytest

from systems.F117_digital_twin_engineer.digital_twin import TwinInputError, run_twin


NOW = datetime(2026, 8, 24, 10, 0, tzinfo=timezone.utc)


def anomaly_case():
    return {"asset_id": "PACKAGING-LINE-2-MOTOR-07", "observed_at": NOW.isoformat(), "temperature_c": 97.0, "vibration_mm_s": 7.6, "current_a": 34.2, "speed_rpm": 1768.0, "throughput_units_min": 118.0, "source": "synthetic://f117/motor-anomaly/v1"}


def test_anomaly_recommends_protected_stop_without_command():
    result = run_twin(anomaly_case(), now=NOW)
    assert result.state["condition"] == "TRIP_THRESHOLD_EXCEEDED"
    assert result.recommendation["action"] == "controlled_stop_and_inspection"
    assert result.status == "AWAITING AUTHORIZED ENGINEER APPROVAL"
    assert result.governance["command_issued"] is False
    assert result.governance["execution_blocked"] is True


def test_authorized_approval_records_next_step_but_still_issues_no_command():
    case = anomaly_case()
    case["approval"] = {"approved": True, "role": "authorized_engineer", "approver": "Demo Engineer", "procedure_reference": "DEMO-SOP-017"}
    result = run_twin(case, now=NOW)
    assert result.status == "AUTHORIZED FOR SITE PROCEDURE - NO COMMAND ISSUED"
    assert result.governance["approval_valid"] is True
    assert result.governance["command_issued"] is False


def test_incomplete_or_wrong_role_approval_fails_closed():
    case = anomaly_case()
    case["approval"] = {"approved": True, "role": "operator", "approver": "Demo"}
    assert run_twin(case, now=NOW).governance["execution_blocked"] is True


def test_missing_sensor_contract_is_rejected():
    case = anomaly_case()
    del case["vibration_mm_s"]
    with pytest.raises(TwinInputError, match="Missing telemetry fields"):
        run_twin(case, now=NOW)


def test_stale_telemetry_is_rejected():
    case = anomaly_case()
    case["observed_at"] = (NOW - timedelta(minutes=5)).isoformat()
    with pytest.raises(TwinInputError, match="stale"):
        run_twin(case, now=NOW)


def test_nominal_state_remains_decision_support_only():
    case = anomaly_case()
    case.update(temperature_c=58.0, vibration_mm_s=2.0, current_a=20.0)
    result = run_twin(case, now=NOW)
    assert result.state["condition"] == "NOMINAL"
    assert result.recommendation["action"] == "continue_and_monitor"
    assert result.governance["protected_action"] is False
    assert result.status == "DECISION SUPPORT COMPLETE"


def test_simulations_and_trace_are_reproducible():
    first = run_twin(anomaly_case(), now=NOW).to_dict()
    second = run_twin(anomaly_case(), now=NOW).to_dict()
    assert first == second
    assert [item["option"] for item in first["simulations"]] == ["continue_and_monitor", "derate_to_70_percent", "controlled_stop_and_inspection"]
    assert [event["sequence"] for event in first["trace"]] == [1, 2, 3, 4, 5]
    assert all(event["evidence"] for event in first["trace"])
