from typing import List, Optional

from physix.world.obstacle import Obstacle


class World:
    """
    - The world is just for assessment as the exact location of obstacles such as walls are determined
    - world has the location of the obstacles in it
    - en
    """
    def __init__(self, obstacles: Optional[List[Obstacle]]=None):
        self._obstacles = obstacles

    def build_from_sdf(self, sdf:str)->None:
        """
        Building from Gazebo sdf
        """
        pass