from dataclasses import dataclass,field
@dataclass
class RadiologyWorkflowContext:
    study_id:str
    metadata:dict=field(default_factory=dict)
