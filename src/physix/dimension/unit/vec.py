from mathx.linalg.vec.vec import Vec as BasicVec
from typing import Union, Sequence
from physix.dimension.unit.unit import Unit
import numpy as np


class Vec(BasicVec):
    def __init__(self, unit:Unit, components: Union[Sequence[float], np.ndarray]):
        super().__init__(components)
        self._unit = unit

    def get_unit(self)->Unit:
        return self._unit

    def get_val(self)-> BasicVec:
        return self._vec