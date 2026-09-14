from enum import Enum

from code.ast_tree.expression import Expression
from typing import TypeVar, Generic, SupportsAbs

T = TypeVar('T', bound=SupportsAbs[Enum])

class Operation(Expression, Generic[T]):
    operator: T

