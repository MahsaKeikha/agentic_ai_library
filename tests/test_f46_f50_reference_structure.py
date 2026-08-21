from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

SYSTEMS = {
    "F46_penetration_testing",
    "F47_api_engineering",
    "F48_database_architecture",
    "F49_embedded_systems",
    "F50_iot_engineering",
}

REQUIRED = {
    "AGENTS",
    "TOOLS",
    "SKILLS",
    "orchestration",
    "memory",
    "state",
    "schemas",
    "prompts",
    "config",
    "safety",
    "observability",
    "evals",
    "benchmarks",
    "examples",
    "tests",
    "docs",
}


def test_reference_layers_exist():
    for system in SYSTEMS:
        base = ROOT / "systems" / system
        assert base.exists(), system
        for layer in REQUIRED:
            assert (base / layer).exists(), f"{system}/{layer}"


def test_each_system_has_multiple_agents_tools_and_skills():
    for system in SYSTEMS:
        base = ROOT / "systems" / system
        assert len(list((base / "AGENTS").glob("*.py"))) >= 5, system
        assert len(list((base / "TOOLS").glob("*.py"))) >= 5, system
        assert len(list((base / "SKILLS").glob("*.py"))) >= 5, system
