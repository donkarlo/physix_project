from physix.quantity.scalar_quantifiable import ScalarQuantity
from physix.quantity.vector_quantifiable import VectorQuantifiable


class Orientation(VectorQuantifiable):
    def __init__(self, components:List[float]):
        self._components = components
        self._vec_representation = Vec(Components)
    def get_vec_representation(self)->Vec:
        return self._vec_representation