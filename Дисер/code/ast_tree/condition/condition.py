from dataclasses import Field
from typing import List, Optional

import torch

from code.ast_tree.condition.condition_variant import ConditionVariantNode
from code.ast_tree.core.context import Context
from code.ast_tree.core.expression import Expression


class ConditionNode(Expression):
    variants: List[ConditionVariantNode]
    else_: Expression = Field(alias="else")

    def eval(self, context: Context, local: Optional[Context] = None) -> bool | float | torch.tensor:
        for variant in self.variants:
            if variant.condition.eval(context, local):
                return variant.eval(context, local)
        return self.else_.eval(context, local)
