from physix.quantity.quantity import Quantity


class Time(Quantity):
    def __init__(self, t: float):
        super().__init__([t])