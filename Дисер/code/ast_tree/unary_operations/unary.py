from dataclasses import dataclass
from enum import Enum

import torch
from code.ast_tree.core.context import Context
from code.ast_tree.core.expression import Expression
from typing import TypeVar, SupportsAbs, Optional

from code.ast_tree.core.operation import Operation

T = TypeVar('T', bound=SupportsAbs[Enum])

# TODO
@dataclass
class UnaryOperation(Operation[T]):
    operand: Expression

    def eval(self, context: Context, local: Optional[Context] = None) -> bool | float | torch.tensor:
        run_time = context.merge_with(local)

        value = self.operand.eval(run_time)

        has_tenor = self.operand.eval(run_time)

        funcs = self._operations_dict[self.operator]

        return funcs.tensor(value) if has_tenor else funcs.scalar(value)
