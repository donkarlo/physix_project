from mathx.geometry.euclidean.coordinate.three_dimension.spherical import Spherical as MathSpherical
from physix.quantity.kind.kinematic.pose.position.position import Position


class Spherical(Position):
    def __init__(self, x:float, y:float, z:float):
        super().__init__(x,y,z)