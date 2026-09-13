
class BinaryOperation(Expression):

    operator: BinaryOperation

    left: Expression
    right: Expression

    def eval(self, context: Context, local: Optional[Context] = None) -> int | float | torch.tensor:
        left = self.left.eval(context)
        right = self.left.eval(context)

        has_tensor = int(not (torch.is_tensor(left) or torch.is_tensor(right)))

        return BINARY_OPERATORS_FUNCS[self.operator][has_tensor](left, right)