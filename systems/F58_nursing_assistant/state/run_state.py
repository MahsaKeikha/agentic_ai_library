from dataclasses import dataclass,field
@dataclass
class RunState:
    phase:str="tasks"
    artifacts:dict=field(default_factory=dict)
    escalations:list=field(default_factory=list)
