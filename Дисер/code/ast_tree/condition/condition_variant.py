from dataclasses import Field
from typing import Optional

import torch

from code.ast_tree.core.context import Context
from code.ast_tree.core.expression import Expression


class ConditionVariantNode(Expression):
    condition: Expression
    then_: Expression  = Field(alias="then")

    def eval(self, context: Context, local: Optional[Context]=None) -> bool | float | torch.tensor:
        return self.value.eval(context)
