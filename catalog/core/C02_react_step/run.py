#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def tool_count_errors(log_text: str) -> int:
    return sum(1 for line in log_text.splitlines() if "ERROR" in line)


def main() -> int:
    log_text = (ROOT / "fixtures" / "app.log").read_text(encoding="utf-8")
    thought = "Need error count before deciding severity."
    act = "tool_count_errors"
    obs = tool_count_errors(log_text)
    out = f"Thought: {thought}\nAct: {act}\nObserve: {obs}\nStop: yes\n"
    print(out)
    (ROOT / "fixtures" / "last_run.txt").write_text(out, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
