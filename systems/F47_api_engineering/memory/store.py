"""In-memory artifact store for F47 API Engineering."""

class MemoryStore:
    def __init__(self) -> None:
        self._items: dict[str, object] = {}

    def put(self, key: str, value: object) -> None:
        self._items[key] = value

    def get(self, key: str, default=None):
        return self._items.get(key, default)
