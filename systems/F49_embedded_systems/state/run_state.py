"""Run state for F49 Embedded Systems."""

from dataclasses import dataclass, field

@dataclass
class RunState:
    request: dict
    artifacts: dict = field(default_factory=dict)
    verification_results: list = field(default_factory=list)
    approvals: list = field(default_factory=list)
