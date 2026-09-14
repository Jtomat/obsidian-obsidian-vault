import torch

from code.ast_tree.core.context import Context
from code.ast_tree.core.node import Node


# Вычисляемый элемент
class Expression(Node):

    def eval(self, context: Context) -> bool | float | torch.tensor:
        pass