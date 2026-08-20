#!/usr/bin/env python3
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def load_checklist(path: Path) -> list[tuple[str, bool]]:
    items = []
    for line in path.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^-\s+\[([ xX])\]\s+(.+)$", line)
        if m:
            items.append((m.group(2).strip(), m.group(1).lower() == "x"))
    return items


def main() -> int:
    draft = (ROOT / "fixtures" / "draft.txt").read_text(encoding="utf-8")
    items = load_checklist(ROOT / "fixtures" / "checklist.md")
    # Offline: mark clarity done if sentences are short
    short = all(len(s.split()) < 20 for s in draft.split(".") if s.strip())
    report = []
    pending = 0
    for text, done in items:
        if "Clarity" in text:
            done = short
        if not done:
            pending += 1
        mark = "x" if done else " "
        report.append(f"- [{mark}] {text}")
    out = "DRAFT:\n" + draft + "\nCHECKLIST:\n" + "\n".join(report) + f"\n\nPending: {pending}\n"
    print(out)
    (ROOT / "fixtures" / "last_run.txt").write_text(out, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
