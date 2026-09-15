from enum import Enum
from typing import Optional, Dict, Callable, Tuple

import torch

from code.ast_tree.core.context import Context
from code.ast_tree.unary_operations.unary import UnaryOperation


class UnaryLogicOperation(Enum):
    Not = "not"
    Cast = "cast"



UNARY_OPERATORS_FUNCS: Dict[Enum, Tuple[Callable, Callable]] = {
    UnaryLogicOperation.Not: (lambda value: not value, torch.logical_not),
    UnaryLogicOperation.Cast: (bool, torch.Tensor.bool),
}


class UnaryLogicOperationNode(UnaryOperation[UnaryLogicOperation]):
    type: str = 'unary_logic_operation'

    def eval(self, context: Context, local: Optional[Context] = None) -> bool | float | torch.tensor:
        base_val = self.operand.eval(context)

        to_exec = UNARY_OPERATORS_FUNCS[self.operator][bool(not torch.is_tensor(base_val))]

        return to_exec(base_val)