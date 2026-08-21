from dataclasses import dataclass, field
@dataclass
class RunState:
    phase: str = "protocol"
    artifacts: dict = field(default_factory=dict)
    deviations: list = field(default_factory=list)
