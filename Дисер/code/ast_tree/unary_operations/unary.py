from enum import Enum

from code.ast_tree.core.expression import Expression
from typing import TypeVar, SupportsAbs

from code.ast_tree.core.operation import Operation

T = TypeVar('T', bound=SupportsAbs[Enum])

class UnaryOperation(Operation[T]):
    operand: Expression

