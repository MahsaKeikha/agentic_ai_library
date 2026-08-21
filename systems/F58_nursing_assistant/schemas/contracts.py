from dataclasses import dataclass,field
@dataclass
class NursingWorkflowContext:
    unit:str
    tasks:list[dict]=field(default_factory=list)
