from pathlib import Path


class Resource:
    id: str
    name: str
    uri: Path

    def read(self):
        pass