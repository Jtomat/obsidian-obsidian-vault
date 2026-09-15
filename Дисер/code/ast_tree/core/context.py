import torch
from typing import Dict
from code.ast_tree.declaration.declaration import Declaration


class Context:
    declarations: Dict[str, Declaration]


    def setup(self, declarations: Dict[str, Declaration]) -> "Context":
        self.declarations = declarations
        return self

    def get_declaration(self, name: str) -> bool | float | torch.tensor:
        return self.declarations[name].value.eval(self)

    def set_declaration(self, declaration: Declaration) -> None:
        self.declarations[declaration.name] = declaration

    def merge_with(self, other: "Context") -> "Context":
        dict_base = self.declarations.copy()

        for i, k, v in enumerate(other.declarations):
            dict_base[k] = v

        return Context().setup(dict_base)
