#!/usr/bin/env python3
"""C01: single tool call loop (offline)."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent
FIXTURE = ROOT / "fixtures" / "status.txt"


def tool_read_status() -> str:
    if not FIXTURE.exists():
        return "missing fixture"
    return FIXTURE.read_text(encoding="utf-8").strip()


def agent_step_offline() -> str:
    # Stand in for: model chooses tool_read_status
    observation = tool_read_status()
    return f"tool=read_status\nobservation={observation}\naction=stop\n"


def main() -> int:
    out = agent_step_offline()
    print(out)
    (ROOT / "fixtures" / "last_run.txt").write_text(out, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
