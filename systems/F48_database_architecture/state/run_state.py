"""Run state for F48 Database Architecture."""

from dataclasses import dataclass, field

@dataclass
class RunState:
    request: dict
    artifacts: dict = field(default_factory=dict)
    risks: list = field(default_factory=list)
    approvals: list = field(default_factory=list)
