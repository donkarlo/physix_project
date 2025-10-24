from physix.dimension.unit.unit import Unit
from mathx.linalg.vec.vec import Vec


class TwistAngular(Quantity):
    """
    Linear velocity speed
    """
    def __init__(self, x:float, y:float, z:float):
        self._x = x
        self._y = y
        self._z = z
        super().__init__(np.asarray([self._x, self._x, self._x]))