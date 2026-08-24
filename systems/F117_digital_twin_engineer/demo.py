#!/usr/bin/env python3
"""Run the F117 flagship digital-twin demonstration."""
import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

from digital_twin import TwinInputError, run_twin


HERE = Path(__file__).resolve().parent


def main() -> None:
    parser = argparse.ArgumentParser(description="F117 deterministic digital-twin flagship demonstration")
    parser.add_argument("--case", default=str(HERE / "examples" / "motor_anomaly.json"))
    parser.add_argument("--approve", action="store_true", help="Record a synthetic authorized-engineer approval")
    args = parser.parse_args()
    case = json.loads(Path(args.case).read_text(encoding="utf-8"))
    if args.approve:
        case["approval"] = {"approved": True, "role": "authorized_engineer", "approver": "Synthetic Demo Engineer", "procedure_reference": "DEMO-SOP-017"}
    try:
        observed = datetime.fromisoformat(case["observed_at"].replace("Z", "+00:00"))
        result = run_twin(case, now=observed.astimezone(timezone.utc))
    except TwinInputError as exc:
        raise SystemExit(f"INPUT BLOCKED: {exc}") from exc
    print(json.dumps(result.to_dict(), indent=2))


if __name__ == "__main__":
    main()
