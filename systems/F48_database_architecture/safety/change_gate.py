"""Human approval gate for consequential F48 changes."""

def approve_change(*, reviewed: bool, rollback_ready: bool, human_approved: bool) -> bool:
    return bool(reviewed and rollback_ready and human_approved)
