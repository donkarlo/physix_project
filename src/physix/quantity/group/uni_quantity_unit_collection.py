from typing import List

from physix.dimension.unit.unit import Unit
from physix.quantity.tensor_quantifiable import TensorQuantifiable


class UniQuantityUnitCollection:
    def __init__(self, unit:Unit, quantities:Optional[List[TensorQuantifiable]]=None):
        self._quantity = type(quantities[0])
        self._unit = unit
        self._quantities = quantities

    def add_quantity(self, quantity:TensorQuantifiable):
        self._quantities.append(quantity)
