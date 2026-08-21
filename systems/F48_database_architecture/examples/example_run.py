"""Example database architecture input for F48."""

EXAMPLE = {
    "workload": "transactional",
    "data_domains": ["orders", "customers"],
    "requirements": {"availability": "high", "auditing": True},
}
