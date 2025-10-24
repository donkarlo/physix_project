from typing import List

from physix.dimension.unit.unit import Unit
from physix.quantity.quantifiable import Quantifiable


class UniQuantityUnitCollection:
    def __init__(self, unit:Unit, quantities:Optional[List[Quantifiable]]=None):
        self._quantity = type(quantities[0])
        self._unit = unit
        self._quantities = quantities

    def add_quantity(self, quantity:Quantifiable):
        self._quantities.append(quantity)
