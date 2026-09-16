from typing import Dict, Callable

from code.ast_tree.core.node import Node


class AstTreeFactory:
    types = {}

    @classmethod
    def register(cls, type: str, exec: Callable[[Dict, 'AstTreeFactory'], Node]):
        cls.types[type] = exec

    @classmethod
    def build(cls, obj: Dict) -> Node:
        return cls.types[obj['type']](obj, cls)