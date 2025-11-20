from physix.quantity.kind.kinematic.pose.orientation.orientation import Orientation


class Euler(Orientation):
    def __init__(self, roll:float, pitch, yaw:float):
        self._roll = roll
        self._pitch = pitch
        self._yaw = yaw
        super().__init__((self._roll, self._pitch, self._yaw))

    def convert_to_quaternion(self)->Quaternion:
        ...