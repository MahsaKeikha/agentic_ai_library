#!/usr/bin/env python3
import argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def send_customer_message(body: str) -> str:
    # Demo only: write to a local file instead of a real email API
    path = ROOT / "fixtures" / "sent_message.txt"
    path.write_text(body, encoding="utf-8")
    return str(path)


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--offline", action="store_true", default=True)
    p.add_argument("--approve", action="store_true", help="Human approval to perform side effect")
    args = p.parse_args()
    draft = "Your order has shipped. Tracking 1Z999DEMO.\n"
    if not args.approve:
        print("GATE: blocked. Re-run with --approve after review.")
        print("DRAFT:\n" + draft)
        return 0
    path = send_customer_message(draft)
    print(f"GATE: approved. Wrote demo send to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
