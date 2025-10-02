from mathx.linalg.vec.vec import Vec
from physix.dimension.unit.unit import Unit

class Scalar:
    def __init__(self, unit:Unit, value:float):
        self._unit = unit
        self._value = value

