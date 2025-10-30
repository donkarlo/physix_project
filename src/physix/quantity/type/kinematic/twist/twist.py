from mathx.linalg.vec.opr.two_opranded import TwoOpranded
from physix.quantity.type.kinematic.twist.angular import Angular
from physix.quantity.type.kinematic.twist.linear import Linear
from physix.quantity.vector_quantifiable import VectorQuantifiable


class Twist(VectorQuantifiable):
    def __init__(self, linear:Linear, angular:Angular):
        self._linear = linear
        self._angular = angular

    def get_vec_representation(self) ->Vec:
        linear_vec = self._linear.get_vec_representation()
        angular_vec = self._angular.get_vec_representation()
        concated_vec = TwoOpranded(linear_vec, angular_vec).concat()