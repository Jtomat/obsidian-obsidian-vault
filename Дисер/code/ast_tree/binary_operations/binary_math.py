from enum import Enum
from typing import Optional, Dict, Callable, Tuple

import torch

from code.ast_tree.binary_operations.binary import BinaryOperation
from code.ast_tree.core.context import Context


class BinaryMathOperation(Enum):
    Add = "add"
    Sub = "sub"
    Mul = "mul"
    Div = "div"
    Mod = "mod"
    Pow = "pow"
    Min = "min"
    Max = "max"


import operator

BINARY_OPERATORS_FUNCS: Dict[Enum, Tuple[Callable, Callable]] = {
    BinaryMathOperation.Add: (torch.add, operator.add),
    BinaryMathOperation.Sub: (torch.sub, operator.sub),
    BinaryMathOperation.Mul: (torch.mul, operator.mul),
    BinaryMathOperation.Div: (torch.div, operator.truediv),
    BinaryMathOperation.Mod: (torch.remainder, operator.mod),
    BinaryMathOperation.Pow: (torch.pow, operator.pow),
    BinaryMathOperation.Min: (torch.minimum, min),
    BinaryMathOperation.Max: (torch.maximum, max),
}


class BinaryOperationNode(BinaryOperation[BinaryMathOperation]):
    type: str = "binary_math_operation"

    def eval(self, context: Context, local: Optional[Context] = None) -> bool | float | torch.tensor:
        left = self.left.eval(context)
        right = self.left.eval(context)

        has_tensor = bool(not (torch.is_tensor(left) or torch.is_tensor(right)))

        return BINARY_OPERATORS_FUNCS[self.operator][has_tensor](left, right)
