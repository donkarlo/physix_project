from mathx.linalg.vec.vec import Vec as LinalgVec

from physix.dimension.unit.unit import Unit


class Vec:
    def __init__(self, unit:Unit, val: LinalgVec):
        self._unit = unit
        self._val = val

    def get_unit(self)->Unit:
        return self._unit

    def get_val(self)-> LinalgVec:
        return self._val