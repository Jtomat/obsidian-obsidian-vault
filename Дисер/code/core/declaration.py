from code.core.context import Context
from code.core.expression import Expression
from code.core.node import Node

# Запись значения в контекст по имени
class Declaration(Node):
    name: str
    value: Expression

    def eval(self, context: Context) -> None:
        context.set_declaration(self)