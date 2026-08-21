from dataclasses import dataclass, field
@dataclass
class TrialContext:
    protocol_version: str
    sites: list[dict] = field(default_factory=list)
