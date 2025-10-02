from mathx.linalg.vec.vec import Vec
class Position(Vec):
    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z
        super().__init__(np.asarray([self._x, self._y, self._z]))
