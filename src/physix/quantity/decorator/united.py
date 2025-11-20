from physix.dimension.unit.unit import Unit
from physix.quantity.decorator.decorator import Decorator
from physix.quantity.quantifiable import Quantifiable


class United(Decorator):
    def __init__(self, inner:Quantifiable, unit:Unit):
        super().__init__(inner)
        self.unit = unit
