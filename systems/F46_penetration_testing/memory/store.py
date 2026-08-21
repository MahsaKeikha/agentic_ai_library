from dataclasses import dataclass, field
from typing import Any

@dataclass
class MemoryStore:
    records: list[dict[str, Any]] = field(default_factory=list)

    def add(self, record: dict[str, Any]) -> None:
        self.records.append(record)
