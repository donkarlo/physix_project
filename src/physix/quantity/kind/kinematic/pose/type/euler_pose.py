from mathx.numbers.quaternion.quaternion import Quaternion
from physix.quantity.kind.kinematic.pose.pose import Pose
from physix.quantity.kind.kinematic.pose.position.position import Position
from mathx.linalg.vec.opr.two_opranded import TwoOpranded
from typing import Sequence


class EulerPose(Pose):
    def __init__(self, position: Position, quaternion: Quaternion):
        self._position = position
        self._quaternion = quaternion

        concat_comps = TwoOpranded(position, quaternion).concat().get_components()
        super().__init__(self._position, self._quaternion)

    @classmethod
    def init_from_components(cls, comps: Sequence[float]) -> "QuaternionPose":
        x, y, z, qx, qy, qz, qw = map(float, comps[:7])
        pos = Position(x, y, z)
        quat = Quaternion(qx, qy, qz, qw)
        return cls(pos, quat)