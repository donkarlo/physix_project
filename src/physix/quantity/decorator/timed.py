from physix.quantity.decorator.decorator import Decorator
from physix.quantity.quantifiable import Quantifiable


class Timed(Decorator):
    def __init__(self, inner:Quantifiable, time_value:float):
        # if has timed
        super().__init__(inner)
        self._time_value = time_value

    def get_time_value(self)->float:
        return self._time_value