import operator
from enum import Enum
from typing import Optional

from code.ast_tree.binary_operations.binary import BinaryOperation
from code.ast_tree.core.context import Context


class BinaryComparisonOperation(Enum):
    Equal = "equal"
    Not_Equal = "not_equal"
    Less = "less"
    Less_Equal = "less_equal"
    Greater = "greater"
    Greater_Equal = "greater_equal"


COMPARISON_OPERATORS_FUNCS = {
    BinaryComparisonOperation.Equal: operator.eq,
    BinaryComparisonOperation.Not_Equal: operator.ne,
    BinaryComparisonOperation.Less: operator.lt,
    BinaryComparisonOperation.Less_Equal: operator.le,
    BinaryComparisonOperation.Greater: operator.gt,
    BinaryComparisonOperation.Greater_Equal: operator.ge,
}


class ComparisonNode(BinaryOperation[BinaryComparisonOperation]):
    type: str = "binary_comparison"

    def eval(self, context: Context, local: Optional[Context] = None) -> bool:
        left = self.left.eval(context)
        right = self.right.eval(context)

        return COMPARISON_OPERATORS_FUNCS[self.operator](left, right)
