from dataclasses import dataclass,field
@dataclass
class RehabilitationContext:
    goals:list[dict]=field(default_factory=list)
    progress:list[dict]=field(default_factory=list)
