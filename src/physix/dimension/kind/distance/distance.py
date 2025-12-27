from physix.dimension.unit.unit import Unit


class Distance:
    def __init__(self, value:float, unit:Unit):
        self._value = value
        self._unit = unit