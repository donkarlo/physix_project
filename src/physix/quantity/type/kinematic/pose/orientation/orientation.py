from physix.quantity.vector_quantifiable import VectorQuantifiable
from mathx.linalg.tensor.vector.vector import Vector
from typing import override, List


class Orientation(VectorQuantifiable):
    def __init__(self, components:List[float]):
        self._components = components
        self._vector_representation = Vector(Components)
    @override
    def get_vector_representation(self)->Vector:
        return self._vector_representation