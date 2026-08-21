"""Data contracts for F49 Embedded Systems."""

from dataclasses import dataclass, field

@dataclass
class EmbeddedProject:
    product: str
    interfaces: list[str] = field(default_factory=list)
    timing_requirements: dict = field(default_factory=dict)
    constraints: dict = field(default_factory=dict)
