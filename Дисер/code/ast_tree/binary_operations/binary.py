from dataclasses import dataclass
from enum import Enum
from typing import TypeVar, SupportsAbs, Unpack

from pydantic import ConfigDict

from code.ast_tree.core.expression import Expression
from code.ast_tree.core.operation import Operation
from code.ast_tree.ast_tree_factory import AstTreeFactory

T = TypeVar('T', bound=SupportsAbs[Enum])

@dataclass
class BinaryOperation(Operation[T]):
    left: Expression
    right: Expression

    def __init_subclass__(cls, **kwargs: Unpack[ConfigDict]):
        super().__init_subclass__(**kwargs)
        AstTreeFactory.register(cls.type, lambda data, builder: build(cls, data, builder))


def build(cls,data, builder):
    print(data)
    return BinaryOperation(type=data['type'], operator=cls.__enum__(data['operator']),
                        left=builder.build(data['left']),
                        right=builder.build(data['right']))