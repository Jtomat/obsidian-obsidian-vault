from pathlib import Path
from typing import List, Any

from code.backend.models.resource import Resource
from code.backend.models.stage import Stage


class Project:
    id: str
    name: str
    path: Path
    description: str

    stages: List[Stage]
    resources: List[Resource]
    globals: Any
