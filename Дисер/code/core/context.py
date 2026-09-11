from typing import Dict

import torch


class Context:
    declarations: Dict[str, "Declaration"]

    def get_declaration(self, name: str) -> int | float | torch.tensor:
        return self.declarations[name].value.eval(self)

    def set_declaration(self, declaration: "Declaration") -> None:
        self.declarations[declaration.name] = declaration

