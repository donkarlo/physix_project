from mathx.linalg.vec.opr.two_opranded import TwoOpranded
from mathx.linalg.vec.vec import Vec
from physix.kinematics.twist_angular import TwistAngular
from physix.kinematics.twist_linear import TwistLinear


class Twist(Vec):
    def __init__(self, twist_linear:TwistLinear, twist_angular:TwistAngular):
        self._linear = linear
        self._angular = angular
        concated_vec= TwoOpranded(twist_linear, twist_angular).get_concated()
        super().__init__(concated_vec.get_components())