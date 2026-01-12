from physix.quantity.scalar_quantifiable import ScalarQuantifiable


class Time(ScalarQuantifiable):
    def __init__(self, value: float):
        self._value = value

    def get_value(self)->float:
        return self._value