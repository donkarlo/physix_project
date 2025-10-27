from mathx.linalg.vec.opr.two_opranded import TwoOpranded
from physix.quantity.scalar_quantifiable import ScalarQuantity
from physix.quantity.type.kinematic.twist.angular import Angular
from physix.quantity.type.kinematic.twist.linear import Linear


class Twist(ScalarQuantity):
    def __init__(self, linear:Linear, angular:Angular):
        self._linear = linear
        self._angular = angular
        concated_vec= TwoOpranded(linear, angular).get_concated()
        super().__init__(concated_vec.get_components())