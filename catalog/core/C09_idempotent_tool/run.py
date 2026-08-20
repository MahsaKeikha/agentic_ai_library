#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parent
LEDGER = ROOT / "fixtures" / "ledger.txt"


def apply_credit(idem_key: str, amount: int) -> str:
    LEDGER.parent.mkdir(parents=True, exist_ok=True)
    done = set()
    if LEDGER.exists():
        done = {line.split()[0] for line in LEDGER.read_text(encoding="utf-8").splitlines() if line.strip()}
    if idem_key in done:
        return f"skip duplicate key={idem_key}"
    with LEDGER.open("a", encoding="utf-8") as f:
        f.write(f"{idem_key} credit {amount}\n")
    return f"applied key={idem_key} amount={amount}"


def main() -> int:
    print(apply_credit("refund-ORD-5001", 28))
    print(apply_credit("refund-ORD-5001", 28))
    print(LEDGER.read_text(encoding="utf-8"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
