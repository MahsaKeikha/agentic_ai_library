#!/usr/bin/env python3
import argparse
import os


def complete(system: str, user: str, offline: bool) -> str:
    if offline or not os.getenv("ANTHROPIC_API_KEY"):
        return f"[offline] system_len={len(system)} user_len={len(user)} reply=placeholder"
    return "[live] install anthropic and wire messages.create here"


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--offline", action="store_true", default=True)
    p.add_argument("--live", action="store_true")
    args = p.parse_args()
    offline = not args.live
    print(complete("You are a concise assistant.", "Say hello in one line.", offline))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
