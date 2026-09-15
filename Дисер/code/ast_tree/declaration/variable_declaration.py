from code.ast_tree.declaration.declaration import Declaration


class VariableDeclaration(Declaration):
    type: str = 'variable_declaration'