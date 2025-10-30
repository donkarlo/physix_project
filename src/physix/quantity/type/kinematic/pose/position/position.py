from physix.quantity.vector_quantifiable import VectorQuantifiable
from mathx.linalg.tensor.vector.vector import Vector
from typing import override

class Position(VectorQuantifiable):
    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z

        self._vector_representation = Vector([self._x, self._y, self._z])

    @override
    def get_vector_representation(self)->Vector:
        return self._vector_representation