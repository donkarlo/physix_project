from mathx.numbers.quaternion.quaternion import Quaternion
from physix.quantity.type.kinematic.pose.orientation.orientation import Orientation
from physix.quantity.type.kinematic.pose.position.position import Position
from mathx.linalg.vec.opr.two_opranded import TwoOpranded
from physix.quantity.vector_quantifiable import VectorQuantifiable


class Pose(VectorQuantifiable):
    def __init__(self, position: Position, orientation: Orientation):
        self._position = position
        self._orientation = orientation

        concat_comps = TwoOpranded(self._position.get_vec_representation(), self._orientation.get_vec_representation()).concat().get_components()

        self._vec_representation = Vec(concat_comps)

    def get_vec_representation(self):
        return self._vec_representation
