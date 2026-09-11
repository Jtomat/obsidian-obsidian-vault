import torch

from code.ast_tree.context import Context
from code.ast_tree.node import Node


# Вычисляемый элемент
class Expression(Node):

    def eval(self, context: Context) -> int | float | torch.tensor:
        pass