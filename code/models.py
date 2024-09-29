""""Dataclasses for all the replies """
from __future__ import annotations

from dataclasses import dataclass
from typing import List
from typing import Any


@dataclass
class Variable:
    max: float
    min: float
    name: str
    unit: str
    value: float

    @staticmethod
    def from_dict(obj: Any) -> Variable:
        """" Convert json to Variable class

        Return:
            Variable"""
        return Variable(
            max=obj.get("Max"),
            min=obj.get("Min"),
            name=obj.get("Name"),
            unit=obj.get("Unit"),
            value=obj.get("Value"),
        )