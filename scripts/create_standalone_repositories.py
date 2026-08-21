#!/usr/bin/env python3
"""Create one real standalone GitHub repository for every F30-F170 system.

This script is intentionally run by the repository owner from a machine where the
GitHub CLI (`gh`) is authenticated. It creates independent repositories with no
runtime dependency on agentic_ai_library.

Examples:
    python scripts/create_standalone_repositories.py --dry-run
    python scripts/create_standalone_repositories.py --start 30 --end 40
    python scripts/create_standalone_repositories.py --start 30 --end 170 --push

The script is resumable. Existing repositories are skipped by default.
"""
from __future__ import annotations

import argparse
import importlib
import json
import re
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path
from typing import Dict, List, Tuple

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

OWNER = "MahsaKeikha"
BOOK_1 = "https://a.co/d/0cbZnSMi"
BOOK_2 = "https://a.co/d/07HnRY7H"

BATCH_MODULES = [
    "systems.ai_engineering_batch",
    "systems.software_engineering_batch",
    "systems.healthcare_batch",
    "systems.neuroscience_batch",
    "systems.robotics_batch",
    "systems.science_batch",
    "systems.education_batch",
    "systems.legal_compliance_batch",
    "systems.manufacturing_batch",
    "systems.marketing_growth_batch",
    "systems.creative_media_batch",
    "systems.public_sector_batch",
    "systems.finance_risk_batch",
    "systems.personal_productivity_batch",
]

F30 = (
    "Agentic Corporate Governance",
    ["intake", "calendar", "policy_register", "board_process", "decision_log", "actions", "risk", "brief"],
    "Executive and Governance",
)

DOMAIN_BY_MODULE = {
    "systems.ai_engineering_batch": "AI Engineering",
    "systems.software_engineering_batch": "Software Engineering",
    "systems.healthcare_batch": "Healthcare",
    "systems.neuroscience_batch": "Neuroscience",
    "systems.robotics_batch": "Robotics",
    "systems.science_batch": "Science",
    "systems.education_batch": "Education",
    "systems.legal_compliance_batch": "Legal and Compliance",
    "systems.manufacturing_batch": "Manufacturing",
    "systems.marketing_growth_batch": "Marketing and Growth",
    "systems.creative_media_batch": "Creative and Media",
    "systems.public_sector_batch": "Government and Public Sector",
    "systems.finance_risk_batch": "Finance and Risk",
    "systems.personal_productivity_batch": "Personal and Productivity",
}


def catalog() -> Dict[str, Tuple[str, List[str], str]]:
    data: Dict[str, Tuple[str, List[str], str]] = {"F30": F30}
    for module_name in BATCH_MODULES:
        module = importlib.import_module(module_name)
        domain = DOMAIN_BY_MODULE[module_name]
        for fid, item in module.SYSTEMS.items():
            name, roles = item[0], list(item[1])
            data[fid] = (name, roles, domain)
    return data


def slugify(name: str) -> str:
    text = name.lower().strip()
    if text.startswith("agentic "):
        text = text[8:]
    text = text.replace("&", " and ")
    text = re.sub(r"[^a-z0-9]+", "_", text).strip("_")
    return f"agentic_{text}"


def run(cmd: List[str], cwd: Path | None = None, check: bool = True) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, cwd=cwd, check=check, text=True, capture_output=True)


def gh_ready() -> bool:
    return shutil.which("gh") is not None and run(["gh", "auth", "status"], check=False).returncode == 0


def repo_exists(repo: str) -> bool:
    return run(["gh", "repo", "view", f"{OWNER}/{repo}", "--json", "name"], check=False).returncode == 0


def py_repr(value) -> str:
    return repr(value)


def render_agents(fid: str, name: str, roles: List[str]) -> str:
    return f'''"""Specialized agents for {fid} {name}."""\nfrom dataclasses import dataclass\nfrom typing import Any, Dict\n\n\n@dataclass(frozen=True)\nclass Agent:\n    name: str\n    responsibility: str\n\n    def analyze(self, case: Dict[str, Any], state: Dict[str, Any]) -> Dict[str, Any]:\n        supplied = case.get(self.name) not in (None, "", [], {{}})\n        return {{\n            "agent": self.name,\n            "responsibility": self.responsibility,\n            "input": case.get(self.name) if supplied else "Unknown / evidence required",\n            "evidence_status": "supplied" if supplied else "missing",\n        }}\n\n\nROLE_NAMES = {py_repr(roles)}\nAGENTS = [\n    Agent(role, f"Own the {{role.replace('_', ' ')}} analysis and contribute traceable state.")\n    for role in ROLE_NAMES\n]\n'''


def render_orchestrator(fid: str, name: str, domain: str) -> str:
    return f'''"""Standalone multi-agent orchestrator for {fid} {name}."""\nfrom dataclasses import dataclass, field, asdict\nfrom typing import Any, Dict, List\nfrom agents import AGENTS\n\n\n@dataclass\nclass WorkflowResult:\n    system_id: str = "{fid}"\n    system_name: str = {name!r}\n    domain: str = {domain!r}\n    analyses: Dict[str, Any] = field(default_factory=dict)\n    risks: List[str] = field(default_factory=list)\n    recommendation: str = ""\n    status: str = "DRAFT - HUMAN REVIEW REQUIRED"\n\n    def to_dict(self) -> Dict[str, Any]:\n        return asdict(self)\n\n\ndef run_system(case: Dict[str, Any] | None = None, approve: bool = False) -> WorkflowResult:\n    case = case or {{}}\n    result = WorkflowResult()\n    shared_state: Dict[str, Any] = {{"system_id": "{fid}", "domain": {domain!r}}}\n\n    for agent in AGENTS:\n        analysis = agent.analyze(case, shared_state)\n        result.analyses[agent.name] = analysis\n        shared_state[agent.name] = analysis\n\n    missing = [name for name, item in result.analyses.items() if item["evidence_status"] == "missing"]\n    if missing:\n        result.risks.append("Missing evidence for: " + ", ".join(missing))\n\n    # Cross-domain safety gates. These flags are deliberately conservative and\n    # keep consequential execution outside the reference workflow.\n    blocking_flags = [\n        "urgent_safety_concern", "unresolved_safety_hazard", "quality_hold",\n        "hazardous_experimental_request", "binding_action_request",\n        "privacy_or_consent_issue", "rights_or_provenance_issue",\n        "targeted_persuasion_request", "high_stakes_external_action",\n    ]\n    active_blocks = [flag for flag in blocking_flags if case.get(flag)]\n    if active_blocks:\n        result.risks.append("Blocking condition(s): " + ", ".join(active_blocks))\n\n    if result.risks:\n        result.recommendation = "Resolve evidence and blocking risks before consequential external action."\n    else:\n        result.recommendation = "Proceed to domain-qualified review and the next controlled step."\n\n    if approve and not result.risks:\n        result.status = "HUMAN REVIEW RECORDED - ELIGIBLE FOR NEXT CONTROLLED STEP"\n    elif approve:\n        result.status = "APPROVAL REQUESTED BUT BLOCKED BY OPEN RISKS"\n    return result\n'''


def render_run(fid: str, name: str) -> str:
    return f'''#!/usr/bin/env python3\n"""CLI for {fid} {name}."""\nimport argparse\nimport json\nfrom pathlib import Path\nfrom orchestrator import run_system\n\n\ndef main() -> None:\n    parser = argparse.ArgumentParser(description={name!r})\n    parser.add_argument("--json", default="{{}}", help="Inline JSON case")\n    parser.add_argument("--case", help="Path to a JSON case file")\n    parser.add_argument("--approve", action="store_true", help="Record human review approval")\n    args = parser.parse_args()\n    case = json.loads(Path(args.case).read_text()) if args.case else json.loads(args.json)\n    print(json.dumps(run_system(case, approve=args.approve).to_dict(), indent=2))\n\n\nif __name__ == "__main__":\n    main()\n'''


def render_test(fid: str, roles: List[str]) -> str:
    first = roles[0]
    return f'''from orchestrator import run_system\nfrom agents import AGENTS\n\n\ndef test_has_multiple_specialized_agents():\n    assert len(AGENTS) >= 4\n\ndef test_missing_evidence_is_explicit():\n    result = run_system({{{first!r}: "evidence"}})\n    assert result.risks\n\ndef test_approval_cannot_erase_open_risks():\n    result = run_system({{}}, approve=True)\n    assert "BLOCKED" in result.status\n\ndef test_complete_case_can_reach_controlled_step():\n    case = {{agent.name: f"verified evidence for {{agent.name}}" for agent in AGENTS}}\n    result = run_system(case, approve=True)\n    assert not result.risks\n    assert result.status.startswith("HUMAN REVIEW RECORDED")\n'''


def render_readme(fid: str, name: str, domain: str, roles: List[str], repo: str) -> str:
    role_lines = "\n".join(f"- **{r.replace('_', ' ').title()} Agent**" for r in roles)
    return f'''# {fid} {name}\n\nStandalone multi-agent AI reference implementation in the **{domain}** domain.\n\nThis repository is one system in Mahsa Keikha's Agentic AI Library. It is fully runnable on its own and does **not** import the umbrella `agentic_ai_library` repository at runtime.\n\n## Multi-agent team\n\n{role_lines}\n\n## Run\n\n```bash\npython run.py\npython run.py --json '{{"{roles[0]}": "example evidence"}}'\n```\n\n## Test\n\n```bash\npython -m pip install pytest\npython -m pytest -q\n```\n\n## Engineering principles\n\n- specialized agent responsibilities\n- shared traceable workflow state\n- explicit missing-evidence handling\n- deterministic offline execution\n- human approval before consequential actions\n- blocking conditions cannot be erased by approval\n\n## AI Engineering Handbook Series\n\n- Book 1: {BOOK_1}\n- Book 2: {BOOK_2}\n\n## Parent catalog\n\nhttps://github.com/{OWNER}/agentic_ai_library\n\nRepository: https://github.com/{OWNER}/{repo}\n'''


def render_pyproject(repo: str) -> str:
    return f'''[project]\nname = "{repo.replace('_', '-')}"\nversion = "0.1.0"\ndescription = "Standalone multi-agent AI reference system"\nrequires-python = ">=3.10"\n\n[tool.pytest.ini_options]\npythonpath = ["."]\ntestpaths = ["tests"]\n'''


def render_workflow() -> str:
    return '''name: tests\non:\n  push:\n  pull_request:\njobs:\n  test:\n    runs-on: ubuntu-latest\n    strategy:\n      matrix:\n        python-version: ["3.10", "3.11", "3.12"]\n    steps:\n      - uses: actions/checkout@v4\n      - uses: actions/setup-python@v5\n        with:\n          python-version: ${{ matrix.python-version }}\n      - run: python -m pip install --upgrade pip pytest\n      - run: python -m pytest -q\n'''


def write_repo(path: Path, fid: str, name: str, roles: List[str], domain: str, repo: str) -> None:
    (path / "tests").mkdir(parents=True, exist_ok=True)
    (path / ".github" / "workflows").mkdir(parents=True, exist_ok=True)
    (path / "README.md").write_text(render_readme(fid, name, domain, roles, repo), encoding="utf-8")
    (path / "agents.py").write_text(render_agents(fid, name, roles), encoding="utf-8")
    (path / "orchestrator.py").write_text(render_orchestrator(fid, name, domain), encoding="utf-8")
    (path / "run.py").write_text(render_run(fid, name), encoding="utf-8")
    (path / "tests" / "test_system.py").write_text(render_test(fid, roles), encoding="utf-8")
    (path / "pyproject.toml").write_text(render_pyproject(repo), encoding="utf-8")
    (path / ".github" / "workflows" / "tests.yml").write_text(render_workflow(), encoding="utf-8")
    (path / ".gitignore").write_text("__pycache__/\n.pytest_cache/\n*.pyc\n.venv/\n", encoding="utf-8")


def initialize_git(path: Path) -> None:
    run(["git", "init", "-b", "main"], cwd=path)
    run(["git", "add", "."], cwd=path)
    run(["git", "-c", "user.name=MahsaKeikha", "-c", "user.email=mahsa.keikha@gmail.com", "commit", "-m", "Initial standalone multi-agent system"], cwd=path)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--start", type=int, default=30)
    parser.add_argument("--end", type=int, default=170)
    parser.add_argument("--push", action="store_true", help="Actually create and push GitHub repositories")
    parser.add_argument("--dry-run", action="store_true", help="Print planned repositories without creating them")
    parser.add_argument("--delay", type=float, default=2.0, help="Seconds between repository creations")
    parser.add_argument("--no-skip-existing", action="store_true", help="Fail rather than skip an existing repository")
    args = parser.parse_args()

    if not (30 <= args.start <= args.end <= 170):
        parser.error("range must satisfy 30 <= start <= end <= 170")

    data = catalog()
    selected = [(f"F{i}", data[f"F{i}"]) for i in range(args.start, args.end + 1)]
    plan = []
    for fid, (name, roles, domain) in selected:
        repo = slugify(name)
        plan.append({"id": fid, "name": name, "repo": f"{OWNER}/{repo}", "domain": domain, "agents": roles})

    if args.dry_run or not args.push:
        print(json.dumps(plan, indent=2))
        if not args.push:
            print("\nNo repositories were created. Re-run with --push to create them.")
        return

    if not gh_ready():
        raise SystemExit("GitHub CLI is not installed/authenticated. Install `gh` and run `gh auth login` first.")

    created = []
    skipped = []
    with tempfile.TemporaryDirectory(prefix="agentic-standalone-") as tmp:
        tmp_root = Path(tmp)
        for index, (fid, (name, roles, domain)) in enumerate(selected, start=1):
            repo = slugify(name)
            full = f"{OWNER}/{repo}"
            if repo_exists(repo):
                if args.no_skip_existing:
                    raise SystemExit(f"Repository already exists: {full}")
                print(f"[{index}/{len(selected)}] SKIP {full} (already exists)")
                skipped.append(full)
                continue

            path = tmp_root / repo
            path.mkdir()
            write_repo(path, fid, name, roles, domain, repo)
            initialize_git(path)
            description = f"{fid} {name} - standalone multi-agent AI reference system"
            print(f"[{index}/{len(selected)}] CREATE {full}")
            run(["gh", "repo", "create", full, "--public", "--description", description, "--source", str(path), "--remote", "origin", "--push"])
            created.append(full)
            time.sleep(max(0.0, args.delay))

    print(json.dumps({"created": created, "skipped": skipped}, indent=2))
    print("\nNext: update agentic_ai_library/docs/AGENT_LINKS.md to the new repository URLs.")


if __name__ == "__main__":
    main()
