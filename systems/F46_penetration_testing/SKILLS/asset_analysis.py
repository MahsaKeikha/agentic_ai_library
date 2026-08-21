def asset_analysis(context: dict) -> dict:
    assets = context.get("authorized_assets", [])
    return {"asset_count": len(assets), "coverage_target": assets}
