from dataclasses import dataclass

from code.ast_tree.core.context import Context
from code.ast_tree.core.expression import Expression
from code.ast_tree.core.node import Node


# Запись значения в контекст по имени
@dataclass
class Declaration(Node):
    name: str
    value: Expression

    def eval(self, context: Context) -> None:
        context.set_declaration(self)