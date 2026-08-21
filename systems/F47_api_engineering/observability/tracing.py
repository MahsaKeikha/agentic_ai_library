"""Trace events for F47 API Engineering."""

from dataclasses import dataclass, field
from time import time

@dataclass
class TraceEvent:
    stage: str
    detail: str
    timestamp: float = field(default_factory=time)

class TraceLog:
    def __init__(self) -> None:
        self.events: list[TraceEvent] = []

    def record(self, stage: str, detail: str) -> None:
        self.events.append(TraceEvent(stage=stage, detail=detail))
