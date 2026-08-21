"""Data contracts for F50 IoT Engineering."""

from dataclasses import dataclass, field

@dataclass
class IoTProject:
    fleet_name: str
    device_types: list[str] = field(default_factory=list)
    telemetry_requirements: dict = field(default_factory=dict)
    constraints: dict = field(default_factory=dict)
