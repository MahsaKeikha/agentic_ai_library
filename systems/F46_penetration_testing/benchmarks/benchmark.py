"""Minimal benchmark harness for F46."""

def benchmark_case() -> dict:
    return {
        "authorization": True,
        "scope": ["example.local"],
        "findings": [],
        "remediation": [],
    }
