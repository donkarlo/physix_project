class QuaternionPose:
    def __init__(self, position_list:List[float], quaternion_list:List[float]):
        self._position = Position(position_list)
        self._quaternion = Quaternion(quaternion_list)
        self._pose = Pose(self._position, self._quaternion)

    def get_timed_gaussian_distributed(self):
        return Timed(self._pose)