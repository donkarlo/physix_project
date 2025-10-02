from typing import Union

from physix.dimension.dimension import Dimension


class Unit:
    def __init__(self, dimension:Dimension, id:Union[int,str]):
        self._dimension = dimension
        self._id = id