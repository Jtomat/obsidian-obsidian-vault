from typing import List

from code.backend.models.operation_node import OperationNode


class Stage:
    id: str
    name: str
    nodes: List[OperationNode]