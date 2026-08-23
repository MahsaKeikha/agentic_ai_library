import json
from pathlib import Path

import pytest

from assessment_engine.engine import AssessmentError, assess, executive_markdown, run, technical_markdown


SAMPLE = Path(__file__).with_name("sample_input.json")


def load_sample():
    return json.loads(SAMPLE.read_text(encoding="utf-8"))


def test_sample_is_scored_and_blocked():
    result = assess(load_sample())
    assert result["overall_score"] == 67
    assert result["maturity_band"] == "Managed"
    assert result["evidence_completeness"] == 100
    assert len(result["critical_blockers"]) == 2
    assert result["gold_standard_candidate"] is False
    assert result["production_recommendation"].startswith("Not production-ready")


def test_gold_candidate_requires_no_blockers_and_evidence():
    data = load_sample()
    data["scores"] = {key: 95 for key in data["scores"]}
    data["findings"] = []
    result = assess(data)
    assert result["overall_score"] == 95
    assert result["maturity_band"] == "Gold Standard Candidate"
    assert result["gold_standard_candidate"] is True


def test_high_score_with_critical_blocker_is_not_gold():
    data = load_sample()
    data["scores"] = {key: 98 for key in data["scores"]}
    result = assess(data)
    assert result["overall_score"] == 98
    assert result["maturity_band"] == "Production Candidate"
    assert result["gold_standard_candidate"] is False


def test_high_score_without_sufficient_evidence_is_not_gold():
    data = load_sample()
    data["scores"] = {key: 95 for key in data["scores"]}
    data["findings"] = []
    data["evidence"] = {"architecture": "reviewed"}
    result = assess(data)
    assert result["evidence_completeness"] == 10
    assert result["maturity_band"] == "Production Candidate"
    assert result["gold_standard_candidate"] is False


def test_invalid_score_fails_closed():
    data = load_sample()
    data["scores"]["evaluation"] = 101
    with pytest.raises(AssessmentError):
        assess(data)


def test_missing_pillar_fails_closed():
    data = load_sample()
    del data["scores"]["human_authority"]
    with pytest.raises(AssessmentError):
        assess(data)


def test_reports_include_decision_and_findings():
    result = assess(load_sample())
    executive = executive_markdown(result)
    technical = technical_markdown(result)
    assert "67 / 100" in executive
    assert "P0-1" in executive
    assert "P0-1" in technical
    assert "Pillar scorecard" in technical


def test_run_creates_three_delivery_artifacts(tmp_path):
    result = run(str(SAMPLE), str(tmp_path))
    assert result["overall_score"] == 67
    assert (tmp_path / "assessment.json").exists()
    assert (tmp_path / "executive_report.md").exists()
    assert (tmp_path / "technical_report.md").exists()
