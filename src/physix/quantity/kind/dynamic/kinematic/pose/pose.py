from physix.quantity.kind.dynamic.kinematic.pose.orientation.orientation import Orientation
from physix.quantity.kind.dynamic.kinematic.pose.position.position import Position
from physix.quantity.vector_quantifiable import VectorQuantifiable
from mathx.linalg.tensor.vector.operation.two_opranded import TwoOpranded
from mathx.linalg.tensor.vector.vector import Vector



class Pose(VectorQuantifiable):
    def __init__(self, position: Position, orientation: Orientation):
        self._position = position
        self._orientation = orientation

        concat_comps = TwoOpranded(self._position.get_vector_representation(), self._orientation.get_vector_representation()).concat().get_components()

        self._vector_representation = Vector(concat_comps)

    def get_vector_representation(self):
        return self._vector_representation

    def get_orientation(self):
        return self._orientation
    def get_position(self):
        return self._position
