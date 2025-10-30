from functools import cache
from mathx.linalg.tensor.vector.vector import Vector
from mathx.linalg.tensor.vector.operation.two_opranded import TwoOpranded
from physix.quantity.vector_quantifiable import VectorQuantifiable
from physix.quantity.type.kinematic.pose.orientation.orientation import Orientation
from physix.quantity.type.kinematic.pose.pose import Pose


class Kinematic(VectorQuantifiable):
    def __init__(self, pose: Pose, orientation: Orientation):
        self._pose = pose
        self._orientation = orientation
        self._vec_representation = None

    def get_pose(self) -> Pose:
        return self._pose

    def get_orientation(self) -> Orientation:
        return self._orientation

    @cache
    def get_vec_representation(self)->Vector:
        pose_vec = self._pose.get_vector_representation()
        orientation_vec = self._orientation.get_vec_representation()
        return TwoOpranded(pose_vec, orientation_vec).concat()