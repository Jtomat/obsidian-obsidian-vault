from dataclasses import dataclass

from code.ast_tree.declaration.declaration import Declaration

@dataclass
class VariableDeclaration(Declaration):
    type: str = 'variable_declaration'

