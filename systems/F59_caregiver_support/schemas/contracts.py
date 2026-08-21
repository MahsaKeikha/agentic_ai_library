from dataclasses import dataclass,field
@dataclass
class CaregiverContext:
    goals:list[str]=field(default_factory=list)
    observations:list[dict]=field(default_factory=list)
