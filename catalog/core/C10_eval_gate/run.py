#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def agent_reply(question: str) -> str:
    # Stand in agent
    if "tracking" in question.lower():
        return "Your tracking number is 1Z999DEMO."
    return "I can help with order status."


def main() -> int:
    lines = (ROOT / "fixtures" / "golden.txt").read_text(encoding="utf-8").splitlines()
    cases = [ln.split("|", 1) for ln in lines if "|" in ln]
    passed = 0
    for q, must_include in cases:
        reply = agent_reply(q.strip())
        ok = must_include.strip().lower() in reply.lower()
        passed += int(ok)
        print(f"{'PASS' if ok else 'FAIL'}: {q.strip()} -> {reply}")
    score = passed / max(len(cases), 1)
    print(f"score={score:.2f}")
    if score < 1.0:
        print("GATE: fail closed (do not promote)")
        return 1
    print("GATE: pass")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
