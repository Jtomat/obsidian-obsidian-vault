from dataclasses import dataclass
from enum import Enum
from typing import TypeVar, SupportsAbs, Dict, Any

from code.ast_tree.ast_tree_factory import AstTreeFactory
from code.ast_tree.core.expression import Expression
from code.ast_tree.core.operation import Operation

T = TypeVar('T', bound=SupportsAbs[Enum])

@dataclass
class BinaryOperation(Operation[T]):
    left: Expression
    right: Expression

    @classmethod
    def from_dict(cls, data: Dict[str, Any], builder: AstTreeFactory) -> 'BinaryOperation':
        return cls(operator=cls.__enum__(data['operator']),
            left=builder.build(data['left']),
            right=builder.build(data['right']))
