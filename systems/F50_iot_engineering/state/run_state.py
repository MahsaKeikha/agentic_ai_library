"""Run state for F50 IoT Engineering."""

from dataclasses import dataclass, field

@dataclass
class RunState:
    request: dict
    artifacts: dict = field(default_factory=dict)
    fleet_findings: list = field(default_factory=list)
    approvals: list = field(default_factory=list)
