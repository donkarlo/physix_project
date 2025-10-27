from physix.quantity.scalar_quantifiable import ScalarQuantity


class Time(ScalarQuantity):
    def __init__(self, t: float):
        super().__init__([t])