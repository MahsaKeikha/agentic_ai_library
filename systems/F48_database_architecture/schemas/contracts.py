"""Structured input contracts for F48 Database Architecture."""

from dataclasses import dataclass, field

@dataclass
class ArchitectureInput:
    workload: str
    domains: list[str] = field(default_factory=list)
    requirements: dict = field(default_factory=dict)
    constraints: dict = field(default_factory=dict)
