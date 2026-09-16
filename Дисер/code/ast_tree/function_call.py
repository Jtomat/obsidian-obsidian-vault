from dataclasses import dataclass
from typing import Optional, Dict, Unpack

import torch
from pydantic import ConfigDict

from code.ast_tree.core.context import Context
from code.ast_tree.core.expression import Expression
from code.ast_tree.declaration.variable_declaration import VariableDeclaration
from code.ast_tree.literal import LiteralNode
from code.ast_tree.ast_tree_factory import AstTreeFactory



@dataclass
class FunctionCallNode(Expression):
    name: str
    arguments: Dict[str, Expression]

    type: str = 'function_call'

    def __init_subclass__(cls, **kwargs: Unpack[ConfigDict]):
        super().__init_subclass__(**kwargs)
        AstTreeFactory.register(cls.type, lambda data, builder: build_function_call(data, builder))

    def eval(self, context: Context, local: Optional[Context] = None) -> bool | float | torch.tensor:
        run_time = context.merge_with(local)

        func = run_time.get_function(self.name)

        if func is not None:
            eval_context = Context()

            for arg in func.arguments:
                literal_value = self.arguments[arg].eval(run_time)
                # внутри все параметры литералы для экономии при вычислениях
                eval_context.set_declaration(VariableDeclaration(name=arg, value=LiteralNode(value=literal_value)))

            return func.value.eval(run_time.merge_with(eval_context))

        raise AttributeError(f'Function with name "{self.name}" not found in runtime context."')


def build_function_call(data: dict, builder: AstTreeFactory) -> FunctionCallNode:
    args = {}
    for key, value in data['arguments']:
        args[key] = builder.build(value)
    return FunctionCallNode(name=data['name'], arguments=args, type=data['type'])