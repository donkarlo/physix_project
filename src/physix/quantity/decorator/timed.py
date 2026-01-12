from physix.quantity.decorator.decorator import Decorator
from physix.quantity.quantifiable import Quantifiable


class Timed(Decorator):
    def __init__(self, inner:Quantifiable, time_value:float):
        # TODO: inner can not be quantity.time.time.Time
        Decorator.__init__(self, inner)
        self._time_value = time_value

    def get_time_value(self)->float:
        return self._time_value