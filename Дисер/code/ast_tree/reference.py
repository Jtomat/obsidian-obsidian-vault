from dataclasses import dataclass
from typing import Optional, Unpack, ClassVar, Dict, Any

import torch
from pydantic import ConfigDict
from torch import Tensor

from code.ast_tree.core.context import Context
from code.ast_tree.core.expression import Expression
from code.ast_tree.ast_tree_factory import AstTreeFactory
from code.ast_tree.core.node import Node


@dataclass
class ReferenceNode(Expression):
    name: str
    type: ClassVar[str]  = 'reference'


    @classmethod
    def from_dict(cls, data: Dict[str, Any], builder: AstTreeFactory) -> 'ReferenceNode':
        return ReferenceNode(name=data['name'])

    def eval(self, context: Context, local: Optional[Context] = None) -> bool | float | Tensor:
        run_time = context.merge_with(local)

        return  run_time.get_declaration(self.name).value.eval(run_time)
