from physix.quantity.kind.kinematic.pose.pose import Pose
from physix.quantity.kind.kinematic.twist.twist import Twist


class Motion:
    def __init__(self, pose: Pose, twist: Twist):
        self._pose = pose
        self._twist = twist