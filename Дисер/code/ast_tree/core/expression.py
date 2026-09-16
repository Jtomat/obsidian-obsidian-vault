from typing import Optional

from torch import Tensor

from code.ast_tree.core.context import Context
from code.ast_tree.core.node import Node


# Вычисляемый элемент
class Expression(Node):

    def eval(self, context: Context, local: Optional[Context] = None) -> bool | float | Tensor:
        pass
