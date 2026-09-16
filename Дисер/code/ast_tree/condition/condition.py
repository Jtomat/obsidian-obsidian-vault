from dataclasses import Field, dataclass
from typing import List, Optional, Unpack

import torch
from pydantic import ConfigDict

from code.ast_tree.condition.condition_variant import ConditionVariantNode
from code.ast_tree.core.context import Context
from code.ast_tree.core.expression import Expression
from code.ast_tree.ast_tree_factory import AstTreeFactory


@dataclass
class ConditionNode(Expression):
    variants: List[ConditionVariantNode]
    else_: Expression = Field(alias="else")
    type: str = "condition"

    def __init_subclass__(cls, **kwargs: Unpack[ConfigDict]):
        super().__init_subclass__(**kwargs)
        AstTreeFactory.register(cls.type, lambda data, builder: ConditionNode(
            variants=list(map(lambda v: builder.build(v), data['variants'])), else_=builder.build(data['else'])))

    def eval(self, context: Context, local: Optional[Context] = None) -> bool | float | torch.tensor:
        for variant in self.variants:
            if variant.condition.eval(context, local):
                return variant.eval(context, local)
        return self.else_.eval(context, local)
