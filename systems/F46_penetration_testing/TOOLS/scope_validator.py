def validate_scope(requested_assets: list[str], authorized_assets: list[str]) -> dict:
    allowed = set(authorized_assets)
    requested = set(requested_assets)
    return {"authorized": sorted(requested & allowed), "blocked": sorted(requested - allowed)}
