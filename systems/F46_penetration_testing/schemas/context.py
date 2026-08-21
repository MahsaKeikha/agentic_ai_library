from dataclasses import dataclass, field

@dataclass
class AssessmentContext:
    written_authorization: bool = False
    authorized_assets: list[str] = field(default_factory=list)
    requested_assets: list[str] = field(default_factory=list)
    controls: list[dict] = field(default_factory=list)
    findings: list[dict] = field(default_factory=list)
