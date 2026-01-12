from physix.quantity.quantifiable import Quantifiable
from typing import runtime_checkable, Protocol
from typing import Union


@runtime_checkable
class ScalarQuantifiable(Quantifiable, Protocol):
    _value: Union[float, int]
    def get_value(self)->float:
        ...