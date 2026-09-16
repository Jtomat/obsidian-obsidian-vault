from dataclasses import dataclass
from typing import Optional, ClassVar, Dict, Any

from torch import Tensor

from code.ast_tree.ast_tree_factory import AstTreeFactory
from code.ast_tree.core.context import Context
from code.ast_tree.core.expression import Expression


@dataclass
class LiteralNode(Expression):
    value: bool | float| Tensor
    type: ClassVar[str]  = 'literal'

    @classmethod
    def from_dict(cls, data: Dict[str, Any], builder: AstTreeFactory) -> 'LiteralNode':
        return LiteralNode(value=data['value'])

    def eval(self, context: Context, local: Optional[Context] = None) -> bool | float | Tensor:
        return self.value
