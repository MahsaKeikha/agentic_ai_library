#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parent
NOTES = ROOT / "fixtures" / "notes"
NOTES.mkdir(parents=True, exist_ok=True)


def remember(key: str, content: str) -> Path:
    path = NOTES / f"{key}.md"
    path.write_text(content, encoding="utf-8")
    return path


def recall(key: str) -> str:
    path = NOTES / f"{key}.md"
    return path.read_text(encoding="utf-8") if path.exists() else ""


def main() -> int:
    remember("ticket_intake", "Product CloudSync. Symptom login loop after SSO change.")
    remember("priority", "P2")
    text = f"intake:\n{recall('ticket_intake')}\n\npriority:\n{recall('priority')}\n"
    print(text)
    (ROOT / "fixtures" / "last_run.txt").write_text(text, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
