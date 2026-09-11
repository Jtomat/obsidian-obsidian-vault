from __future__ import annotations

from enum import Enum
from typing import Optional, Dict

import torch
from pydantic import BaseModel

class Node(BaseModel):
    type: str

