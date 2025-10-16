from physix.kinematics.quaternion import Quaternion
from physix.kinematics.position import Position
from mathx.linalg.vec.vec import Vec
from mathx.linalg.vec.opr.two_opranded import TwoOpranded
from typing import Sequence
from physix.dimension.unit.unit import Unit



class Pose(Vec):
    def __init__(self, position:Position, quaternion:Quaternion):
        self._position = position
        self._quaternion = quaternion

        concat_comps = TwoOpr(position, quaternion).concat().get_components()
        super().__init__(concat_comps)

    @classmethod
    def init_from_components(cls, comps: Sequence[float], position_unit:Unit, quaternion_unit:Unit) -> "Pose":
        x, y, z, qx, qy, qz, qw = map(float, comps[:7])
        pos = Position(x, y, z, position_unit)
        quat = Quaternion(qx, qy, qz, qw, position_unit)
        return cls(pos, quat)
