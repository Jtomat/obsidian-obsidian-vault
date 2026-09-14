import torch

from code.ast_tree.core.context import Context
from code.ast_tree.core.expression import Expression


class LiteralNode(Expression):
    type: str = 'literal'

    value: bool | float

    def eval(self, context: Context) -> bool | float | torch.tensor:
        return context