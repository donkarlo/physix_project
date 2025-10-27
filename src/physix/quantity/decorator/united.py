from physix.dimension.unit.unit import Unit
from physix.quantity.tensor_quantifiable import TensorQuantifiable


class United(Decorator):
    def __init__(self, inner:TensorQuantifiable, unit:Unit):
        super().__init__(inner)
        self.unit = unit
