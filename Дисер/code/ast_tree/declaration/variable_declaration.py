from dataclasses import dataclass
from typing import ClassVar, Unpack, Any, Dict

from pydantic import ConfigDict

from code.ast_tree.ast_tree_factory import AstTreeFactory
from code.ast_tree.declaration.declaration import Declaration

@dataclass
class VariableDeclaration(Declaration):
    type: ClassVar[str]  = 'variable_declaration'


    @classmethod
    def from_dict(cls, data: Dict[str, Any], builder: AstTreeFactory) -> 'VariableDeclaration':
        return VariableDeclaration(name=data['name'], value=builder.build(data['value']))


