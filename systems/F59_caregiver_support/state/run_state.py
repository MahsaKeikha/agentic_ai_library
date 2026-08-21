from dataclasses import dataclass,field
@dataclass
class RunState:
    phase:str="routine"
    observations:list=field(default_factory=list)
    escalations:list=field(default_factory=list)
