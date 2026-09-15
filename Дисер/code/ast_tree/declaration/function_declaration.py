from code.ast_tree.core.expression import Expression
from code.ast_tree.declaration.declaration import Declaration
from code.ast_tree.reference import ReferenceNode


class FunctionDeclaration(Declaration):
    type: str = 'function_declaration'

    arguments: list[ReferenceNode]
    exec: Expression