from typing import Optional

import torch

from code.ast_tree.context import Context
from code.ast_tree.expression import Expression


class ReferenceNode(Expression):
    type: str = 'reference'

    name: str

    def eval(self, context: Context, local: Optional[Context] = None) -> int | float | torch.tensor:
        return context.get_declaration(self.name).eval(context, local)