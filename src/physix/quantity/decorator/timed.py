from physix.quantity.quantity import Quantity
from physix.quantity.quantity import Quantifiable
from physix.quantity.type.time import Time


class Timed(Decorator):
    def __init__(self, inner:Quantifiable, time:Time):
        super().__init__(inner)
        self._time = time

    def get_time(self)->Time:
        return self._time