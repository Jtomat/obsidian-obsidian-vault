from dataclasses import dataclass
from enum import Enum
from typing import TypeVar, Generic, SupportsAbs, Dict, Callable, get_origin, get_args

from code.ast_tree.core.expression import Expression

T = TypeVar('T', bound=SupportsAbs[Enum])


@dataclass
class CallableOperation:
    tensor: Callable
    scalar: Callable

@dataclass
class Operation(Expression, Generic[T]):
    __enum__ = TypeVar('__enum__', bound=Enum)
    operator: T

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)

        for base in getattr(cls, "__orig_bases__", ()):
            if get_origin(base) is Operation:
                enum_type = get_args(base)[0]
                cls.__enum__ = enum_type
                break

    _operations_dict: Dict[T, CallableOperation]
