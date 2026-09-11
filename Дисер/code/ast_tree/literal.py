import torch

from code.ast_tree.context import Context
from code.ast_tree.expression import Expression


class LiteralNode(Expression):
    type: str = 'literal'

    value: int | float

    def eval(self, context: Context) -> int | float | torch.tensor:
        return context