from dataclasses import dataclass, field

@dataclass
class InnovationContext:
    objective: str
    evidence: dict = field(default_factory=dict)
    approvals: dict = field(default_factory=dict)
