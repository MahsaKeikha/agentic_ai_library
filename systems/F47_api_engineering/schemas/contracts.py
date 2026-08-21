"""Data contracts for F47 API Engineering."""

from dataclasses import dataclass, field

@dataclass
class APIProject:
    service_name: str
    consumers: list[str] = field(default_factory=list)
    requirements: dict = field(default_factory=dict)
    constraints: dict = field(default_factory=dict)
