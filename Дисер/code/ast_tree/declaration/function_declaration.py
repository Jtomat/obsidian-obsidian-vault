from dataclasses import dataclass

from code.ast_tree.declaration.declaration import Declaration

@dataclass
class FunctionDeclaration(Declaration):
    arguments: list[str]
    type: str = 'function_declaration'
