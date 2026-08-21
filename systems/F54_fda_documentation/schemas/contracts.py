from dataclasses import dataclass,field
@dataclass
class DocumentationContext:
    submission_type:str
    documents:list[dict]=field(default_factory=list)
