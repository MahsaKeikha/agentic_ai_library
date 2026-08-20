import launcher


def test_registry_covers_f01_to_f170():
    reg = launcher.registry()
    expected = {f"F{i:02d}" if i < 100 else f"F{i}" for i in range(1, 171)}
    assert set(reg) == expected


def test_flagship_returns_repository_pointer():
    result = launcher.run_agent("F01")
    assert result["status"] == "STANDALONE REPOSITORY"
    assert "github.com/MahsaKeikha/agentic_book_writer" in result["repository"]


def test_individual_unified_system_runs():
    result = launcher.run_agent("F27")
    assert result["system_id"] == "F27"
    assert result["result"]


def test_batch_system_runs_with_explicit_missing_evidence():
    result = launcher.run_agent("F35", {"corpus": "sample documents"})
    assert result["system_id"] == "F35"
    assert result["analyses"]
    assert result["risks"]


def test_unknown_id_is_rejected():
    try:
        launcher.run_agent("F999")
    except ValueError:
        pass
    else:
        raise AssertionError("Unknown system ID should raise ValueError")
