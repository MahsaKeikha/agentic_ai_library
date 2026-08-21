from dataclasses import dataclass,field
@dataclass
class RunState:
    phase:str="requirements"
    evidence:dict=field(default_factory=dict)
    risks:list=field(default_factory=list)
