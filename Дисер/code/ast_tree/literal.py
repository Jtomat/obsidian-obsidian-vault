import torch

from code.core.context import Context
from code.core.expression import Expression


class LiteralNode(Expression):
    type: str = 'literal'

    value: int | float

    def eval(self, context: Context) -> int | float | torch.tensor:
        return context