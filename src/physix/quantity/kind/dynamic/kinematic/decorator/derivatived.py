from physix.dimension.unit.interface import Interface
from physix.quantity.kind.dynamic.kinematic.decorator.decorator import Decorator
from physix.quantity.kind.dynamic.kinematic.pose.pose import Pose


class Derivatived(Decorator):
    """
    Every time a higher order derivative is added
    """

    def __init__(self, derivatived_pose: Pose, inner: Interface):
        # TODO: check that orientation kind is the same after first derivative, mostly it must be linear
        Decorator.__init__(self, inner)
        self._derivatived_pose = derivatived_pose

    def get_derivatived_pose(self) -> Pose:
        return self._derivatived_pose
