from typing import Union, Optional

from physix.dimension.dimension import Dimension


class Unit:
    def __init__(self, id:Union[int,str], dimension: Optional[Dimension]=None):
        self._id = id
        self._dimension = dimension
