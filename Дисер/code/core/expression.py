from code.

# Вычисляемый элемент
class Expression(Node):

    def eval(self, context: Context) -> int | float | torch.tensor:
        pass