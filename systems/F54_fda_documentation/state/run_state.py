from dataclasses import dataclass,field
@dataclass
class RunState:
    phase:str="document_intake"
    gaps:list=field(default_factory=list)
    artifacts:dict=field(default_factory=dict)
