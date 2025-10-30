from physix.quantity.scalar_quantifiable import ScalarQuantifiable


class Time(ScalarQuantifiable):
    def __init__(self, t: float):
        self._time_value = t