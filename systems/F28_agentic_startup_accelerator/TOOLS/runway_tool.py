def estimate_runway(cash, monthly_burn):
    burn = float(monthly_burn or 0)
    return None if burn <= 0 else float(cash or 0) / burn
