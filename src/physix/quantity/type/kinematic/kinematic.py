from physix.quantity.tensor_quantifiable import TensorQuantifiable
from physix.quantity.type.kinematic.pose.orientation.orientation import Orientation
from physix.quantity.type.kinematic.pose.pose import Pose


class Kinematic(TensorQuantifiable):
    def __init__(self, pose: Pose, orientation: Orientation):
        self._pose = pose
        self._orientation = orientation

    def get_pose(self) -> Pose:
        return self._pose

    def get_orientation(self) -> Orientation:
        return self._orientation