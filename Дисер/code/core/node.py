from __future__ import annotations

from pydantic import BaseModel

class Node(BaseModel):
    type: str

