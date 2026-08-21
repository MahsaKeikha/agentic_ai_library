"""Run state for F47 API Engineering."""

from dataclasses import dataclass, field

@dataclass
class RunState:
    request: dict
    artifacts: dict = field(default_factory=dict)
    findings: list = field(default_factory=list)
    approvals: list = field(default_factory=list)
