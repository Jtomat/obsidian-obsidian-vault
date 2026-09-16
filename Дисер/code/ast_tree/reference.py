from dataclasses import dataclass
from typing import Optional, Unpack

import torch
from pydantic import ConfigDict

from code.ast_tree.core.context import Context
from code.ast_tree.core.expression import Expression
from code.ast_tree.ast_tree_factory import AstTreeFactory


@dataclass
class ReferenceNode(Expression):
    name: str
    type: str = 'reference'

    def __init_subclass__(cls, **kwargs: Unpack[ConfigDict]):
        super().__init_subclass__(**kwargs)
        AstTreeFactory.register(cls.type, lambda data, builder: ReferenceNode(name=data['name'], type=data['type']))

    def eval(self, context: Context, local: Optional[Context] = None) -> bool | float | torch.tensor:
        run_time = context.merge_with(local)

        return  run_time.get_declaration(self.name).value.eval(run_time)
