import operator
from enum import Enum

import torch

from code.ast_tree.binary_operations.binary import BinaryOperation
from code.ast_tree.core.context import Context


class BinaryLogicalOperator(Enum):
    And = 'and',
    Or = 'or',

BINARY_LOGICAL_FUNCS = {
    BinaryLogicalOperator.And: operator.and_,
    BinaryLogicalOperator.Or: operator.or_,
}


class BinaryLogicalOperationNode(BinaryOperation[BinaryLogicalOperator]):
    type: str = "logical_operation"


    def eval(self, context: Context) -> bool | float | torch.tensor:
        left = self.left.eval(context)
        right = self.right.eval(context)

        return BINARY_LOGICAL_FUNCS[self.operator](left, right)