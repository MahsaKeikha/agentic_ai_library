def capacity_plan(rows: int, bytes_per_row: int, growth_factor: float = 1.2) -> dict:
    return {"estimated_bytes": int(rows * bytes_per_row * growth_factor)}
