from code.ast_tree.expression import Expression
from typing import TypeVar, Generic

T = TypeVar('T')

class UnaryMathOperationNode(Expression, Generic(T)):

    operator: UnaryOperation
    operand: Expression