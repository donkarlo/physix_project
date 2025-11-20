from physix.quantity.kind.kinematic.pose.position.position import Position


class Cartesian(Position):
    def __init__(self, x: float, y: float, z: float):
        super().__init__([x, y, z])
        self._x = x
        self._y = y
        self._z = z

    @classmethod
    def init_from_components(cls, comps: Sequence[float]) -> "Position":
        x, y, z = map(float, comps[:3])
        return cls(x, y, z, unit)

    def get_x(self) -> float:
        return self._x

    def get_y(self) -> float:
        return self._y

    def get_z(self) -> float:
        return self._z