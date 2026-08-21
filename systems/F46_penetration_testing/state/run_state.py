from dataclasses import dataclass, field

@dataclass
class RunState:
    authorized: bool = False
    phase: str = "intake"
    findings: list[dict] = field(default_factory=list)
