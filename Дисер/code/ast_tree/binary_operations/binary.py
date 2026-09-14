from enum import Enum
from typing import TypeVar, SupportsAbs

from code.ast_tree.core.expression import Expression
from code.ast_tree.core.operation import Operation

T = TypeVar('T', bound=SupportsAbs[Enum])


class BinaryOperation(Operation[T]):
    left: Expression
    right: Expression
