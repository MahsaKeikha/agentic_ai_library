def report_synthesis(context: dict) -> dict:
    return {
        "scope": context.get("authorized_assets", []),
        "finding_count": len(context.get("findings", [])),
        "human_review_required": True,
    }
