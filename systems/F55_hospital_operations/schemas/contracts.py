from dataclasses import dataclass,field
@dataclass
class OperationsContext:
    unit:str
    capacity:dict=field(default_factory=dict)
