"""Example API engineering input for F47."""

EXAMPLE = {
    "service_name": "orders-api",
    "consumers": ["web", "mobile"],
    "requirements": {"versioning": "explicit", "idempotency": True},
}
