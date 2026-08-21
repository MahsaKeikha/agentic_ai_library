"""Example IoT engineering input for F50."""

EXAMPLE = {
    "fleet_name": "environmental-sensors",
    "device_types": ["sensor-node"],
    "telemetry_requirements": {"temperature_hz": 1},
    "constraints": {"intermittent_connectivity": True},
}
