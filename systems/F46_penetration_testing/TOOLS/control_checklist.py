def summarize_controls(controls: list[dict]) -> dict:
    verified = [c for c in controls if c.get("verified")]
    return {"total": len(controls), "verified": len(verified), "unverified": len(controls) - len(verified)}
