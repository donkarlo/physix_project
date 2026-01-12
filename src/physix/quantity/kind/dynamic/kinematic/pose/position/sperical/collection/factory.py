from mathx.geometry.euclidean.coordinate.three_dimension.spherical import Spherical as MathSpherical
from physix.quantity.kind.dynamic.kinematic.pose.position.sperical.spherical import Spherical


class Factory:
    @staticmethod
    def get_cartesian_by_radiuses_and_xy_angle_increment_rate(radises: List[float], xy_angle_increment_rate: float,
                                                              start: float,
                                                              xy_z_angles: Union[float, List[float]] = 0) -> List[Spherical]:
        if isinstance(xy_z_angles, list):
            if len(radises) != len(xy_z_angles):
                raise ValueError("radises and xy_angles must have the same length or a constant to be propegated")

        spericals: List["Spherical"] = []
        for counter, radius in enumerate(radises):
            xy_angle = start + counter * xy_angle_increment_rate
            if isinstance(xy_z_angles, list):
                spherical = MathSpherical(radius, xy_angle, xy_z_angles[counter])
            elif isinstance(xy_z_angles, float):
                spherical = Spherical(MathSpherical(radius, xy_angle, xy_z_angles))

            spericals.append(spherical)
        return spericals