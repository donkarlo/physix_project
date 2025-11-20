from physix.quantity.quantifiable import Quantifiable
from typing import runtime_checkable, Protocol


@runtime_checkable
class ScalarQuantifiable(Quantifiable, Protocol):
    def get_value(self)->float:
        ...