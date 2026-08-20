#!/usr/bin/env python3
"""Unified launcher for the Agentic AI Library.

F01-F26 are standalone repositories and are surfaced with their GitHub links.
F27-F170 are executable from this umbrella repository.
"""
from __future__ import annotations

import argparse
import importlib
import importlib.util
import json
from dataclasses import asdict, is_dataclass
from pathlib import Path
from typing import Any, Dict

ROOT = Path(__file__).resolve().parent

FLAGSHIPS = {
    "F01": ("Agentic Book Writer", "agentic_book_writer"),
    "F02": ("Agentic Research Lab", "agentic_research_lab"),
    "F03": ("Agentic Biotech R&D", "agentic_biotech_rd"),
    "F04": ("Agentic Tech Support", "agentic_tech_support"),
    "F05": ("Agentic Online Shop", "agentic_online_shop"),
    "F06": ("Agentic Debug Automation", "agentic_debug_automation"),
    "F07": ("Agentic Software Design", "agentic_software_design"),
    "F08": ("Agentic CEO Assistant", "agentic_ceo_assistant"),
    "F09": ("Agentic AI Safety", "agentic_ai_safety"),
    "F10": ("Agentic PhD Assistant", "agentic_phd_assistant"),
    "F11": ("Agentic Account Manager", "agentic_account_manager"),
    "F12": ("Agentic Robotics Governance", "agentic_robotics_governance"),
    "F13": ("Agentic QA Safety Manager", "agentic_qa_safety_manager"),
    "F14": ("Agentic Client Inquiry Bot", "agentic_client_inquiry_bot"),
    "F15": ("Agentic Fullstack Web", "agentic_fullstack_web"),
    "F16": ("Agentic Engineering Professor", "agentic_engineering_professor"),
    "F17": ("Agentic Immigration Assistant", "agentic_immigration_assistant"),
    "F18": ("Agentic Real Estate", "agentic_real_estate"),
    "F19": ("Agentic Psychologist Assistant", "agentic_psychologist_assistant"),
    "F20": ("Agentic Dating Advisor", "agentic_dating_advisor"),
    "F21": ("Agentic COO Assistant", "agentic_coo_assistant"),
    "F22": ("Agentic CFO Assistant", "agentic_cfo_assistant"),
    "F23": ("Agentic Board Advisor", "agentic_board_advisor"),
    "F24": ("Agentic Chief of Staff", "agentic_chief_of_staff"),
    "F25": ("Agentic Strategy Consultant", "agentic_strategy_consultant"),
    "F26": ("Agentic Venture Capital Analyst", "agentic_venture_capital_analyst"),
}

INDIVIDUAL_UNIFIED = {
    "F27": ("Agentic M&A Advisor", "F27_agentic_ma_advisor"),
    "F28": ("Agentic Startup Accelerator", "F28_agentic_startup_accelerator"),
    "F29": ("Agentic Innovation Officer", "F29_agentic_innovation_officer"),
    "F30": ("Agentic Corporate Governance", "F30_agentic_corporate_governance"),
}

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


def _to_jsonable(value: Any) -> Any:
    if is_dataclass(value):
        return asdict(value)
    if isinstance(value, dict):
        return {k: _to_jsonable(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [_to_jsonable(v) for v in value]
    return value


def registry() -> Dict[str, Dict[str, str]]:
    items: Dict[str, Dict[str, str]] = {}
    for fid, (name, repo) in FLAGSHIPS.items():
        items[fid] = {
            "id": fid,
            "name": name,
            "kind": "standalone",
            "location": f"https://github.com/MahsaKeikha/{repo}",
        }
    for fid, (name, folder) in INDIVIDUAL_UNIFIED.items():
        items[fid] = {
            "id": fid,
            "name": name,
            "kind": "local",
            "location": f"systems/{folder}/run.py",
        }
    for module_name in BATCH_MODULES:
        try:
            module = importlib.import_module(module_name)
        except ModuleNotFoundError:
            continue
        for fid, system in module.SYSTEMS.items():
            name = system[0]
            items[fid] = {
                "id": fid,
                "name": name,
                "kind": "local",
                "location": module_name,
            }
    return dict(sorted(items.items(), key=lambda kv: int(kv[0][1:])))


def _run_individual(fid: str) -> Dict[str, Any]:
    name, folder = INDIVIDUAL_UNIFIED[fid]
    path = ROOT / "systems" / folder / "run.py"
    spec = importlib.util.spec_from_file_location(f"launcher_{fid}", path)
    if not spec or not spec.loader:
        raise RuntimeError(f"Cannot load {fid} from {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return {
        "system_id": fid,
        "system_name": name,
        "result": _to_jsonable(module.run()),
        "status": "DRAFT - HUMAN REVIEW REQUIRED",
    }


def run_agent(fid: str, case: Dict[str, Any] | None = None, approve: bool = False) -> Dict[str, Any]:
    fid = fid.upper().strip()
    case = case or {}

    if fid in FLAGSHIPS:
        name, repo = FLAGSHIPS[fid]
        return {
            "system_id": fid,
            "system_name": name,
            "status": "STANDALONE REPOSITORY",
            "message": "This flagship is maintained in its own repository. Clone/open that repository to execute it.",
            "repository": f"https://github.com/MahsaKeikha/{repo}",
        }

    if fid in INDIVIDUAL_UNIFIED:
        result = _run_individual(fid)
        if approve:
            result["status"] = "HUMAN APPROVAL RECORDED"
        return result

    for module_name in BATCH_MODULES:
        try:
            module = importlib.import_module(module_name)
        except ModuleNotFoundError:
            continue
        if fid in getattr(module, "SYSTEMS", {}):
            result = module.run_system(fid, case, approve=approve)
            return _to_jsonable(result)

    raise ValueError(f"Unknown or unavailable system ID: {fid}")


def _load_case(args: argparse.Namespace) -> Dict[str, Any]:
    if args.case:
        return json.loads(Path(args.case).read_text(encoding="utf-8"))
    if args.json:
        return json.loads(args.json)
    return {}


def main() -> None:
    parser = argparse.ArgumentParser(description="Launch any F01-F170 Agentic AI Library system")
    parser.add_argument("system", nargs="?", help="System ID, for example F35")
    parser.add_argument("--list", action="store_true", help="List all registered systems")
    parser.add_argument("--case", help="Path to JSON input case")
    parser.add_argument("--json", help="Inline JSON input case")
    parser.add_argument("--approve", action="store_true", help="Record the human approval flag")
    args = parser.parse_args()

    if args.list:
        for item in registry().values():
            print(f"{item['id']:>4}  {item['name']:<40} {item['kind']}")
        return

    if not args.system:
        parser.error("provide a system ID such as F35, or use --list")

    output = run_agent(args.system, _load_case(args), approve=args.approve)
    print(json.dumps(output, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
