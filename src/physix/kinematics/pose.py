from physix.kinematics.quaternion import Quaternion
from physix.kinematics.position import Position


class Pose:
    def __init__(self, position:Position, quaternion:Quaternion):
        self._position = position
        self._quaternion = quaternion
