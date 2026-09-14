from enum import Enum

from jaraco.classes.properties import classproperty

from code.ast_tree.expression import Expression
from typing import TypeVar, SupportsAbs

from code.ast_tree.operation import Operation
from code.ast_tree.types import OperatorFuncs

T = TypeVar('T', bound=SupportsAbs[Enum])

class UnaryOperation(Operation[T]):
    operand: Expression

    _operations: OperatorFuncs[T]

