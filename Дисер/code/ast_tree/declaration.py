from code.ast_tree.context import Context
from code.ast_tree.expression import Expression
from code.ast_tree.node import Node
from code.ast_tree.reference import ReferenceNode


# Запись значения в контекст по имени
class Declaration(Node):
    name: str
    value: Expression

    def eval(self, context: Context) -> None:
        context.set_declaration(self)


class VariableDeclaration(Declaration):
    type: str = 'variable_declaration'


class FunctionDeclaration(Declaration):
    type: str = 'function_declaration'

    arguments: list[ReferenceNode]
    exec: Expression