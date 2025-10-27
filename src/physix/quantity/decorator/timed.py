from physix.quantity.scalar_quantifiable import ScalarQuantity
from physix.quantity.scalar_quantifiable import TensorQuantifiable
from physix.quantity.type.time import Time


class Timed(Decorator):
    def __init__(self, inner:TensorQuantifiable, time:Time):
        super().__init__(inner)
        self._time = time

    def get_time(self)->Time:
        return self._time