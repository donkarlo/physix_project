from physix.dimension.unit.unit import Unit
from mathx.linalg.tensor.vector.vector import Vector
from physix.quantity.vector_quantifiable import VectorQuantifiable
from typing import override


class Angular(VectorQuantifiable):
    """
    Linear velocity speed
    """
    def __init__(self, x:float, y:float, z:float):
        self._x = x
        self._y = y
        self._z = z
        self._vector_representation = Vector([self._x, self._y, self._y])

    @override
    def get_vector_representation(self) -> "Vector":
        return self._vector_representation