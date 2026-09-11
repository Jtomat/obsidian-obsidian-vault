from code.ast_tree.expression import Expression


class UnaryMathOperationNode(Expression):

    operator: UnaryOperation
    operand: Expression