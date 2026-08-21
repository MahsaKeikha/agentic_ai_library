"""Human approval gate for F50 fleet actions."""

def approve_fleet_action(*, staged: bool, rollback_ready: bool, human_approved: bool) -> bool:
    return bool(staged and rollback_ready and human_approved)
