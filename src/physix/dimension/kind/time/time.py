from physix.dimension.unit.scalar import Scalar
from physix.dimension.unit.unit import Unit


class Time(Scalar):
    def __init__(self, value:float, unit:Unit):
        self._value = value
        self._unit = unit

    def convert_to_unit(self, unit:Union[Unit,str]):
        pass