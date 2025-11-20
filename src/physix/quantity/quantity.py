from physix.quantity.quantifiable import Quantifiable


class Quantity(Quantifiable):
    def __init__(self, value: float) -> None:
        self._value = value

    def get_value(self) -> float:
        return self._value