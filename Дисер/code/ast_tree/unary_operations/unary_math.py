from enum import Enum
from typing import Optional

import torch

from code.ast_tree.context import Context
from code.ast_tree.expression import Expression


class UnaryOperation(Enum):
    Negate = "negate"
    Abs = "abs"
    Sqrt = "sqrt"
    Sin = "sin"
    Cos = "cos"
    Tan = "tan"
    Exp = "exp"
    Log = "log"
    Floor = "floor"
    Ceil = "ceil"


import math

UNARY_OPERATORS_FUNCS = {
    UnaryOperation.Negate: (torch.neg, lambda x: -x),
    UnaryOperation.Abs: (torch.abs, abs),
    UnaryOperation.Sqrt: (torch.sqrt, math.sqrt),
    UnaryOperation.Sin: (torch.sin, math.sin),
    UnaryOperation.Cos: (torch.cos, math.cos),
    UnaryOperation.Tan: (torch.tan, math.tan),
    UnaryOperation.Exp: (torch.exp, math.exp),
    UnaryOperation.Log: (torch.log, math.log),
    UnaryOperation.Floor: (torch.floor, math.floor),
    UnaryOperation.Ceil: (torch.ceil, math.ceil),
}


class UnaryMathOperationNode(Expression):
    type: str = 'unary_math_operation'

    operator: UnaryOperation
    operand: Expression

    def eval(self, context: Context, local: Optional[Context] = None) -> int | float | torch.tensor:
        base_val = self.operand.eval(context)
        to_exec = UNARY_OPERATORS_FUNCS[self.operator][int(not torch.is_tensor(base_val))]

        return to_exec(base_val)