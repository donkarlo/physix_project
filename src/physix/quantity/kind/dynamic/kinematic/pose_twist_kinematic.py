from functools import cache
from mathx.linalg.tensor.vector.vector import Vector
from mathx.linalg.tensor.vector.operation.two_opranded import TwoOpranded
from physix.quantity.kind.dynamic.kinematic.twist.twist import Twist
from physix.quantity.vector_quantifiable import VectorQuantifiable
from physix.quantity.kind.dynamic.kinematic.pose.pose import Pose


class PoseTwistKinematic(VectorQuantifiable):
    def __init__(self, pose: Pose, twist: Twist):
        self._pose = pose
        self._twist = twist
        self._vec_representation = None

    def get_pose(self) -> Pose:
        return self._pose

    def get_twist(self) -> Twist:
        return self._twist

    @cache
    def get_vec_representation(self)->Vector:
        pose_vec = self._pose.get_vector_representation()
        twist_vec = self._twist.get_vec_representation()
        return TwoOpranded(pose_vec, twist_vec).concat()