from physix.dimension.unit.unit import Unit
from typing import List, Optional
import numpy as np
from mathx.linalg.vec.vec import Vec
from typing import Sequence
from physix.dimension.unit.vec import Vec as UnitedVec


class Position(UnitedVec):
    def __init__(self, x: float, y: float, z: float, unit:Unit):
        super().__init__(unit, [x, y, z])
        self._x = x
        self._y = y
        self._z = z

        self._unit = unit


    @classmethod
    def init_from_components(cls, comps: Sequence[float], unit:Unit) -> "Position":
        x, y, z = map(float, comps[:3])
        return cls(x, y, z, unit)

    def get_x(self) -> float:
        return self._x

    def get_y(self) -> float:
        return self._y

    def get_z(self) -> float:
        return self._z

    def get_unit(self) -> Unit:
        return self._unit
