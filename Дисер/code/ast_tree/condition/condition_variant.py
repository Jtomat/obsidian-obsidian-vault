from dataclasses import Field, dataclass
from typing import Optional, Unpack

import torch
from pydantic import ConfigDict

from code.ast_tree.core.context import Context
from code.ast_tree.core.expression import Expression
from code.ast_tree.ast_tree_factory import AstTreeFactory


@dataclass
class ConditionVariantNode(Expression):
    condition: Expression
    then_: Expression = Field(alias="then")
    type: str = 'condition_variant'

    def __init_subclass__(cls, **kwargs: Unpack[ConfigDict]):
        super().__init_subclass__(**kwargs)

        AstTreeFactory.register(cls.type,
                                lambda data, builder: ConditionVariantNode(
                                    condition=builder.build(data['condition']),
                                    then_=builder.build(data['then']),
                                    type=cls.type))

    def eval(self, context: Context, local: Optional[Context] = None) -> bool | float | torch.tensor:
        return self.then_.eval(context.merge_with(local))
