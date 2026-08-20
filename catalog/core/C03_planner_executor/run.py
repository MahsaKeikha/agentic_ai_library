#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def plan() -> list[str]:
    return ["load_input", "validate", "summarize"]


def execute(steps: list[str]) -> list[str]:
    log = []
    data = (ROOT / "fixtures" / "input.txt").read_text(encoding="utf-8").strip()
    for step in steps:
        if step == "load_input":
            log.append(f"{step}: {len(data)} chars")
        elif step == "validate":
            log.append(f"{step}: {'ok' if data else 'empty'}")
        elif step == "summarize":
            log.append(f"{step}: {data[:40]}")
        else:
            log.append(f"{step}: skipped")
    return log


def main() -> int:
    steps = plan()
    log = execute(steps)
    out = "PLAN:\n" + "\n".join(f"- {s}" for s in steps) + "\n\nEXEC:\n" + "\n".join(log) + "\n"
    print(out)
    (ROOT / "fixtures" / "last_run.txt").write_text(out, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
