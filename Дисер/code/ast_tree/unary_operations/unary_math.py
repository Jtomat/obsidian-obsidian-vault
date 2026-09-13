import math
from enum import Enum
from typing import Optional, Dict

import torch

from code.ast_tree.context import Context
from code.ast_tree.unary_operations.unary import UnaryOperation


class UnaryMathOperation(Enum):
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



UNARY_OPERATORS_FUNCS: Dict[Enum, (callable, callable)] = {
    UnaryMathOperation.Negate: (torch.neg, lambda x: -x),
    UnaryMathOperation.Abs: (torch.abs, abs),
    UnaryMathOperation.Sqrt: (torch.sqrt, math.sqrt),
    UnaryMathOperation.Sin: (torch.sin, math.sin),
    UnaryMathOperation.Cos: (torch.cos, math.cos),
    UnaryMathOperation.Tan: (torch.tan, math.tan),
    UnaryMathOperation.Exp: (torch.exp, math.exp),
    UnaryMathOperation.Log: (torch.log, math.log),
    UnaryMathOperation.Floor: (torch.floor, math.floor),
    UnaryMathOperation.Ceil: (torch.ceil, math.ceil),
}


class UnaryMathOperationNode(UnaryOperation[UnaryMathOperation]):
    type: str = 'unary_math_operation'

    def eval(self, context: Context, local: Optional[Context] = None) -> int | float | torch.tensor:
        base_val = self.operand.eval(context)

        to_exec = UNARY_OPERATORS_FUNCS[self.operator][int(not torch.is_tensor(base_val))]

        return to_exec(base_val)