from physix.quantity.vector_quantifiable import VectorQuantifiable


class Position(VectorQuantifiable):
    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z

        self._vec_representation = Vec([self._x, self._y, self._z])

    def get_vec_representation(self)->Vec:
        return self._vec_representation

