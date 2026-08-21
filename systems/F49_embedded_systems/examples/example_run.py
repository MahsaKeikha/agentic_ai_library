"""Example embedded systems input for F49."""

EXAMPLE = {
    "product": "sensor-node",
    "interfaces": ["I2C", "BLE"],
    "timing_requirements": {"sample_period_ms": 100},
    "constraints": {"battery_powered": True},
}
