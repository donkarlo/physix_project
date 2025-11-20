from physix.quantity.scalar_quantifiable import ScalarQuantifiable


class Time(ScalarQuantifiable):
    def __init__(self, time_value: float):
        self._time_value = time_value

    def get_value(self)->float:
        return self._time_value

    def get_time_value(self)->float:
        return self._time_value