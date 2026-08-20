#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def build_package(ticket_id: str, symptom: str, steps_tried: list[str]) -> str:
    lines = [
        f"ticket: {ticket_id}",
        f"symptom: {symptom}",
        "steps_tried:",
        *[f"  - {s}" for s in steps_tried],
        "ask_of_specialist: confirm IdP certificate rotation window",
    ]
    return "\n".join(lines) + "\n"


def main() -> int:
    pkg = build_package(
        "T-1001",
        "SSO login loop after certificate change",
        ["cleared local session", "reproduced in Chrome"],
    )
    path = ROOT / "fixtures" / "escalation.txt"
    path.write_text(pkg, encoding="utf-8")
    print(pkg)
    print(f"wrote {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
