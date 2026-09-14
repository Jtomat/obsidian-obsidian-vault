from typing import Optional

import torch

from code.ast_tree.core.context import Context
from code.ast_tree.core.expression import Expression


class ReferenceNode(Expression):
    type: str = 'reference'

    name: str

    def eval(self, context: Context, local: Optional[Context] = None) -> bool | float | torch.tensor:
        if local is None:
            return context.get_declaration(self.name)
        else:
            return context.merge_with(local).get_declaration(self.name)